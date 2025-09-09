from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .post import PostInDB


class CommentBase(BaseModel):
    """댓글 기본 스키마"""
    content: str = Field(..., min_length=1, description="댓글 내용")


class CommentCreate(CommentBase):
    """댓글 생성 스키마"""
    post_id: int = Field(..., description="게시글 ID")


class CommentUpdate(BaseModel):
    """댓글 수정 스키마"""
    content: Optional[str] = Field(None, min_length=1)


class CommentInDB(CommentBase):
    """데이터베이스에서 반환되는 댓글 스키마"""
    id: int
    post_id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Comment(CommentInDB):
    """API 응답용 댓글 스키마"""
    author: "User"
