import json
import os
# Core imports - ensure these folders have __init__.py files
from validation.request_validator import validate_request
from orchestration.batch_handler import handle_batch_request
from utils.dynamodb_client import save_campaign
from utils.response_builder import build_response
from utils.logger import log_info, log_error

def lambda_handler(event, context):
    """
    Main entry point for PersonaPulse Campaign Generation.
    Flow: Validate -> Orchestrate (Bedrock) -> Save (DynamoDB) -> Respond
    """
    try:
        log_info("Received new campaign request")
        
        # 1. Parse the incoming body
        body = event.get("body", "{}")
        if isinstance(body, str):
            body = json.loads(body)

        # 2. Validate the request (Checks for target, audience, tone, and language)
        is_valid, error = validate_request(body)
        if not is_valid:
            log_error(f"Validation failed: {error}")
            return build_response(400, {"error": error})

        # 3. Orchestrate campaign generation
        # This calls batch_handler which uses the new prompt_engine.py
        batch_result = handle_batch_request(body)

        # 4. Save the generated campaign to DynamoDB (Ref: CampaignTable)
        campaign_id = save_campaign(batch_result)
        if campaign_id:
            batch_result["campaign_id"] = campaign_id

        log_info(f"Campaign generated successfully. ID: {campaign_id}")
        
        # 5. Return success response with CORS headers
        return build_response(200, batch_result)

    except Exception as e:
        log_error(f"System Error in PersonaPulse: {str(e)}")
        # Provide detailed error info for easier debugging in CloudWatch
        return build_response(500, {
            "error": "Internal Server Error",
            "details": str(e)
        })