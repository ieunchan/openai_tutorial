from PIL import Image
from decouple import config
from openai import OpenAI
import requests


openai_api_key=config("OPENAI_API_KEY")
MODEL="dall-e-3"

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model=MODEL,
    prompt="",
    size="1024x1024",
    quality="standard",
    n=1,
)
image_url = response.data[0].url

# 저장 파일 이름 설정
filename = "image.jpg"
response = requests.get(image_url)
with open(filename,'wb') as f:
    f.write(response.content)
Image.open(filename)
