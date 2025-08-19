오 지금 짜준 건 \*\*“상황 고르면 그 상황의 플레이리스트 보여주는 코드”\*\*였고,
말한 것처럼 진짜 **랜덤으로 뽑아주는 코드**는 아니야 🙂

랜덤 추천 버전은 이렇게 바꿔줄 수 있어 ⬇️

```python
import random

# 상황별 플레이리스트 (앞에 만든 거랑 동일)
playlists = {
    "아침에 일어날 때": [
        "볼빨간사춘기 – 여행",
        "DAY6 – 한 페이지가 될 수 있게",
        "HONNE – Day 1",
        "BIGBANG – We Like 2 Party",
        "Bruno Mars – Count on Me"
    ],
    "통학/출근길": [
        "아이유 – 팔레트",
        "DPR LIVE – Martini Blue",
        "AKMU – 리얼리티",
        "Khalid – Better",
        "BIGBANG – 뱅뱅뱅"
    ],
    "비 오는 날": [
        "검정치마 – Everything",
        "Sam Kim – Who Are You",
        "Billie Eilish – Ocean Eyes",
        "Heize – You, Clouds, Rain",
        "BIGBANG – If You"
    ],
    # ... (나머지 상황들도 위 코드처럼 계속 이어붙이면 됨!)
}

def random_playlist():
    # 랜덤 상황 하나 선택
    situation = random.choice(list(playlists.keys()))
    songs = playlists[situation]
    
    # 랜덤 노래 2~3곡 뽑기
    random_songs = random.sample(songs, k=min(3, len(songs)))
    
    print(f"\n🎲 랜덤 상황: {situation}")
    print("추천 곡들:")
    for song in random_songs:
        print("-", song)

# 실행
if __name__ == "__main__":
    random_playlist()


