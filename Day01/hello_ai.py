from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

#make sure the console can print emojis/unicode on Windows
sys.stdout.reconfigure(encoding="utf-8")

#load environment variables from .env file
load_dotenv()

#create a client instance
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

#send a request to the API
response = client.chat.completions.create(model = os.getenv("MODEL"),
                                          messages = [{"role": "user",
                                                       "content": "Hello, AI!"}])

#display the response
print(response.choices[0].message.content)
