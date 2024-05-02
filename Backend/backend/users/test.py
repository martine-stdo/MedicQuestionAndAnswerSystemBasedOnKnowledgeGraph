import os
os.environ["OPENAI_API_KEY"] = "sk-hK3PPvt64931nJJA1cD77f0d27Cd4b18B1C069F8DcE0De80"

os.environ["OPENAI_BASE_URL"] = "https://gtapi.xiaoerchaoren.com:8932/v1"

from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(

  model="gpt-3.5-turbo",

  messages=[

    {"role": "system", "content": "You are a helpful assistant."},

    {"role": "user", "content": "Hello!"}

  ]

)

print(completion)