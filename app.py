import streamlit as st
import google.generativeai as genai

# 제목과 설명
st.title("🎬 누아르 영화 씬 메이커")
st.info("팀원 전용 테스트 페이지입니다.")

# API 키 설정 (Streamlit 설정에서 입력할 예정)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    # 입력창
    user_input = st.text_area("장면이나 대사를 입력하세요:", "어두운 골목, 비에 젖은 코트를 입은 사내가 서 있다.")

    if st.button("AI 분석 시작"):
        with st.spinner('분석 중...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(user_input + " \n\n 한국형 누아르 영화풍으로 대사와 연출 가이드를 상세히 써줘.")
            st.markdown("---")
            st.subheader("📝 결과물")
            st.write(response.text)
else:
    st.error("API Key를 설정해주세요!")
