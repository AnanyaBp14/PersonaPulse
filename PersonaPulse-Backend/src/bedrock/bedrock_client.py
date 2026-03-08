import boto3
from .model_config import MODEL_ID, INFERENCE_CONFIG

# Initialized outside the handler to optimize Lambda cold starts
client = boto3.client("bedrock-runtime")

def invoke_model(prompt: str):
    response = client.converse(
        modelId=MODEL_ID,
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig=INFERENCE_CONFIG
    )
    return response["output"]["message"]["content"][0]["text"]