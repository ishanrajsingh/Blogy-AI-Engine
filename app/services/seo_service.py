import textstat

def seo_score(blog: str, keyword: str):
    words = blog.split()
    word_count = len(words)

    keyword_count = blog.lower().count(keyword.lower())
    density = (keyword_count / word_count) * 100 if word_count else 0

    readability = textstat.flesch_reading_ease(blog)

    headings = blog.count("## ")
    subheadings = blog.count("### ")

    faqs = "faq" in blog.lower()
    cta = any(x in blog.lower() for x in ["contact", "try", "get started", "sign up"])
    snippet = "what is" in blog.lower()

    score = 0

    if 0.5 <= density <= 2:
        score += 15

    if word_count > 1200:
        score += 20

    if headings >= 6:
        score += 15

    if subheadings >= 2:
        score += 10

    if readability > 20:
        score += 10

    if faqs:
        score += 10

    if cta:
        score += 10

    if snippet:
        score += 10

    return {
        "score": score,
        "word_count": word_count,
        "keyword_density": round(density, 2),
        "readability": readability,
        "headings": headings,
        "subheadings": subheadings,
        "faq_present": faqs,
        "cta_present": cta,
        "snippet_ready": snippet
    }