from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# 데이터베이스 URL 설정 (SQLite 사용)
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite:///./copilot_board.db"
)

# SQLAlchemy 엔진 생성 (SQLite용 설정 추가)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={
        "check_same_thread": False,  # SQLite에 필요한 설정
        "timeout": 20,  # 락 대기 시간 (초)
    },
    echo=False,  # SQL 쿼리 로깅 (개발시에는 True로 설정 가능)
    pool_pre_ping=True,  # 연결 유효성 검사
)

# 세션 로컬 클래스 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성
Base = declarative_base()


def get_db():
    """데이터베이스 세션 의존성"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
