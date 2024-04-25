import requests


def generate_questions(paragraph, num_of_questions):
    openai_api_key = 'sk-proj-JIe8e7A1LOJLbmINy5PGT3BlbkFJ2KTNyW5GapiyAfcoN0k7'# put yout api key here

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"""Generate {num_of_questions} questions to this text with 3 options of answer and the only
                one should be correct:
                
                {paragraph}

                Print the questions in json format like this:
                {{"(Text of question #1)": [option1, option2, option3], "Text of question #2": [option1, option2, option3], ...}}"""
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    # как работать и что возвращать, если запрос прошел не успешно?
    # Check if the request was successful
    if response.status_code == 200:
        # print("Response from OpenAI:", response.json())
        # print('\n')
        # print(response.json()['choices'][0]['message']['content'])
        return response.json()['choices'][0]['message']['content']
    else:
        # print("Error:", response.status_code, response.text)
        return "Error"


# fine-tune the function
# make the descriptions of custom mistakes like two neighboring vowels, duplicated redundant symbols
def generate_typos(paragraph):
    openai_api_key = 'sk-proj-JIe8e7A1LOJLbmINy5PGT3BlbkFJ2KTNyW5GapiyAfcoN0k7'  # put yout api key here

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")
    url = "https://api.openai.com/v1/chat/completions"
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"""Make >5 typos in the paragraph:

                {paragraph}

                Print the altered paragraph.
                Don't print anything else."""
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    response = requests.post(url, headers=headers, json=data)

    # как работать и что возвращать, если запрос прошел не успешно?
    # Check if the request was successful
    if response.status_code == 200:
        # print("Response from OpenAI:", response.json())
        # print('\n')
        # print(response.json()['choices'][0]['message']['content'])
        return response.json()['choices'][0]['message']['content']
    else:
        # print("Error:", response.status_code, response.text)
        return "Error"


# сгенерировать с подсказками, правильный ли это глагол, то есть изменить промпт
def generate_verb_forms_checks(paragraph):
    openai_api_key = 'sk-proj-JIe8e7A1LOJLbmINy5PGT3BlbkFJ2KTNyW5GapiyAfcoN0k7'  # put yout api key here

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "model": "gpt-4-turbo-2024-04-09",  # "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"""Find in the below paragraph all the tense forms of verbs 
                and for each second of them
                put '____' instead of the tense form of a verb and then put the base form
                of the tense form verb in "()"-type braces. Like this: ____ (the base form of the verb).

                {paragraph}

                Print the altered paragraph.
                Don't print anything else."""
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    # как работать и что возвращать, если запрос прошел не успешно?
    # Check if the request was successful
    if response.status_code == 200:
        # print("Response from OpenAI:", response.json())
        # print('\n')
        # print(response.json()['choices'][0]['message']['content'])
        return response.json()['choices'][0]['message']['content']
    else:
        # print("Error:", response.status_code, response.text)
        return "Error"


def generate_sentence_in_particular_tense(tense):
    openai_api_key = 'sk-proj-JIe8e7A1LOJLbmINy5PGT3BlbkFJ2KTNyW5GapiyAfcoN0k7'  # put yout api key here

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"""Make a sentence with {tense} tense, where
                    the predicate tense form with all auxiliary verbs that make up the tense
                    will be ommited and the gap will be instead of it with the verb in "()" braces.
                    Use the concrete indicator of the tense so that user will understand
                    by it, how to change the verb.
                                         
                    Print the sentence.
                    Don't print anything else."""
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    # как работать и что возвращать, если запрос прошел не успешно?
    # Check if the request was successful
    if response.status_code == 200:
        # print("Response from OpenAI:", response.json())
        # print('\n')
        # print(response.json()['choices'][0]['message']['content'])
        return response.json()['choices'][0]['message']['content']
    else:
        # print("Error:", response.status_code, response.text)
        return "Error"


