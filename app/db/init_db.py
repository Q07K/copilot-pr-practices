"""
게시판 애플리케이션용 데이터베이스 초기화 스크립트
"""
from sqlalchemy import create_engine
from app.db.database import Base
from app.models import User, Post, Comment
import os
from dotenv import load_dotenv

load_dotenv()

def init_db():
    """데이터베이스 테이블 생성"""
    DATABASE_URL = os.getenv(
        "DATABASE_URL", 
        "sqlite:///./copilot_board.db"
    )
    
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}  # SQLite에 필요한 설정
    )
    
    # 모든 테이블 생성
    Base.metadata.create_all(bind=engine)
    print("데이터베이스 테이블이 성공적으로 생성되었습니다.")

if __name__ == "__main__":
    init_db()
