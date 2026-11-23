from openai import OpenAI
from dotenv import load_dotenv
import os
import re

TOOL_NAMES = [
    "days_until_new_year",
    "get_current_time",
    "roll_dice",
    "generate_password",
]


def clean_reply(text):
    """Remove Qwen3's <think>...</think> block (it appears even when empty)."""

    return re.sub(r"<think>.*?</think>", "", text or "", flags=re.DOTALL).strip()

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def choose_tool(user_request):

    planner_prompt = f"""
You are an AI planner.

Available tools:

1. get_current_time
   Use when the user asks for the current date or time.

2. roll_dice
   Use when the user asks to roll a dice.

3. generate_password
   Use when the user wants a secure password.

4. days_until_new_year
   Use when the user asks how many days are left until the new year.

If no tool is required, return:

none

Return ONLY the tool name.

User Request:

{user_request}

/no_think
"""

    response = client.chat.completions.create(

        model=os.getenv("MODEL"),

        messages=[
            {
                "role":"system",
                "content":"You are an AI planner."
            },
            {
                "role":"user",
                "content":planner_prompt
            }
        ],

        max_tokens=50
    )

    reply = clean_reply(response.choices[0].message.content)

    # The model sometimes adds extra words, so look for a known tool name
    for name in TOOL_NAMES:
        if name in reply:
            return name

    return "none"


