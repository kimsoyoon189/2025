# dongmyeong_cafe_play.py
import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="동명동 데이트 & 놀거리 추천", page_icon="🌸", layout="centered")

# 헤더
st.markdown(
    """
    <h1 style='text-align:center; color:#ff99aa;'>🌸 동명동 카페 & 놀거리 추천 🌸</h1>
    <p style='text-align:center; color:gray; font-size:16px;'>
    예쁜 카페에서 달콤한 시간을 보내고, 근처에서 즐길 거리까지!<br>
    오늘 하루를 완벽하게 만들어 드릴게요 💖
    </p>
    """,
    unsafe_allow_html=True
)

# 카페 데이터
cafes = [
    {"name": "커피 로드뷰", "location": "광주 동구 동계천로 132", "features": "크림라떼 시그니처, 우드톤 인테리어", "image": "https://example.com/coffee_roadview.jpg"},
    {"name": "레브", "location": "광주 동구 동명로14번길 29", "features": "모던 브런치 카페, 데이트 & 모임 적합", "image": "https://example.com/reve.jpg"},
    {"name": "홉커피", "location": "광주 동구 동계로 1", "features": "푸딩 케이크 전문, 피스타치오 체리 푸딩 인기", "image": "https://example.com/hopcoffee.jpg"},
    {"name": "디엑스커피", "location": "광주 동구 동계천로95번길 3", "features": "붉은 벽돌 외관, 반려동물 동반 가능", "image": "https://example.com/dxcoffee.jpg"},
    {"name": "카페 온화", "location": "광주 동구 동계천로 151-31", "features": "한옥 스타일, 수플레 팬케이크", "image": "https://example.com/onhwa.jpg"},
    {"name": "베러그릭", "location": "광주 동구 동계천로 163-6", "features": "그릭요거트 전문, 아기자기한 정원", "image": "https://example.com/bettergreek.jpg"},
    {"name": "카페 호시정", "location": "광주 동구 동계천로 137-9", "features": "주택 개조, 정원과 한옥 분위기", "image": "https://example.com/hoshijeong.jpg"},
    {"name": "블루웨일", "location": "광주 동구 동계천로 169-3", "features": "실버 밀크티 & 수플레 팬케이크", "image": "https://example.com/bluewhale.jpg"},
]

# 놀거리 데이터
plays = [
    {"name": "충장로 거리 산책", "desc": "카페 나와서 바로 걷기 좋은 로드, 쇼핑과 구경까지 한 번에!", "image": "https://example.com/chungjang.jpg"},
    {"name": "예술의 거리 탐방", "desc": "작은 갤러리와 공방이 모여 있는 감성 가득한 거리", "image": "https://example.com/artstreet.jpg"},
    {"name": "양림동 역사문화마을", "desc": "동명동에서 도보로 가까운, 한옥과 역사적 건물들 산책", "image": "https://example.com/yangrim.jpg"},
    {"name": "오월 18기념공원", "desc": "조용히 산책하며 광주의 역사와 의미를 되새길 수 있는 곳", "image": "https://example.com/may18park.jpg"},
    {"name": "전일빌딩245 전망대", "desc": "광주 시내를 한눈에 내려다보는 뷰 포인트", "image": "https://example.com/jeonil245.jpg"},
]

# 추천 버튼
if st.button("💌 오늘의 카페 + 놀거리 추천 💌"):
    cafe = random.choice(cafes)
    play = random.choice(plays)

    # 카페 추천
    st.markdown(
        f"<h2 style='color:#ff85a2;'>☕ 오늘은 <b>{cafe['name']}</b>에서 시작해볼까요?</h2>",
        unsafe_allow_html=True
    )
    st.image(cafe["image"], use_column_width=True)
    st.write(f"📍 **위치:** {cafe['location']}")
    st.write(f"✨ **특징:** {cafe['features']}")

    st.markdown("<hr>", unsafe_allow_html=True)

    # 놀거리 추천
    st.markdown(
        f"<h2 style='color:#85c1ff;'>🎈 그리고 이렇게 즐겨보세요: <b>{play['name']}</b></h2>",
        unsafe_allow_html=True
    )
    st.image(play["image"], use_column_width=True)
    st.write(f"💡 {play['desc']}")
    st.markdown("<p style='color:gray;'>오늘 하루가 예쁘게 기억에 남을 거예요 🌷</p>", unsafe_allow_html=True)

# 전체 카페 & 놀거리 목록
with st.expander("📜 전체 카페 목록 보기"):
    for cafe in cafes:
        st.write(f"**{cafe['name']}** — {cafe['features']} ({cafe['location']})")

with st.expander("🎡 전체 놀거리 목록 보기"):
    for play in plays:
        st.write(f"**{play['name']}** — {play['desc']}")
