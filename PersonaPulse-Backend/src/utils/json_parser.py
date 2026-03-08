import json
import re


def safe_parse(raw_output: str):
    """
    Production-safe JSON parser for LLM output.
    Handles:
    - Markdown wrappers
    - Extra text before JSON
    - Extra text after JSON
    - Trailing commas
    """

    if not raw_output:
        raise ValueError("Empty model response.")

    # Remove markdown fences
    cleaned = re.sub(r"```json|```", "", raw_output)

    # Extract first JSON object
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found in model output.")

    json_str = match.group()

    # Remove trailing commas
    json_str = re.sub(r",\s*}", "}", json_str)
    json_str = re.sub(r",\s*]", "]", json_str)

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON structure: {str(e)}")