import boto3
import uuid
import time
import os
from .logger import log_error

# Use environment variable injected by AWS SAM
TABLE_NAME = os.environ.get("DYNAMODB_TABLE", "PersonaPulseCampaigns")
dynamodb = boto3.resource('dynamodb')

def save_campaign(campaign_data):
    try:
        table = dynamodb.Table(TABLE_NAME)
        campaign_id = str(uuid.uuid4())
        item = {
            "campaign_id": campaign_id,
            "timestamp": int(time.time()),
            "campaign_data": campaign_data
        }
        table.put_item(Item=item)
        return campaign_id
    except Exception as e:
        log_error(f"DynamoDB Error: {str(e)}")
        return None