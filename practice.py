# - grammar practice
# - spelling practice
# - reading practice

from gpt_check import *
from text.text_retrieving import *

import json

# BASIC FUNCTIONS FOR PRACTICE
# json is returned, it's predictable
def generate_text_for_reading():
    text = generate_paragraph()
    text_with_questions = generate_questions(text, 5)
    questions_in_json = json.loads(text_with_questions)
    return [text, questions_in_json]
# a list with two texts is returned: original and with mistakes
def generate_text_for_spelling():
    text = generate_paragraph()
    text_with_typos = generate_typos(text)
    return [text, text_with_typos]
# improvements of the function:
# - not to change the beginning, so that a user understands the main tense of the story
def generate_text_for_grammar_checking():
    text = generate_paragraph()
    text_with_tenses_check = generate_verb_forms_checks(text)
    return [text, text_with_tenses_check]


# NEXT FUNCTIONS FOR PRACTICE
def generate_text_for_articles_checking():
    return
# FUNCTIONS FOR VISUAL PRACTICE

# это вроде как реально сделать
# как отправить гпт4 изображение? вроде же как можно
#
#
#
# хотя бы заготовку!!!
def check_picture_description():
    # - load a picture
    # - give a correct or incorrect description
    return

