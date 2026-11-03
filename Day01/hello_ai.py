from openai import OpenAI
from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv()

#create a client instance
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

#send a request to the API
response = client.chat.completions.create(model = os.getenv("MODEL"),
                                          messages = [{"role": "user",
                                                       "content": "Hello, AI!"}])

#display the response
print(response.choices[0].