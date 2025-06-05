import streamlit as st

# 🎨 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천 🎯",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="auto",
)

# 💅 커스텀 스타일 적용
st.markdown("""
    <style>
        body {
            background-color: #f8f8ff;
        }
        .job-card {
            background-color: #ffffff;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 10px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
            transition: 0.3s;
        }
        .job-card:hover {
            transform: scale(1.02);
            background-color: #f0f9ff;
        }
        .footer {
            font-size: 0.9rem;
            color: #aaa;
            text-align: center;
            margin-top: 3rem;
        }
    </style>
""", unsafe_allow_html=True)

# 🌟 헤더 영역
st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b; font-size: 3rem;'>✨ MBTI로 알아보는 찰떡 직업 추천 ✨</h1>
    <h4 style='text-align: center; color: #4bff9f;'>당신의 성격에 딱 맞는 직업은 무엇일까요? 💼</h4>
""", unsafe_allow_html=True)

# 🎭 MBTI 선택
st.markdown("## 📌 당신의 MBTI를 선택해주세요:")
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]
mbti = st.selectbox("👉 MBTI 선택", mbti_list)

# 🔮 MBTI 직업 추천 데이터
mbti_jobs = {
    "ISTJ": ["👨‍💼 회계사", "📊 관리자", "💼 공무원"],
    "ISFJ": ["👩‍⚕️ 간호사", "🏫 교사", "🧑‍🏫 상담사"],
    "INFJ": ["🧘‍♂️ 심리학자", "📖 작가", "🌍 NGO 활동가"],
    "INTJ": ["🧠 전략가", "🧪 연구원", "💻 데이터 분석가"],
    "ISTP": ["🔧 엔지니어", "🛠️ 기술자", "🚗 정비사"],
    "ISFP": ["🎨 디자이너", "📸 사진작가", "🎭 예술가"],
    "INFP": ["📝 작가", "🎼 음악가", "🎬 영화 감독"],
    "INTP": ["🧑‍🔬 과학자", "📐 수학자", "🖥️ 개발자"],
    "ESTP": ["💼 영업 사원", "🎤 이벤트 기획자", "🏃 트레이너"],
    "ESFP": ["🎤 연예인", "🎉 행사 기획자", "🕺 댄서"],
    "ENFP": ["🌈 광고 기획자", "🎙️ 방송인", "✈️ 여행 작가"],
    "ENTP": ["🧑‍💼 창업가", "🎯 마케팅 전문가", "🗣️ 연설가"],
    "ESTJ": ["📋 프로젝트 매니저", "🏢 경영자", "🛡️ 군인"],
    "ESFJ": ["👩‍🏫 교사", "👨‍🍳 요리사", "👩‍👩‍👧‍👦 사회복지사"],
    "ENFJ": ["🎓 교육자", "📢 퍼실리테이터", "💞 커뮤니티 매니저"],
    "ENTJ": ["💼 CEO", "📈 투자 전문가", "🧑‍💻 IT 전략가"],
}

# 🎁 결과 출력
if mbti:
    st.markdown(f"""
        <div style='text-align: center; margin-top:2rem;'>
            <h2 style='color:#6c5ce7;'>🧬 <span style="background-color: #ffeaa7; padding: 5px 10px; border-radius: 8px;">{mbti}</span> 유형에게 추천하는 직업 🌟</h2>
        </div>
    """, unsafe_allow_html=True)

    for job in mbti_jobs[mbti]:
        st.markdown(f"<div class='job-card'>👉 {job}</div>", unsafe_allow_html=True)

# 🎉 하단 메세지
st.markdown("""
    <hr>
    <div class='footer'>
        🚀 오늘도 멋진 진로 탐색 하세요!<br>
        Made with ❤️ using <b>Streamlit</b> <br>
        🔗 <a href="https://github.com/yourusername" target="_blank">GitHub</a> | <a href="https://yourportfolio.com" target="_blank">Portfolio</a>
    </div>
""", unsafe_allow_html=True)
