# streamlit run app.py
import streamlit as st

# ===================== 데이터 =====================
COLOR_PALETTES = {
    "봄웜": [{"name": "라이트 브라운", "hex": "#C8A165"}, {"name": "골드 브론즈", "hex": "#D4A373"}, {"name": "꿀카라멜", "hex": "#E6B980"}],
    "여름쿨": [{"name": "애쉬 브라운", "hex": "#8B7C6E"}, {"name": "소프트 블랙", "hex": "#2F2F2F"}, {"name": "로즈 브라운", "hex": "#A97474"}],
    "가을웜": [{"name": "다크 초콜릿 브라운", "hex": "#4B2E2E"}, {"name": "카퍼 레드", "hex": "#B34729"}, {"name": "올리브 브라운", "hex": "#6B4C3B"}],
    "겨울쿨": [{"name": "블루 블랙", "hex": "#101820"}, {"name": "딥 와인", "hex": "#5C1A33"}, {"name": "애쉬 블론드", "hex": "#D8CFC4"}],
}

FACE_ALIASES = {
    "계란형": "oval", "긴얼굴": "long", "둥근형": "round", "각진형": "square",
    "하트형": "heart", "다이아": "diamond", "삼각형": "triangle"
}

HAIR_RULES = [
    {"name": "텍스처 픽시 크롭", "style_desc": "윗머리 볼륨 살린 숏컷", "tags": ["숏", "픽시", "텍스처"], "color_fit": ["겨울쿨", "여름쿨"], "maintenance": "하"},
    {"name": "롱 레이어드 웨이브 + 사이드 파트", "style_desc": "긴 웨이브, 부드러운 얼굴선", "tags": ["롱", "레이어드", "웨이브"], "color_fit": ["봄웜", "가을웜"], "maintenance": "중"},
    {"name": "턱선 길이의 블런트 보브", "style_desc": "모던하고 깔끔한 단발", "tags": ["숏", "보브", "스트레이트"], "color_fit": ["여름쿨", "겨울쿨"], "maintenance": "중"},
    {"name": "미디엄 커튼뱅 + C컬", "style_desc": "C컬과 커튼뱅으로 얼굴 감싸기", "tags": ["미디엄", "앞머리", "C컬"], "color_fit": ["봄웜", "여름쿨"], "maintenance": "하"},
    {"name": "센터 파트 스트레이트 롱", "style_desc": "시크한 긴 생머리", "tags": ["롱", "스트레이트"], "color_fit": ["겨울쿨"], "maintenance": "하"},
]

# ===================== 정규화 =====================
def normalize_face(face_shape: str) -> str:
    return FACE_ALIASES.get(face_shape, face_shape.lower())

# ===================== 추천 필터 =====================
def filter_styles(face_shape, gender, length, bang, personal_color, top_k=5):
    filtered = []
    for s in HAIR_RULES:
        # 길이 체크
        if length != "무관" and length not in s["tags"]:
            continue
        # 앞머리 체크
        if bang == "있음" and "앞머리" not in s["tags"]:
            continue
        if bang == "없음" and "앞머리" in s["tags"]:
            continue
        # 퍼스널컬러 체크
        if personal_color != "무관" and personal_color not in s.get("color_fit", []):
            continue
        filtered.append(s)
    return filtered[:top_k]

# ===================== Streamlit UI =====================
st.title("💇‍♂️ 나에게 꼭 맞는 헤어스타일, 얼굴형·컬러·앞머리까지 완벽 추천")

face_shape = st.selectbox("👉 얼굴형", list(FACE_ALIASES.keys()))
gender = st.selectbox("👉 성별", ["무관", "남성", "여성"])
length = st.selectbox("👉 원하는 길이", ["무관", "숏", "미디엄", "롱"])
bang = st.selectbox("👉 앞머리 여부", ["무관", "있음", "없음"])
personal_color = st.selectbox("👉 퍼스널컬러", ["무관", "봄웜", "여름쿨", "가을웜", "겨울쿨"])

if st.button("✨ 추천 받기"):
    results = filter_styles(face_shape, gender, length, bang, personal_color)
    
    if not results:
        st.warning("조건에 맞는 스타일이 없습니다. 옵션을 조정해보세요.")
    else:
        st.subheader("추천 헤어스타일")
        for i, r in enumerate(results, 1):
            with st.expander(f"{i}. {r['name']}"):
                st.write(f"**스타일 설명:** {r['style_desc']}")
                st.write(f"**태그:** {', '.join(r['tags'])}")
                if r.get("color_fit"):
                    st.write(f"**추천 퍼스널컬러:** {', '.join(r['color_fit'])}")
                st.write(f"**손질 난이도:** {r['maintenance']}")
        
        # 퍼스널컬러 팔레트
        if personal_color != "무관" and personal_color in COLOR_PALETTES:
            st.subheader(f"🎨 {personal_color}에게 어울리는 염색 컬러 팔레트")
            cols = st.columns(len(COLOR_PALETTES[personal_color]))
            for idx, c in enumerate(COLOR_PALETTES[personal_color]):
                with cols[idx]:
                    st.markdown(
                        f"<div style='background-color:{c['hex']}; width:100px; height:100px; border-radius:12px; border:1px solid rgba(0,0,0,0.08)'></div>",
                        unsafe_allow_html=True
                    )
                    st.caption(f"{c['name']} ({c['hex']})")





