"""
SQLite 최적화를 위한 설정 유틸리티
"""

from sqlalchemy import event, text
from sqlalchemy.engine import Engine
import sqlite3


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """SQLite 연결시 성능 최적화를 위한 PRAGMA 설정"""
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        
        # Foreign Key 제약 조건 활성화
        cursor.execute("PRAGMA foreign_keys=ON")
        
        # WAL 모드 활성화 (동시성 향상)
        cursor.execute("PRAGMA journal_mode=WAL")
        
        # 동기화 설정 (성능 향상)
        cursor.execute("PRAGMA synchronous=NORMAL")
        
        # 캐시 크기 설정 (메모리 사용량 증가, 성능 향상)
        cursor.execute("PRAGMA cache_size=10000")
        
        # 임시 저장소를 메모리에 설정
        cursor.execute("PRAGMA temp_store=MEMORY")
        
        cursor.close()


def optimize_database(engine):
    """데이터베이스 최적화 쿼리 실행"""
    with engine.connect() as conn:
        # 통계 정보 업데이트
        conn.execute(text("ANALYZE"))
        
        # 인덱스 재구성
        conn.execute(text("REINDEX"))
        
        # 빈 공간 정리
        conn.execute(text("VACUUM"))
        
        conn.commit()
    
    print("SQLite 데이터베이스 최적화가 완료되었습니다.")
