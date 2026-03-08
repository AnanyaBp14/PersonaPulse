# PersonaPulse AI - Serverless Architecture

## Overview
PersonaPulse leverages an AWS-native, event-driven serverless architecture to ensure high scalability, rapid deployment, and minimal operational overhead.

## AWS Services Utilized
1. **Amazon API Gateway:** Provides secure REST endpoints and manages CORS policies for the React frontend.
2. **AWS Lambda:** Orchestrates batch content generation. Utilizes Python `ThreadPoolExecutor` to handle parallel, asynchronous invocations of Bedrock to prevent timeout constraints.
3. **Amazon Bedrock (Nova Micro):** The foundational AI layer. Selected specifically for its ultra-low latency, strict JSON adherence, and cost-efficiency ($200 credits optimized).
4. **Amazon DynamoDB:** A NoSQL datastore that provides stateful persistence for historical campaigns, elevating the system from a stateless wrapper to a robust SaaS application.
5. **AWS IAM:** Ensures secure, least-privilege access between Lambda, DynamoDB, and Bedrock.