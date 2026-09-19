from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os 

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

model = init_chat_model(
    "gpt-5.5",
    # Kwargs passed to the model:
    temperature=0.7,
    timeout=120,
    max_tokens=1000,
    max_retries=10,  # Default; increase for unreliable networks
    api_key=api_key,
)

# response = model.invoke('안녕하세요')

# print(response)
# print("-"* 20,'\n', response.content)


prompt = ChatPromptTemplate.from_messages(
    [
        ('system', '당신은 친절하고 유용한 AI 어시스턴트 입니다.'),
        ('user', "{input}" )
    ]
)

input = "가을에 대한 시를 만들어줘"
chain = prompt | model 

chain_response = chain.invoke({"input" : input})

print(chain_response)
print("##"* 30,'\n', chain_response.content)


# 문자열 출력 파서 선언
output_parser = StrOutputParser()

# llm 구성에 위 문자열 파서 추가
chain_prompt = prompt | model | output_parser
chain_output_response = chain_prompt.invoke({"input": input})


# print(chain_output_response)
print("##"* 30,'\n', chain_output_response)
