import spacy

# Загрузка модели языка английского
nlp = spacy.load("en_core_web_sm")

# Текст с глаголами в разных временных формах
# text = "He walks to the store. She walked to the store yesterday. They will walk to the store tomorrow."

text = "She will have done some shopping."

# Обработка текста
doc = nlp(text)

# Извлечение полных временных форм глаголов
full_verb_forms = [token.text for token in doc if token.pos_ == "VERB"]

# Вывод результатов
print(full_verb_forms)
