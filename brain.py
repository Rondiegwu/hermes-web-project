import os
from groq import Groq

def get_automated_tip():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a natural health expert. Write a short, engaging 2-sentence health tip about oral hygiene or natural ingredients like bentonite clay. No hashtags."
            },
            {"role": "user", "content": "Give me a unique health tip for today."}
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content
