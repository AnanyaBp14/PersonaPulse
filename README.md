PersonaPulse AI

AI-Powered Omnichannel Content Orchestration Engine for the Creator Economy

PersonaPulse AI is a serverless generative-AI platform that transforms a single marketing idea into optimized, platform-specific content for multiple digital channels.

Built on AWS Bedrock + Lambda + API Gateway, the system enables creators, startups, and Indian SMBs to generate personalized content campaigns instantly.

🚀 Problem Statement

Digital creators, startups, and SMBs struggle to produce high-quality content tailored to each platform.

A single marketing idea must often be rewritten multiple times for:



LinkedIn

Instagram

Twitter

WhatsApp

This process is:

• Time-consuming

• Requires marketing expertise

• Leads to inconsistent messaging

Small teams cannot afford dedicated content strategists.

💡 Our Solution

PersonaPulse AI converts one idea into a full omnichannel campaign.

Users input a single campaign concept, and the AI generates:



Hook

Main content

Call-to-Action

Hashtags

Engagement score

All content is optimized for the selected platform and audience.

🌟 Key Features

AI Campaign Generator

Transforms a single idea into complete marketing posts.



Omnichannel Output

Generates optimized posts for:

• LinkedIn

• Twitter

• Instagram

• WhatsApp Broadcast

Bharat Localization

Supports regional content styles including:

• English

• Hinglish

• Hindi

• Marathi

• Kannada

AI Engagement Score

Custom heuristic scoring system that evaluates:



Hook strength

CTA clarity

Hashtag density

Emotional tone

Image Prompt Generator

Automatically generates AI image prompts for visual content creation.

🧠 Why AI is Required

Traditional rule-based software cannot convert a high-level idea into nuanced platform-specific marketing content.

Generative AI enables:

• Semantic understanding of marketing ideas

• Tone adaptation for different audiences

• Cultural localization for Indian markets

• Structured JSON output for automated workflows

Without AI, this level of intelligent content transformation is impossible.

⚙️ Architecture

React Frontend

↓

Amazon API Gateway

↓

AWS Lambda (Campaign Orchestrator)

↓

Amazon Bedrock (Nova Micro Model)

↓

Custom Engagement Scoring Logic

↓

Amazon DynamoDB (Campaign Storage)

☁️ AWS Services Used

ServicePurposeAmazon BedrockGenerative AI content generationAWS LambdaBackend orchestration and scoringAmazon API GatewayREST API interfaceAmazon DynamoDBCampaign storageAWS AmplifyFrontend hosting and authenticationAmazon S3Static web hosting📊 AI Workflow

1️⃣ User enters campaign idea

2️⃣ Lambda constructs structured prompt

3️⃣ Bedrock generates platform-specific content

4️⃣ Engagement scoring logic evaluates output

5️⃣ Results rendered in dashboard UI

🧩 Tech Stack

Frontend

• React (Vite)

• TailwindCSS

• Amplify Auth

Backend

• Python (AWS Lambda)

• Amazon Bedrock

• DynamoDB

Infrastructure

• API Gateway

• AWS Amplify Hosting

🖥️ Live Prototype

Deployed link: https://main.d1c5b2jxa4xlij.amplifyapp.com/

🎥 Demo Video

Demo link here.

Example

https://youtu.be/demo

📦 Installation

Frontend

npm install

npm run dev

Backend

sam build

sam deploy

🏆 Impact

PersonaPulse reduces the time required to create a full marketing campaign from 3 hours to under 10 seconds.

It empowers Indian creators and SMBs to scale their digital presence without hiring marketing teams.

📜 License

MIT License
