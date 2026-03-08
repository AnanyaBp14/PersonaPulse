# PersonaPulse Cost Estimation

This document estimates the operational cost of running PersonaPulse on AWS.

---

# Architecture Cost Components

The system uses serverless AWS services.

Primary cost contributors:

Amazon Bedrock  
AWS Lambda  
Amazon API Gateway  

---

# Amazon Bedrock Cost

Model used:

amazon.nova-micro-v1

Estimated cost:

~$0.0003 per request

Example usage:

1000 generations per day

Daily cost:

$0.30

Monthly cost:

$9

---

# AWS Lambda Cost

Lambda pricing depends on:

Execution time  
Memory allocation  
Number of requests

Example:

Execution time: 1 second  
Requests: 1000/day  

Monthly estimate:

~$1

---

# API Gateway Cost

Estimated:

$3 per million requests

Example usage:

30,000 requests per month

Cost:

~$0.10

---

# Total Estimated Monthly Cost

Bedrock: $9  
Lambda: $1  
API Gateway: $0.10  

Estimated Total:

~$10/month

---

# Cost Optimization Strategies

Use smaller Bedrock models  
Limit request payload size  
Cache repeated prompts  
Batch platform generation  

---

# Scaling Projection

If the system grows to:

100,000 requests/month

Estimated cost:

~$40–$60/month

Still affordable for startup usage.
