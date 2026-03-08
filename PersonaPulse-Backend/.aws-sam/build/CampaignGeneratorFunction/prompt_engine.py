from .platform_rules import PLATFORM_RULES
from .language_templates import LANGUAGE_HINTS

def build_prompt(
    idea,
    platform,
    audience,
    tone,
    language,
    cultural=True,
    include_image=False
):
    """
    Builds a strict, structured prompt for Amazon Nova Micro
    optimized for long-form content and native script enforcement.
    """

    # -----------------------------
    # Cultural Context Injection
    # -----------------------------
    cultural_hint = ""
    if cultural:
        cultural_hint = """
CRITICAL CULTURAL RULE:
Naturally incorporate relevant Indian context:
- UPI, Tier-2/3 cities, MSMEs, Local festivals (Diwali, Ugadi, etc.)
Do NOT force context if irrelevant.
"""

    # -----------------------------
    # Image Prompt Field
    # -----------------------------
    image_schema_field = ""
    image_instruction_block = ""

    if include_image:
        image_schema_field = '"image_prompt": "Detailed AI image generation prompt",'
        image_instruction_block = """
VISUAL REQUIREMENT:
Generate a cinematic, production-grade AI image prompt aligned with the content.
"""

    # -----------------------------
    # Language Enforcement Block
    # -----------------------------
    language_block = f"""
CRITICAL LANGUAGE ENFORCEMENT:
You MUST generate the ENTIRE JSON values (hook, content, cta) strictly in: {language}

STRICT SCRIPT RULES:
- If language is Kannada → Use ONLY Kannada Script (ಕನ್ನಡ ಲಿಪಿ). Do NOT use Devanagari.
- If language is Marathi/Hindi → Use ONLY Devanagari Script.
- If language is Hinglish → Mix Hindi + English in Roman Script.

Language Guidance:
{LANGUAGE_HINTS.get(language, "Use professional English.")}
"""

    # -----------------------------
    # JSON Strictness Block
    # -----------------------------
    json_strict_block = """
STRICT OUTPUT RULES:
Return ONLY a single raw JSON object. No explanations, no markdown code blocks, no intro/outro text.
"""

    # -----------------------------
    # Final Prompt Assembly
    # -----------------------------
    prompt = f"""
You are PersonaPulse AI — an elite campaign generator for Indian SMBs.

CAMPAIGN INPUT:
Idea: {idea} | Platform: {platform} | Audience: {audience} | Tone: {tone} | Language: {language}

PLATFORM CONSTRAINTS:
{PLATFORM_RULES.get(platform, "Use structured professional formatting.")}

{language_block}

{cultural_hint}

{image_instruction_block}

CONTENT STRUCTURE REQUIREMENTS:
- Hook must be platform-optimized.
- Content must be LONG-FORM, detailed, and highly readable.
- CTA must be clear and actionable.

{json_strict_block}

JSON SCHEMA:
{{
  "hook": "Powerful opening line",
  "content": "Main body of the post (Long-form)",
  "cta": "Clear call to action",
  "hashtags": ["#tag1", "#tag2", "#tag3"],
  {image_schema_field.rstrip(',')}
}}
"""

    return prompt.strip()