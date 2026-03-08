# PersonaPulse – System Architecture

## Overview

PersonaPulse is an AI-powered content orchestration platform that converts a single idea into optimized social media posts for multiple platforms.

The system uses a **serverless AWS architecture** to ensure scalability, reliability, and cost efficiency.

---

## High-Level Architecture

User Browser
 →
React Frontend (Campaign Builder UI)
 →
Amazon API Gateway
 →
AWS Lambda (AI Orchestrator)
 →
Amazon Bedrock (Generative AI Model)
 →
Engagement Scoring Logic
 →
Structured JSON Response
 →
Frontend Dashboard Rendering

---

## Architectural Layers

### Frontend Layer

Technology:
- React (Vite)
- TailwindCSS
- Axios

Responsibilities:
- Collect user inputs
- Configure campaign parameters
- Display generated content
- Render platform cards

---

### API Layer

Service: **Amazon API Gateway**

Responsibilities:

- Expose REST endpoint
- Handle HTTP requests
- Enable CORS
- Route requests to Lambda

Endpoint:

POST /generate

---

### Compute Layer

Service: **AWS Lambda**

Responsibilities:

- Validate user inputs
- Construct AI prompt
- Call Amazon Bedrock
- Parse JSON output
- Compute engagement scores
- Return structured response

Lambda functions are **stateless**, enabling horizontal scalability.

---

### AI Layer

Service: **Amazon Bedrock**

Model used:

amazon.nova-micro-v1

Responsibilities:

- Generate structured marketing content
- Adapt tone and platform style
- Generate hooks, content, CTA

Output format is strictly JSON.

---

### Optional Storage Layer (Future)

Future additions include:

Amazon DynamoDB
- Store campaign history
- Save generated posts

Amazon S3
- Archive generated content
- Store images and assets

---

## Architecture Diagram

User → React Frontend → API Gateway → Lambda → Amazon Bedrock → Response → Dashboard


---

## Key Design Principles

Serverless Architecture  
Stateless Processing  
Low Latency AI Generation  
Scalable Cloud Infrastructure  

---

## Benefits

Auto-scaling with Lambda  
Low operational cost  
Managed AI via Bedrock  
Fast content generation 
