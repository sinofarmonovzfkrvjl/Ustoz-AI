from openai import OpenAI

def BilimdonAI(prompt: str):
    """Bu AI o'zbekiston maktablaridagi deyarli barcha fanlarni biladi va shu fanlarga oid mavzular bo'yicha javob beradi"""
    API_TOKEN = "9961b821af1943f791354e7fe74c8130"

    client = OpenAI(
        base_url="https://api.netmind.ai/inference-api/openai/v1",
        api_key=API_TOKEN,
    )

    messages = [
        {"role": "system", "content": "only speaks in uzbek language and is a 15-years of experienced uzbek teacher who knows whole uzbekistan's school's subjects including math and answers in uzbek language completely"},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="google/gemma-3-27b-it",
        messages=messages,
        max_tokens=1000,  # Completion tokens
    )

    return response.choices[0].message.content

# BilimdonAI("qadimgi turkiylar haqida qisqacha malumot")
