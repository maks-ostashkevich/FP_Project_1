from gpt_check import *
from practice import *
from text.text_retrieving import *

import random

A1_words_json = {
    "Home, family and friends": ["home", "family", "friends", "mother", "father", "sister", "brother", "house", "room", "kitchen", "bathroom", "living", "pet", "garden", "meal", "dinner", "party", "birthday", "holiday", "welcome"],
    "Work": ["work", "job", "office", "boss", "colleague", "meeting", "salary", "project", "team", "break", "task", "email", "report", "deadline", "promotion", "career", "interview", "full-time", "part-time", "shift"],
    "Tourism": ["tourism", "travel", "trip", "holiday", "hotel", "map", "tourist", "guide", "destination", "sightseeing", "attraction", "beach", "museum", "monument", "city", "country", "vacation", "backpack", "camping", "souvenir"],
    "Cafe and restaurant": ["cafe", "restaurant", "menu", "order", "waiter", "table", "dish", "meal", "lunch", "dinner", "breakfast", "snack", "drink", "bill", "tip", "reserve", "chef", "taste", "service", "food"],
    "Public places": ["public", "place", "park", "museum", "library", "theater", "cinema", "station", "hospital", "shop", "market", "school", "university", "bank", "post", "office", "city", "square", "street", "traffic"]
}


def exercise_for_gap_filling(word):
    sentence = generate_sentence_with_words_list([word])
    # possible cycle to generate sentence with one such word
    sentence_with_gap = sentence.replace(word, '(?)')
    similar_word = generate_similar_word(word)
    return [sentence, sentence_with_gap, [word, similar_word]]


def generate_sentence(word):
    sentence = generate_sentence_with_words_list([word])
    return sentence


def check_translation(sentence, user_translation):
    translation_result = check_sentence_translation(sentence, user_translation)
    return translation_result


# 3 words
def generate_lesson(words):
    print("Present Simple is ...")
    lesson_list = [exercise_for_gap_filling(words[0]), exercise_for_gap_filling(words[1]), generate_sentence(words[2]),
                   generate_text_for_reading()]
    return lesson_list