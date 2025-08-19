import streamlit as st
import random

# --- 데이터 (15가지 예시 중 일부) ---
HAIR_RULES = [
    {
        "name": "롱 레이어드 웨이브 + 사이드 파트",
        "tags": ["여성", "롱", "레이어드", "웨이브"],
        "fit": {"oval": 3, "round": 2, "square": 2, "heart": 3, "long": 1, "diamond": 3, "triangle": 2},
        "color_fit": ["봄웜", "가을웜"],  # 퍼스널컬러 적합도
        "notes": "사이드 파트로 비대칭을 주면 광대·턱선을 부드럽게.",
        "maintenance": "중"
    },
    {
        "name": "턱선 길이의 블런트 보브",
        "tags": ["여성", "숏", "보브", "스트레이트"],
        "fit": {"oval": 3, "round": 1, "square": 2, "heart": 3, "long": 2, "diamond": 2, "triangle": 2},
        "color_fit": ["여름쿨", "겨울쿨"],
        "notes": "끝선이 둔탁해 볼륨감↑, 목선 강조.",
        "maintenance": "중"
    },
    {
        "name": "텍스처 픽시 크롭",
        "tags": ["여성", "남성", "숏", "픽시"],
        "fit": {"oval": 3, "round": 2, "square": 3, "heart": 2, "long": 2, "diamond": 3, "triangle": 2},
        "color_fit": ["겨울쿨", "여름쿨"],
        "notes": "윗머리 텍스처로 정수리 볼륨 살리기.",
        "maintenance": "하"
    },
    {
        "name": "울프컷 셰기",
        "tags": ["여성", "남성", "미디엄", "레이어드"],
        "fit": {"oval": 2, "round": 2, "square": 3, "heart": 2, "long": 3, "diamond": 3, "triangle": 2},
        "color_fit": ["봄웜", "가을웜"],
        "notes": "윗볼륨+아웃라인로 세로 비율 보정.",
        "maintenance": "중"
    },
    {
        "name": "센터 파트 스트레이트 롱",
        "tags": ["여성", "롱", "스트레이트"],
        "fit": {"oval": 3, "round": 1, "square": 2, "heart": 2, "long": 1, "diamond": 3, "triangle": 2},
        "color_fit": ["겨울쿨"],
        "notes": "깔끔하지만 둥근/긴 얼굴은 주의 필요.",
        "maintenance": "하"
    },
    # ... 나머지 스타일도 color_fit 추가 가능
]

# 얼굴형 매핑
FACE_ALIASES = {
    "계란형": "oval", "긴얼굴": "long", "둥근형": "round", "각진형": "square",
    "하트형": "heart", "다이아": "diamond", "삼각형": "triangle"
}

def normalize_face(face_shape: str) -> str:
    for k, v in FACE_ALIASES.items():
        if k == face_shape:
            return v
    return face_shape.lower()

def score_style(rule, face_key, gender, length, low_maint, personal_color):
    score = rule["fit"].get(face_key, 0)
    if gender and gender in rule["tags"]:
        score += 0.5
    if length and length in rule["tags"]:
        score += 0.5
    if low_maint and rule["maintenance"] == "하":
        score += 0.5
    if personal_color and personal_color in rule.get("color_fit", []):
        score += 0.7  # 퍼스널컬러 가중치
    score += random.uniform(-0.1, 0.1)
    return score

def recommend(face_shape, gender, length, low_maint, personal_color, top_k=5):
    face_key = normalize_face(face_shape)
    scored = []
    for r in HAIR_RULES:
        s = score_style(r, face_key, gender, length, low_maint, personal_color)
        scored.append((s, r))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [r for _, r in scored[:top_k]]

# --- Streamlit UI ---
st.title("💇 얼굴형 & 퍼스널컬러 기반 헤어스타일 추천기")

face_shape = st.selectbox("👉 얼굴형을 골라주세요", list(FACE_ALIASES.keys()))
gender = st.selectbox("👉 성별", ["무관", "남성", "여성"])
length = st.selectbox("👉 원하는 머리 길이", ["무관", "숏", "미디엄", "롱"])
personal_color = st.selectbox("👉 퍼스널컬러", ["무관", "봄웜", "여름쿨", "가을웜", "겨울쿨"])
low_maint = st.checkbox("손질 쉬운 스타일 원해요 (✔️)")

if st.button("✨ 헤어스타일 추천 받기"):
    g = None if gender == "무관" else gender
    l = None if length == "무관" else length
    pc = None if personal_color == "무관" else personal_color
    results = recommend(face_shape, g, l, low_maint, pc)
    
    st.subheader("추천 헤어스타일 Top 5")
    for i, r in enumerate(results, 1):
        st.markdown(f"**{i}. {r['name']}**")
        st.write(f"태그: {', '.join(r['tags'])}")
        st.write(f"손질 난이도: {r['maintenance']}")
        st.write(f"추천 퍼스널컬러: {', '.join(r.get('color_fit', []))}")
        st.info(r['notes'])



