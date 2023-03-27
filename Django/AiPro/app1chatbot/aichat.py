'''
# chatbot/utils.py
import openai
openai.api_key = "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"

def generate_response(message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
'''