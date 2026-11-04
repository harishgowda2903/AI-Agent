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

while True:

    #user prompt
    user_prompt = input("User: ")

    if user_prompt.lower() in ["exit", "quit"]:
        print("Exiting...")
        break


    #send a request to the API
    response = client.chat.completions.create(model = os.getenv("MODEL"),
                                            messages = [{"role": "user",
                                                        "content": user_prompt}])

    #display the response
    print("AI: " + response.choices[0].message.content)


