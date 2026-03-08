def format_breakdown(hook_score, cta_score, hashtag_score, emotion_score):
    return [
        {"metric": "Hook Strength", "score": hook_score, "reason": "Question/Power word detected" if hook_score > 5 else "Hook lacks impact"},
        {"metric": "CTA Clarity", "score": cta_score, "reason": "Strong action verbs used" if cta_score > 5 else "CTA is weak or missing"},
        {"metric": "Hashtag Quality", "score": hashtag_score, "reason": "Optimal density (3-8 tags)" if hashtag_score > 5 else "Too many or too few tags"},
        {"metric": "Emotional Tone", "score": emotion_score, "reason": "Emotional resonance detected" if emotion_score > 5 else "Tone is overly dry"}
    ]