import streamlit as st
import random

# 영화 + 줄거리 + 포스터 데이터
movies = {
    "기생충": {
        "desc": "가난한 가족과 부유한 가족의 기묘한 만남으로 시작되는 블랙코미디.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/0/0b/Parasite_%282019_film%29.png"
    },
    "오징어 게임": {
        "desc": "빚더미에 오른 사람들이 목숨 건 게임에 참가하게 되는 이야기.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/2/2e/Squid_Game_poster.jpg"
    },
    "킹덤": {
        "desc": "죽은 자들이 되살아나는 전염병 속, 왕세자의 사투.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/4/45/Kingdom_poster.jpg"
    },
    "Stranger Things": {
        "desc": "1980년대 인디애나에서 벌어지는 초자연적 사건과 아이들의 모험.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/f/f7/Stranger_Things_season_4.jpg"
    },
    "Money Heist": {
        "desc": "천재 교수와 도둑들이 벌이는 대규모 은행 강도 작전.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/0/03/Money_Heist.jpg"
    },
    "Inception": {
        "desc": "꿈속에서 또 다른 꿈으로 들어가는 특수 요원들의 이야기.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/7/7e/Inception_ver3.jpg"
    },
    "Interstellar": {
        "desc": "인류 생존을 위해 우주로 떠나는 아버지와 과학자들.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"
    },
    "Coco": {
        "desc": "죽은 자들의 나라에서 가족의 의미를 찾아가는 소년의 모험.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/9/9f/Coco_%282017_film%29_poster.jpg"
    },
    "Moana": {
        "desc": "바다의 부름을 받은 소녀 모아나의 항해와 성장 이야기.",
        "poster": "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg"
    }
}

# 간식 데이터
snacks = [
    "팝콘 🍿", "치킨 🍗", "피자 🍕", "라면 🍜", "아이스크림 🍨",
    "감자칩 🥔", "떡볶이 🌶️", "쿠키 🍪", "맥주 🍺", "콜라 🥤",
    "초콜릿 🍫", "샌드위치 🥪", "김밥 🍙"
]

st.title("🎬 랜덤 영화 & 간식 추천기")

if st.button("추천 받기 🎲"):
    movie = random.choice(list(movies.keys()))
    snack = random.choice(snacks)
    info = movies[movie]

    st.image(info["poster"], width=300)
    st.subheader(f"🍿 영화: {movie}")
    st.write(f"**줄거리:** {info['desc']}")
    st.subheader(f"🥤 간식: {snack}")



