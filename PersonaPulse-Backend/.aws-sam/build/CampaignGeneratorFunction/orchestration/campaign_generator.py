from prompts.prompt_engine import build_prompt
from bedrock.bedrock_client import invoke_model
from scoring.engagement_scoring import calculate_score
from utils.json_parser import safe_parse
from utils.logger import log_error


def generate_campaign(body, platform):
    try:
        prompt = build_prompt(
            body["idea"],
            platform,
            body["audience"],
            body["tone"],
            body["language"],
            body.get("cultural", True),
            body.get("include_image", True if platform == "Instagram" else False)
        )

        raw_output = invoke_model(prompt)

        try:
            structured = safe_parse(raw_output)
        except Exception:
            # 🔥 AUTO RETRY WITH STRICTER PROMPT
            retry_prompt = prompt + "\n\nREMINDER: Return ONLY raw JSON."
            raw_output = invoke_model(retry_prompt)
            structured = safe_parse(raw_output)

        structured["engagement"] = calculate_score(structured, platform)

        return structured

    except Exception as e:
        log_error(f"Failed generating for {platform}: {str(e)}")
        return {"error": str(e)}