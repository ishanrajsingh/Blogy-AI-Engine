from fastapi import APIRouter
from app.models.schemas import BlogRequest
from app.services.keyword_service import analyze_keyword
from app.services.prompt_service import build_prompt
from app.services.llm_service import generate_blog
from app.services.seo_service import seo_score
from app.services.formatter_service import format_output

router = APIRouter()

@router.post("/generate-blog")
def generate_blog_api(request: BlogRequest):
    keyword_data = analyze_keyword(request.keyword)

    prompt = build_prompt(keyword_data)
    raw_blog = generate_blog(prompt)

    formatted_blog = format_output(raw_blog)
    seo = seo_score(formatted_blog, request.keyword)

    return {
        "blog": formatted_blog,
        "seo": seo,
        "keywords": keyword_data
    }