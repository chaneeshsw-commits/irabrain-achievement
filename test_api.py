from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Hello, IRABrain!"}
    ]
)

print(response.content[0].text)