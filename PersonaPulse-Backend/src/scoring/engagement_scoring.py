from .scoring_rules import POWER_WORDS, EMOTIONAL_WORDS, CTA_WORDS
from .score_breakdown import format_breakdown

def calculate_score(content_json, platform):
    hook = content_json.get("hook", "")
    content = content_json.get("content", "")
    cta = content_json.get("cta", "")
    hashtags = content_json.get("hashtags", [])

    hook_score = 25 if "?" in hook or any(w in hook.lower() for w in POWER_WORDS) else 10
    cta_score = 25 if any(w in cta.lower() for w in CTA_WORDS) else 10
    hashtag_score = 25 if 3 <= len(hashtags) <= 8 else 10
    emotion_score = 25 if any(w in content.lower() for w in EMOTIONAL_WORDS) else 10

    total_score = hook_score + cta_score + hashtag_score + emotion_score

    return {
        "total": min(total_score, 99),
        "details": format_breakdown(hook_score, cta_score, hashtag_score, emotion_score)
    }