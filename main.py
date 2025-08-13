# app.py
import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="저녁 메뉴 추천", page_icon="🍽", layout="centered")

# 제목
st.title("🍽 오늘 저녁 뭐 먹지?")

# 메뉴 리스트
menus = [
    "김치찌개", "된장찌개", "비빔밥", "불고기", "삼겹살", "치킨", "피자", "햄버거", "파스타",
    "초밥", "떡볶이", "쌀국수", "부대찌개", "라멘", "순두부찌개", "돈까스", "마라탕", "쭈꾸미 볶음"
]

# 사용자 메뉴 입력 기능
st.sidebar.header("메뉴 추가하기")
new_menu = st.sidebar.text_input("추가할 메뉴")
if st.sidebar.button("메뉴 추가"):
    if new_menu and new_menu not in menus:
        menus.append(new_menu)
        st.sidebar.success(f"'{new_menu}' 추가 완료!")
    elif new_menu in menus:
        st.sidebar.warning("이미 있는 메뉴입니다.")
    else:
        st.sidebar.error("메뉴 이름을 입력하세요.")

# 추천 버튼
if st.button("메뉴 추천받기 🍽"):
    choice = random.choice(menus)
    st.success(f"오늘 저녁은 **{choice}** 어떠세요? 😋")

# 현재 메뉴 목록 보기
with st.expander("📜 현재 메뉴 목록 보기"):
    st.write(menus)
