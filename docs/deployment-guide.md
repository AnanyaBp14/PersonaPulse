# PersonaPulse Deployment Guide

This document explains how to deploy the PersonaPulse system.

---

# Backend Deployment

The backend uses AWS Lambda and API Gateway.

## Step 1 – Deploy Lambda

1. Open AWS Console
2. Go to AWS Lambda
3. Create a new function
4. Runtime: Python 3.11
5. Upload the backend code

---

## Step 2 – Configure Bedrock Access

Attach IAM role with permission:

bedrock:InvokeModel

Example policy:

Allow access to:

amazon.nova-micro-v1

---

## Step 3 – Create API Gateway

1. Open API Gateway
2. Create REST API
3. Add resource:

/generate

4. Add method:

POST

5. Connect integration to Lambda

---

## Step 4 – Enable CORS

Enable CORS for the endpoint to allow frontend requests.

Allowed origin:

*

Allowed methods:

POST

---

# Frontend Deployment

The frontend is built using React.

---

## Step 1 – Install Dependencies

npm install

---

## Step 2 – Set Environment Variable

Create a `.env` file.

Example:

VITE_API_URL=https://juoe0v4c3a.execute-api.us-east-1.amazonaws.com/prod/generate

---

## Step 3 – Run Locally

npm run dev

---

# Production Deployment (Recommended)

Frontend deployment options:

AWS Amplify  
Amazon S3 + CloudFront  

---

## Amplify Deployment

1. Push code to GitHub
2. Connect repository in AWS Amplify
3. Build automatically
4. Deploy live URL

---

# Deployment Outcome

Users can access the application through a web browser and generate AI-powered marketing campaigns.
