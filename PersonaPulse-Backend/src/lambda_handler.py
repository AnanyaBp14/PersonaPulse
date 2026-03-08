import json
import os
import sys

# Allow Lambda to access modules inside src folder
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Core imports
from validation.request_validator import validate_request
from orchestration.batch_handler import handle_batch_request
from utils.dynamodb_client import save_campaign
from utils.logger import log_info, log_error


# Global CORS headers
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,POST"
}


def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": CORS_HEADERS,
        "body": json.dumps(body)
    }


def lambda_handler(event, context):
    """
    PersonaPulse Campaign Generator

    Flow:
    Validate Request
    → Generate AI Campaign (Bedrock)
    → Save to DynamoDB
    → Return Response
    """

    try:
        log_info("Received request")

        # Handle CORS preflight
        http_method = None

        if "requestContext" in event:
            http_method = event.get("requestContext", {}).get("http", {}).get("method")

        if http_method == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": json.dumps({"message": "CORS preflight success"})
            }

        # Parse request body
        body = event.get("body", "{}")

        if isinstance(body, str):
            body = json.loads(body)

        log_info(f"Request body: {body}")

        # Validate request
        is_valid, error = validate_request(body)

        if not is_valid:
            log_error(f"Validation failed: {error}")

            return build_response(
                400,
                {"error": error}
            )

        # Generate campaign using orchestration layer
        batch_result = handle_batch_request(body)

        # Save campaign to DynamoDB
        campaign_id = save_campaign(batch_result)

        if campaign_id:
            batch_result["campaign_id"] = campaign_id

        log_info(f"Campaign generated successfully. ID: {campaign_id}")

        # Success response
        return build_response(
            200,
            batch_result
        )

    except Exception as e:

        log_error(f"System Error in PersonaPulse: {str(e)}")

        return build_response(
            500,
            {
                "error": "Internal Server Error",
                "details": str(e)
            }
        )