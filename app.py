import streamlit as st
import json
from datetime import datetime
from pathlib import Path

# 데이터 파일 경로
DATA_FILE = Path("books.json")

# 데이터 로드
def load_books():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# 데이터 저장
def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

# 세션 상태 초기화
if "books" not in st.session_state:
    st.session_state.books = load_books()

# 페이지 설정
st.set_page_config(page_title="독서 기록", page_icon="📚", layout="wide")

# 제목
st.title("📚 나의 독서 기록")
st.markdown("---")

# 사이드바: 책 추가
with st.sidebar:
    st.header("📖 새 책 추가")

    title = st.text_input("책 제목")
    author = st.text_input("저자")
    status = st.selectbox("읽기 상태", ["읽고 싶은 책", "읽는 중", "완료"])
    rating = st.slider("별점", 0, 5, 0)
    review = st.text_area("감상평")
    start_date = st.date_input("시작일", value=None)
    end_date = st.date_input("완료일", value=None)

    if st.button("책 추가", type="primary", use_container_width=True):
        if title:
            new_book = {
                "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
                "title": title,
                "author": author,
                "status": status,
                "rating": rating,
                "review": review,
                "start_date": start_date.isoformat() if start_date else None,
                "end_date": end_date.isoformat() if end_date else None,
                "created_at": datetime.now().isoformat()
            }
            st.session_state.books.append(new_book)
            save_books(st.session_state.books)
            st.success(f"'{title}' 추가됨!")
            st.rerun()
        else:
            st.error("책 제목을 입력해주세요.")

# 메인 영역: 통계
col1, col2, col3, col4 = st.columns(4)

total = len(st.session_state.books)
reading = len([b for b in st.session_state.books if b["status"] == "읽는 중"])
completed = len([b for b in st.session_state.books if b["status"] == "완료"])
wishlist = len([b for b in st.session_state.books if b["status"] == "읽고 싶은 책"])

col1.metric("전체", f"{total}권")
col2.metric("읽는 중", f"{reading}권")
col3.metric("완료", f"{completed}권")
col4.metric("읽고 싶은 책", f"{wishlist}권")

st.markdown("---")

# 필터
filter_status = st.selectbox("필터", ["전체", "읽고 싶은 책", "읽는 중", "완료"])

# 책 목록 표시
if filter_status == "전체":
    filtered_books = st.session_state.books
else:
    filtered_books = [b for b in st.session_state.books if b["status"] == filter_status]

if not filtered_books:
    st.info("등록된 책이 없습니다. 사이드바에서 책을 추가해주세요.")
else:
    for i, book in enumerate(reversed(filtered_books)):
        with st.expander(f"{'⭐' * book['rating'] if book['rating'] > 0 else '☆'} {book['title']} - {book['author'] or '저자 미상'}"):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.write(f"**상태:** {book['status']}")
                st.write(f"**별점:** {'⭐' * book['rating'] if book['rating'] > 0 else '없음'}")
                if book.get("start_date"):
                    st.write(f"**시작일:** {book['start_date']}")
                if book.get("end_date"):
                    st.write(f"**완료일:** {book['end_date']}")
                if book.get("review"):
                    st.write(f"**감상평:** {book['review']}")

            with col2:
                if st.button("삭제", key=f"delete_{book['id']}", type="secondary"):
                    st.session_state.books = [b for b in st.session_state.books if b["id"] != book["id"]]
                    save_books(st.session_state.books)
                    st.rerun()
