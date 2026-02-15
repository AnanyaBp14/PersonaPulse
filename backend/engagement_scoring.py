def score_content(content):
    score = 50

    if "?" in content:
        score += 10
    if "!" in content:
        score += 5
    if len(content) < 400:
        score += 10
    if "call to action" in content.lower():
        score += 10

    return min(score, 100)
