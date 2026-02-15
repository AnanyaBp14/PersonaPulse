def build_prompt(idea, platform, audience, tone):

    return f"""
You are an expert digital content strategist.

Generate a {platform} post.

Target audience: {audience}
Tone: {tone}

STRICT RULES:
- Return ONLY valid JSON.
- Do NOT include explanations.
- Do NOT include markdown.
- Do NOT include extra text outside JSON.

Return JSON in this exact format:

{{
  "hook": "Strong engaging opening line",
  "content": "Platform-optimized main content body",
  "cta": "Clear call to action",
  "hashtags": "Relevant hashtags separated by spaces"
}}

Idea:
{idea}
"""
