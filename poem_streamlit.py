import streamlit as st 
import time 
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os 

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# st.title("This is a title")
st.title("_AI 시인_ :sunglasses:")
# st.title("Dashboard", icon=":material/dashboard:")

title = st.text_input("시의 주제를 입력하세요", "가을")
st.write("시의 주제 : ", title)

if st.button("시 작성"):
    # st.write("시 작성중")

    with st.spinner("시 작성중..."):
        time.sleep(5)
        # llm 생성
        model = init_chat_model(
            "gpt-5.5",
            # Kwargs passed to the model:
            temperature=0.7,
            timeout=120,
            max_tokens=1000,
            max_retries=10,  # Default; increase for unreliable networks
            api_key=api_key,
        )        
        # prompt
        prompt = ChatPromptTemplate.from_messages([
            ('system', '당신은 도움을 주는 어시스턴스 입니다.'),
            ('user', '{input2}')
        ])
        # outputParser + chain
        chain = prompt | model | StrOutputParser()
        # response 출력 + invoke
        response = chain.invoke({'input2' : title + " 에 대한 시를 작서해줘"})

        st.write(response)




