#!/usr/bin/env python3
"""
SQLite 데이터베이스 초기화 스크립트
"""

import os
import sys
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.db.database import engine, Base
from app.models import User, Post, Comment


def create_database():
    """SQLite 데이터베이스 파일과 테이블 생성"""
    print("SQLite 데이터베이스 초기화 중...")
    
    # 데이터베이스 파일 경로 확인
    db_path = "./copilot_board.db"
    if os.path.exists(db_path):
        print(f"기존 데이터베이스 파일 발견: {db_path}")
        response = input("기존 데이터베이스를 삭제하고 새로 생성하시겠습니까? (y/N): ")
        if response.lower() == 'y':
            os.remove(db_path)
            print("기존 데이터베이스 파일을 삭제했습니다.")
        else:
            print("데이터베이스 초기화를 취소했습니다.")
            return
    
    # 모든 테이블 생성
    Base.metadata.create_all(bind=engine)
    print(f"데이터베이스가 성공적으로 생성되었습니다: {db_path}")
    print("생성된 테이블:")
    print("- users (사용자)")
    print("- posts (게시글)")
    print("- comments (댓글)")


def main():
    """메인 함수"""
    try:
        create_database()
    except Exception as e:
        print(f"데이터베이스 생성 중 오류 발생: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
