from decouple import config
from openai import OpenAI


openai_api_key=config("OPENAI_API_KEY")
MODEL="gpt-3.5-turbo"
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "너는 고객의 만족도를 분석하는 로봇이야. 고객의 응답내용을 토대로 만족 또는 불만족을 구분해줘.JSON"},
        {"role": "user", "content": "오늘 구매한 컴퓨터는 소음이 심하고 가격에 비해서 성능이 별로야"}
    ]
)
print(response.choices[0].message.content)
pass