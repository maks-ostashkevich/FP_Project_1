import text.text_retrieving
from text.text_retrieving import generate_paragraph
from gpt_check import *
from practice import *
from lesson_genering import *

# print(generate_sentence_with_word('crush', 'verb'))
# print(get_UA_translation_of_word('crush', 'adjective'))

# sentence = generate_sentence_with_word('crush', 'adjective')

# sentence = generate_sentence_with_words_list(['empathy', 'crush', 'honey'], ['noun', 'verb', 'noun'])

# print(sentence)

# json_words_A1 = generate_words_for_level('A1')

# result = generate_similar_word('impossible')
# print(result)

# result = exercise_for_gap_filling(A1_words_json["Tourism"][15])
# print(result)

# result = check_sentence_translation('A bird is flying', 'Птах літає')
# print(result)

result = generate_lesson(["home", "family", "friends"])
print(result)

"""
check1 = y['Emotions and Feelings']
check2 = y['Nature and Environment']
check3 = y['Science and Technology']
check4 = y['Business']
check5 = y['Other']


counter = 0
for i in check1:
    print(i)
    if not list_of_level_words_B2.find(i):
        counter += 1
for i in check2:
    print(i)
    if not list_of_level_words_B2.find(i):
        counter += 1
for i in check3:
    print(i)
    if not list_of_level_words_B2.find(i):
        counter += 1
for i in check4:
    print(i)
    if not list_of_level_words_B2.find(i):
        counter += 1
for i in check5:
    print(i)
    if not list_of_level_words_B2.find(i):
        counter += 1

print(counter)

"""