def get_list_of_Level_words(level, list_of_level_words):
    openai_api_key = 'sk-proj-JIe8e7A1LOJLbmINy5PGT3BlbkFJ2KTNyW5GapiyAfcoN0k7'  # put yout api key here

    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo-0125",  # "gpt-3.5-turbo"
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"""Here is the list of words - L1: 
                    {list_of_level_words}.
                    
                    There are categories: "Emotions and Feelings", "Nature and Environment",
                    "Science and Technology", "Business", "Other"
                    
                    For each word classify it according to one of these categories.
                    Do not transform words to lemmas or other new forms during your processing.
                    
                    List them in the initial order and put after a space their category, like this:
                    budget Business
                    bullet Other
                    ...
                    """
            }
        ]
    }
# breed disaster astronaut adaptation computer telescope
# attach business balance circulate commuter company dollar donate economy employment enterprise exchange
#    franchise import invoice
    response = requests.post(url, headers=headers, json=data)

    # как работать и что возвращать, если запрос прошел не успешно?
    # Check if the request was successful
    if response.status_code == 200:
        # print("Response from OpenAI:", response.json())
        # print('\n')
        # print(response.json()['choices'][0]['message']['content'])
        return response.json()['choices'][0]['message']['content']
    else:
        # print("Error:", response.status_code, response.text)
        return "Error"


# auxiliary functions:
# - inject a noun into the prompt in order for ChatGPT generate a new kind of sentences
#   we can inject nouns specifically for the same level

def generate_sentence_with_word(word, part_of_speech):
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
                "content": f"""Generate a sentence in English with {word} as {part_of_speech}.
                Print only the sentence, don't print anything else, don't print quotes
                 around the sentence."""
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"

def generate_similar_word(word):
    print(word)

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
                "content": f"""Generate a similar in letters but having completely different definition 
                word to word "{word}" in English.
                Print only the similar word, don't print anything else, don't print quotes
                 around the similar word."""
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"
def generate_similar_word_with_pos(word, part_of_speech):
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
                "content": f"""Generate a sentence in English with {word} as {part_of_speech}.
                Print only the sentence, don't print anything else, don't print quotes
                 around the sentence."""
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"


def generate_sentence_with_words_list_with_pos(words_list, pos_list):
    # print(word)
    # print(part_of_speech)
    words_with_pos = ", ".join(f"{word} as {pos}" for word, pos in zip(words_list, pos_list))

    print(words_with_pos)

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
                "content": f"""Generate a sentence in English with such words: {words_with_pos}.
                Print only the sentence, don't print anything else, don't print quotes
                around the sentence."""
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"

def generate_sentence_with_words_list(words_list):
    words_list_string = ", ".join(words_list)

    print(words_list_string)

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
                "content": f"""Generate a sentence in English with such words: {words_list_string}.
                Print only the sentence, don't print anything else, don't print quotes
                around the sentence."""
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"


def get_UA_translation_of_word(word, part_of_speech):
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
                "content": f"""
                    Print the most relevant translation of {word} as {part_of_speech} to Ukrainian,
                    don't print anything else, don't print any additional information or explanations.
                    """
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"

# DON'T RUN OFTEN
# НЕ ЗАПУСКАТИ ЧАСТО, ЇСТЬ ГРОШІ
def generate_words_for_level(level):
    openai_api_key = 'sk-proj-JIe8e7A1LOJLbmINy5PGT3BlbkFJ2KTNyW5GapiyAfcoN0k7'

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
                "content": f"""Generate 20 the most relevant English words for {level} level in such subjects:
                1. Home, family and friends.
                2. Work.
                3. Tourism.
                4. Cafe and restaurant.
                5. Public places.

                Return them strictly in such json format:
                {{"(Name of #1 subject)": [word1, ..., word20], "(Name of #2 subject)": [word1, ..., word20], ...}}
                
                Don't print anything else. Don't print any of your explanations or additional information.
                Print only and only the final json-object.
                """
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"

def check_sentence_translation(sentence, sentence_translation):
    openai_api_key = 'sk-proj-JIe8e7A1LOJLbmINy5PGT3BlbkFJ2KTNyW5GapiyAfcoN0k7'

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
                "content": f"""Print "yes", if there are cases when "{sentence_translation}" 
                                is possible to translate to "{sentence}" else return "no".
                                Don't print anything except "yes" or "no"."""
                # Don't print anything except "yes" or "no".
                # Explain your choice.
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error"