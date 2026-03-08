#!/bin/bash
echo "Building SAM application..."
sam build

echo "Deploying to AWS..."
sam deploy --guided \
  --stack-name personapulse-backend \
  --capabilities CAPABILITY_IAM \
  --region us-east-1