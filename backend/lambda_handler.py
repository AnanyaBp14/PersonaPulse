import json
from bedrock_client import generate_content
from prompt_engine import build_prompt
from engagement_scoring import score_content

def lambda_handler(event, context):

    try:
        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event

        idea = body.get("idea")
        platform = body.get("platform")
        audience = body.get("audience")
        tone = body.get("tone")

        if not idea:
            return {
                "statusCode": 400,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"error": "Idea is required"})
            }

        prompt = build_prompt(idea, platform, audience, tone)

        structured_output = generate_content(prompt)

        combined_text = (
            structured_output.get("hook", "") + " " +
            structured_output.get("content", "") + " " +
            structured_output.get("cta", "")
        )

        score = score_content(combined_text)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "hook": structured_output.get("hook"),
                "content": structured_output.get("content"),
                "cta": structured_output.get("cta"),
                "hashtags": structured_output.get("hashtags"),
                "engagement_score": score
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
