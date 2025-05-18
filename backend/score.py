def calculate_privacy_score(data):
    score = 100
    if data.get("email_found"):
        score -= 20
    if data.get("phone_found"):
        score -= 20
    if data.get("address_found"):
        score -= 20
    if data.get("public_posts"):
        score -= len(data["public_posts"]) * 2
    score = max(score, 0)
    return score
