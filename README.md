 PersonaPulse AI
AI-Powered Multi-Platform Content Personalization Engine

Built with Amazon Bedrock (Serverless)

 Overview

PersonaPulse AI transforms a single content idea into platform-optimized, audience-personalized posts using Generative AI.

Instead of manually rewriting content for LinkedIn, Instagram, Twitter, YouTube, or blogs, PersonaPulse intelligently adapts tone, structure, and engagement strategy using Amazon Bedrock foundation models.

This project demonstrates meaningful AI usage in real-world content workflows.

Problem Statement

Content creators, students, startups, and marketing teams struggle with:

Rewriting content for multiple platforms

Adjusting tone for different audiences

Maintaining brand consistency

Improving engagement without guesswork

Manual rewriting is repetitive and time-consuming.

Solution

PersonaPulse AI:

Accepts a core idea

Adapts it for selected platform

Personalizes tone and audience

Generates structured output (Hook, Content, CTA, Hashtags)

Predicts engagement score

All powered by Amazon Bedrock.

 Why AI?

This problem requires:

Semantic understanding

Context-aware rewriting

Tone transformation

Platform-aware formatting

Structured JSON generation

Traditional rule-based systems cannot handle this.

Amazon Bedrock enables intelligent, scalable content transformation.

Architecture
User (Browser)
      ↓
React Frontend (SPA)
      ↓
Amazon API Gateway
      ↓
AWS Lambda
      ↓
Amazon Bedrock (Nova Micro)
      ↓
Structured JSON Response
      ↓
Frontend Rendering

 AWS Services Used

Amazon Bedrock (Nova Micro – Serverless)

AWS Lambda (Backend logic)

Amazon API Gateway (REST endpoint)

IAM Roles (Secure Bedrock access)

CloudWatch (Monitoring & Logs)

Features

Platform selection (LinkedIn, Instagram, Twitter, YouTube, Blog)

Audience targeting

Tone customization

Structured JSON output

Engagement scoring system

AI-powered prompt conditioning

Serverless scalable backend

Futuristic AI frontend UI

API Structure
Endpoint
POST /generate

Request Body
{
  "idea": "AI transforming rural education",
  "platform": "LinkedIn",
  "audience": "Students",
  "tone": "Professional"
}

Response Body
{
  "hook": "...",
  "content": "...",
  "cta": "...",
  "hashtags": "...",
  "engagement_score": 85
}

Project Structure
PersonaPulse/
│
├── frontend/        # React SPA
├── backend/         # Lambda + Bedrock integration
├── requirements.md  # Functional & Non-functional requirements
├── design.md        # System design document
├── README.md
└── LICENSE

 Local Setup
Frontend
cd frontend
npm install
npm start


Runs on:

http://localhost:3000

Deployment

Backend deployed as:

AWS Lambda (Python)

API Gateway (Regional REST API)

Bedrock Serverless Model (Nova Micro)

 Scalability

Fully serverless

Auto-scaling Lambda

Stateless backend

Bedrock managed inference

Horizontally scalable architecture

 Security

IAM role-based Bedrock access

HTTPS-only API communication

Input validation

No persistent sensitive data storage

🛣 Future Roadmap

Brand voice memory

Multi-platform batch generation

A/B testing

Content calendar

Analytics dashboard

User authentication (Cognito)

S3 content storage

CloudFront deployment

Demo

Video pitch available in submission materials.

Built For Hackathon

Track: AI for Media, Content & Digital Experiences
Theme: Meaningful AI for real-world workflows

 License

MIT License
