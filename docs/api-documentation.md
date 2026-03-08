# PersonaPulse API Documentation

## Base Endpoint

The PersonaPulse backend exposes a REST API through Amazon API Gateway.

Base URL:

https://juoe0v4c3a.execute-api.us-east-1.amazonaws.com/prod

---

# Endpoint

POST /generate

Generates AI-powered marketing content.

---

# Request Body

Content-Type: application/json

Example:

{
  "idea": "AI transforming rural education",
  "platforms": ["LinkedIn", "Instagram"],
  "audience": "Students",
  "tone": "Professional",
  "language": "English"
}

---

# Request Parameters

idea  
Description: Core campaign idea  
Type: String  
Required: Yes  

platforms  
Description: List of target platforms  
Type: Array  
Example: ["LinkedIn","Instagram"]

audience  
Description: Target audience segment  
Type: String  

tone  
Description: Tone of the generated content  
Type: String  

language  
Description: Language for generated content  
Type: String  

---

# Response Body

Example response:

{
  "campaign_title": "AI transforming rural education",
  "campaign_id": "a8f7c12d",
  "results": {
    "LinkedIn": {
      "hook": "AI is redefining rural education in India.",
      "content": "Technology is enabling personalized learning for millions of students.",
      "cta": "Join the movement to transform education.",
      "engagement": {
        "total": 87
      }
    }
  }
}

---

# Response Fields

campaign_title  
Campaign idea title

campaign_id  
Unique campaign identifier

results  
Generated posts grouped by platform

hook  
Opening line

content  
Main post body

cta  
Call to action

hashtags  
Suggested hashtags

engagement.total  
AI engagement score (0-100)

---

# Error Response

Example error:

{
  "error": "Model failed to return valid JSON"
}

Possible HTTP codes:

400 Bad Request  
500 Internal Server Error
