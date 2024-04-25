import openai
import requests

def validate_sentence_with_word(sentence, word, part_of_speech):
    print(word)
    print(part_of_speech)
    openai_api_key = 'sk-proj-JIe8e7A1LOJLbmINy5PGT3BlbkFJ2KTNyW5GapiyAfcoN0k7'  # put yout api key here

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "model": "gpt-4-turbo-2024-04-09",  # "gpt-3.5-turbo"
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f""" Check if {word} in {sentence} is {part_of_speech}.
                                Return only "Yes" or "No".
                """
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"