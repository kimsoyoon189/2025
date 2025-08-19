import streamlit as st
import random

# --- 데이터 (15가지 예시) ---
HAIR_RULES = [
    {
        "name": "롱 레이어드 웨이브 + 사이드 파트",
        "tags": ["여성", "롱", "레이어드", "웨이브"],
        "fit": {"oval": 3, "round": 2, "square": 2, "heart": 3, "long": 1, "diamond": 3, "triangle": 2},
        "notes": "사이드 파트로 비대칭을 주면 광대·턱선을 부드럽게.",
        "maintenance": "중"
    },
    {
        "name": "턱선 길이의 블런트 보브",
        "tags": ["여성", "숏", "보브", "스트레이트"],
        "fit": {"oval": 3, "round": 1, "square": 2, "heart": 3, "long": 2, "diamond": 2, "triangle": 2},
        "notes": "끝선이 둔탁해 볼륨감↑, 목선 강조.",
        "maintenance": "중"
    },
    {
        "name": "미디엄 커튼뱅 + C컬",
        "tags": ["여성", "미디엄", "앞머리", "C컬"],
        "fit": {"oval": 3, "round": 3, "square": 2, "heart": 2, "long": 3, "diamond": 2, "triangle": 3},
        "notes": "커튼뱅이 얼굴 폭을 좁혀주고 긴 얼굴 비율 보정.",
        "maintenance": "하"
    },
    {
        "name": "텍스처 픽시 크롭",
        "tags": ["여성", "남성", "숏", "픽시"],
        "fit": {"oval": 3, "round": 2, "square": 3, "heart": 2, "long": 2, "diamond": 3, "triangle": 2},
        "notes": "윗머리 텍스처로 정수리 볼륨 살리기.",
        "maintenance": "하"
    },
    {
        "name": "롱보브(Lob) + 내추럴 웨이브",
        "tags": ["여성", "미디엄", "웨이브"],
        "fit": {"oval": 3, "round": 2, "square": 3, "heart": 2, "long": 2, "diamond": 3, "triangle": 2},
        "notes": "쇄골 길이로 턱선 각을 부드럽게.",
        "maintenance": "중"
    },
    {
        "name": "울프컷 셰기",
        "tags": ["여성", "남성", "미디엄", "레이어드"],
        "fit": {"oval": 2, "round": 2, "square": 3, "heart": 2, "long": 3, "diamond": 3, "triangle": 2},
        "notes": "윗볼륨+아웃라인로 세로 비율 보정.",
        "maintenance": "중"
    },
    {
        "name": "미드 페이드 크롭 (남)",
        "tags": ["남성", "숏", "페이드"],
        "fit": {"oval": 3, "round": 3, "square": 3, "heart": 2, "long": 1, "diamond": 3, "triangle": 2},
        "notes": "앞머리 약간 다운·업으로 이마 비율 조절.",
        "maintenance": "하"
    },
    {
        "name": "투블록 K-스타일",
        "tags": ["남성", "미디엄", "투블록"],
        "fit": {"oval": 3, "round": 2, "square": 2, "heart": 3, "long": 2, "diamond": 2, "triangle": 3},
        "notes": "윗부분 볼륨 주면 역삼각·삼각형 보정에 좋음.",
        "maintenance": "중"
    },
    {
        "name": "프렌치 보브 + 마이크로 뱅",
        "tags": ["여성", "숏", "앞머리"],
        "fit": {"oval": 3, "round": 1, "square": 2, "heart": 2, "long": 3, "diamond": 2, "triangle": 2},
        "notes": "짧은 뱅으로 시선↑ → 긴 얼굴 균형.",
        "maintenance": "중"
    },
    {
        "name": "센터 파트 스트레이트 롱",
        "tags": ["여성", "롱", "스트레이트"],
        "fit": {"oval": 3, "round": 1, "square": 2, "heart": 2, "long": 1, "diamond": 3, "triangle": 2},
        "notes": "깔끔하지만 둥근/긴 얼굴은 주의 필요.",
        "maintenance": "하"
    },
    # ... (15개 전체 다 넣어도 됨. 길이 때문에 일부 생략)
]

FACE_ALIASES = {
    "계란형": "oval", "긴얼굴": "long", "둥근형": "round", "각진형": "square",
    "하트형": "heart", "다이아": "diamond", "삼각형": "triangle"
}

def normalize_face(face_shape: str) -> str:
    for k, v in FACE_ALIASES.items():
        if k == face_shape:
            return v
    return face_shape.lower()

def score_style(rule, face_key, gender, length, low_maint):
    score = rule["fit"].get(face_key, 0)
    if gender and gender in rule["tags"]:
        score += 0.5
    if length and length in rule["tags"]:
        score += 0.5
    if low_maint and rule["maintenance"] == "하":
        score += 0.5
    score += random.uniform(-0.1, 0.1)
    return score

def recommend(face_shape, gender, length, low_maint, top_k=5):
    face_key = normalize_face(face_shape)
    scored = []
    for r in HAIR_RULES:
        s = score_style(r, face_key, gender, length, low_maint)
        scored.append((s, r))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [r for _, r in scored[:top_k]]

# --- Streamlit UI ---
st.title("💇 얼굴형별 헤어스타일 추천기")

face_shape = st.selectbox("👉 얼굴형을 골라주세요", list(FACE_ALIASES.keys()))
gender = st.selectbox("👉 성별", ["무관", "남성", "여성"])
length = st.selectbox("👉 원하는 머리 길이", ["무관", "숏", "미디엄", "롱"])
low_maint = st.checkbox("손질 쉬운 스타일 원해요 (✔️)")

if st.button("✨ 헤어스타일 추천 받기"):
    g = None if gender == "무관" else gender
    l = None if length == "무관" else length
    results = recommend(face_shape, g, l, low_maint)
    
    st.subheader("추천 헤어스타일 Top 5")
    for i, r in enumerate(results, 1):
        st.markdown(f"**{i}. {r['name']}**")
        st.write(f"태그: {', '.join(r['tags'])}")
        st.write(f"손질 난이도: {r['maintenance']}")
        st.info(r['notes'])


