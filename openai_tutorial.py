from decouple import config
from openai import OpenAI

openai_api_key=config("OPENAI_API_KEY")
MODEL="gpt-3.5-turbo"
client = OpenAI(api_key=openai_api_key)
response = client.chat.completions.create(
    model = MODEL,
    messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
    ]
)
print(response.choices[0].message.content)
pass