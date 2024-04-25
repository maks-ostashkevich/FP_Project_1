def substitute_word_in_sentence_with_gap(sentence, word, translation):
    modified_sentence = sentence.replace(word, f"____ ({translation})")

    return modified_sentence

