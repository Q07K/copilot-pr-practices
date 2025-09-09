from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .comment import Comment


class PostBase(BaseModel):
    """게시글 기본 스키마"""
    title: str = Field(..., min_length=1, max_length=200, description="게시글 제목")
    content: str = Field(..., min_length=1, description="게시글 내용")


class PostCreate(PostBase):
    """게시글 생성 스키마"""
    pass


class PostUpdate(BaseModel):
    """게시글 수정 스키마"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)


class PostInDB(PostBase):
    """데이터베이스에서 반환되는 게시글 스키마"""
    id: int
    author_id: int
    view_count: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Post(PostInDB):
    """API 응답용 게시글 스키마"""
    author: "User"
    comments: List["Comment"] = []


class PostList(PostInDB):
    """게시글 목록용 스키마 (댓글은 포함하지 않음)"""
    author: "User"
    comment_count: Optional[int] = 0
