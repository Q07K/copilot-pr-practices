# 게시판 ERD (Entity Relationship Diagram) - SQLite 버전

## 데이터베이스 설정
- **Database**: SQLite
- **File**: `copilot_board.db`
- **ORM**: SQLAlchemy 2.0+

## 테이블 구조

### 1. users (사용자)
```
┌─────────────────┬──────────────┬──────────────┬─────────────┐
│ Column          │ Type         │ Constraint   │ Description │
├─────────────────┼──────────────┼──────────────┼─────────────┤
│ id              │ INTEGER      │ PK, AI       │ 사용자 ID   │
│ username        │ VARCHAR(50)  │ UNIQUE, NN   │ 사용자명    │
│ email           │ VARCHAR(100) │ UNIQUE, NN   │ 이메일      │
│ hashed_password │ VARCHAR(255) │ NN           │ 암호화된 비밀번호 │
│ full_name       │ VARCHAR(100) │ NULL         │ 전체 이름   │
│ is_active       │ BOOLEAN      │ DEFAULT TRUE │ 활성 상태   │
│ is_superuser    │ BOOLEAN      │ DEFAULT FALSE│ 관리자 여부 │
│ created_at      │ DATETIME     │ NN           │ 생성일시    │
│ updated_at      │ DATETIME     │ NULL         │ 수정일시    │
└─────────────────┴──────────────┴──────────────┴─────────────┘
```

### 2. posts (게시글)
```
┌─────────────┬──────────────┬──────────────┬─────────────┐
│ Column      │ Type         │ Constraint   │ Description │
├─────────────┼──────────────┼──────────────┼─────────────┤
│ id          │ INTEGER      │ PK, AI       │ 게시글 ID   │
│ title       │ VARCHAR(200) │ NN           │ 게시글 제목 │
│ content     │ TEXT         │ NN           │ 게시글 내용 │
│ author_id   │ INTEGER      │ FK, NN       │ 작성자 ID   │
│ view_count  │ INTEGER      │ DEFAULT 0    │ 조회수      │
│ created_at  │ DATETIME     │ NN           │ 생성일시    │
│ updated_at  │ DATETIME     │ NULL         │ 수정일시    │
└─────────────┴──────────────┴──────────────┴─────────────┘
```

### 3. comments (댓글)
```
┌─────────────┬──────────────┬──────────────┬─────────────┐
│ Column      │ Type         │ Constraint   │ Description │
├─────────────┼──────────────┼──────────────┼─────────────┤
│ id          │ INTEGER      │ PK, AI       │ 댓글 ID     │
│ content     │ TEXT         │ NN           │ 댓글 내용   │
│ post_id     │ INTEGER      │ FK, NN       │ 게시글 ID   │
│ author_id   │ INTEGER      │ FK, NN       │ 작성자 ID   │
│ created_at  │ DATETIME     │ NN           │ 생성일시    │
│ updated_at  │ DATETIME     │ NULL         │ 수정일시    │
└─────────────┴──────────────┴──────────────┴─────────────┘
```

## 관계도

```
       users                     posts                    comments
  ┌─────────────┐           ┌─────────────┐          ┌─────────────┐
  │ id (PK)     │ 1       N │ id (PK)     │ 1      N │ id (PK)     │
  │ username    │◄──────────┤ author_id   │◄─────────┤ post_id     │
  │ email       │           │ title       │          │ author_id   │
  │ ...         │           │ content     │          │ content     │
  └─────────────┘           │ ...         │          │ ...         │
                            └─────────────┘          └─────────────┘
                                                           │
                            ┌─────────────┐               │
                            │ users       │ 1           N │
                            │ id (PK)     │◄──────────────┘
                            │ username    │
                            │ ...         │
                            └─────────────┘
```

## 관계 설명

1. **User ↔ Post (1:N)**
   - 한 사용자는 여러 게시글을 작성할 수 있음
   - `posts.author_id` → `users.id`

2. **User ↔ Comment (1:N)**
   - 한 사용자는 여러 댓글을 작성할 수 있음
   - `comments.author_id` → `users.id`

3. **Post ↔ Comment (1:N)**
   - 한 게시글에는 여러 댓글이 있을 수 있음
   - `comments.post_id` → `posts.id`

## 제약사항

- **PK**: Primary Key (기본키)
- **FK**: Foreign Key (외래키)
- **AI**: Auto Increment (자동증가)
- **NN**: Not Null (필수값)
- **UNIQUE**: 고유값

## 인덱스

- `users.username` (고유 인덱스)
- `users.email` (고유 인덱스)
- `posts.title` (인덱스)
- `posts.author_id` (외래키 인덱스)
- `comments.post_id` (외래키 인덱스)
- `comments.author_id` (외래키 인덱스)
