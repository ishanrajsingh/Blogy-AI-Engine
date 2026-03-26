from pydantic import BaseModel

class BlogRequest(BaseModel):
    keyword: str