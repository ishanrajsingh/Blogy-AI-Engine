def analyze_keyword(keyword: str):
    keyword = keyword.lower()

    intent = "informational"
    if any(x in keyword for x in ["best", "top", "vs", "review"]):
        intent = "commercial"
    elif any(x in keyword for x in ["buy", "price", "cheap"]):
        intent = "transactional"

    secondary_keywords = [
        f"{keyword} tools",
        f"{keyword} software",
        f"{keyword} platforms",
        "AI content generation",
        "SEO automation India",
        "organic traffic growth",
        "blog automation platform"
    ]

    is_blgy = "blogy" in keyword

    return {
        "primary": keyword,
        "secondary": secondary_keywords,
        "intent": intent,
        "is_blgy": is_blgy
    }