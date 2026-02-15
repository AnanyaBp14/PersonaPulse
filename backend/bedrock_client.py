import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def generate_content(prompt):

    response = bedrock.converse(
        modelId="amazon.nova-micro-v1:0",
        messages=[
            {
                "role": "user",
                "content": [
                    {"text": prompt}
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 700,
            "temperature": 0.6
        }
    )

    raw_output = response["output"]["message"]["content"][0]["text"]

    try:
        json_start = raw_output.find("{")
        json_end = raw_output.rfind("}") + 1
        json_string = raw_output[json_start:json_end]
        structured_output = json.loads(json_string)
        return structured_output

    except Exception:
        return {
            "hook": "Generated Content",
            "content": raw_output,
            "cta": "",
            "hashtags": ""
        }
