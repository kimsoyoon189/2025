import streamlit as st
import random

# -------------------------------
# 데이터 정의
# -------------------------------
HAIR_RULES = [
    {
        "name": "롱 레이어드 웨이브 + 사이드 파트",
        "tags": ["여성", "롱", "레이어드", "웨이브"],
        "fit": {"oval": 3, "round": 2, "square": 2, "heart": 3, "long": 1, "diamond": 3, "triangle": 2},
        "color_fit": ["봄웜", "가을웜"],
        "bangs": ["없음", "시스루"],
        "notes": "사이드 파트로 비대칭을 주면 광대·턱선을 부드럽게.",
        "maintenance": "중",
        "dye": ["애쉬브라운", "초코브라운", "로즈골드"]
    },
    {
        "name": "턱선 길이의 블런트 보브",
        "tags": ["여성", "숏", "보브", "스트레이트"],
        "fit": {"oval": 3, "round": 1, "square": 2, "heart": 3, "long": 2, "diamond": 2, "triangle": 2},
        "color_fit": ["여름쿨", "겨울쿨"],
        "bangs": ["없음", "풀뱅"],
        "notes": "끝선이 둔탁해 볼륨감↑, 목선 강조.",
        "maintenance": "중",
        "dye": ["블루블랙", "와인레드", "애쉬그레이"]
    },
    {
        "name": "텍스처 픽시 크롭",
        "tags": ["여성", "남성", "숏", "픽시"],
        "fit": {"oval": 3, "round": 2, "square": 3, "heart": 2, "long": 3, "diamond": 3, "triangle": 2},
        "color_fit": ["겨울쿨"],
        "bangs": ["없음"],
        "notes": "짧은 숏컷으로 시원하고 세련된 인상, 직모보단 텍스처 넣기 추천.",
        "maintenance": "하",
        "dye": ["블랙", "애쉬블루", "실버"]
    }
]

# -------------------------------
# 추천 함수
# -------------------------------
def recommend_style(face_shape, personal_color, bang_preference):
    results = []
    for style in HAIR_RULES:
        score = style["fit"].get(face_shape, 0)
        if personal_color in style["color_fit"]:
            score += 1
        if bang_preference in style["bangs"]:
            score += 1
        if score > 0:
            results.append((score, style))
    results.sort(key=lambda x: -x[0])
    return results

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="헤어스타일 추천기", page_icon="💇‍♀️", layout="centered")

st.title("💇 퍼스널 헤어스타일 추천기")
st.write("얼굴형, 퍼스널컬러, 앞머리 여부를 입력하면 어울리는 스타일과 염색 컬러를 추천해드려요 ✨")

# 입력값 받기
face_shape = st.selectbox("👤 얼굴형 선택", ["oval", "round", "square", "heart", "long", "diamond", "triangle"])
personal_color = st.selectbox("🎨 퍼스널컬러 선택", ["봄웜", "여름쿨", "가을웜", "겨울쿨"])
bang_preference = st.selectbox("✂️ 앞머리 스타일", ["없음", "있음", "시스루", "풀뱅"])

if st.button("추천 받기 🎲"):
    results = recommend_style(face_shape, personal_color, bang_preference)
    if not results:
        st.warning("조건에 맞는 스타일이 없어요 😢 옵션을 바꿔보세요.")
    else:
        best = results[0][1]
        st.success(f"✨ 추천 스타일: **{best['name']}**")
        st.write(f"📌 특징: {best['notes']}")
        st.write(f"🔧 손질 난이도: {best['maintenance']}")
        st.write(f"🎨 어울리는 염색 컬러: {', '.join(best['dye'])}")
        st.write(f"💡 앞머리 추천: {', '.join(best['bangs'])}")




