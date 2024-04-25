from nltk.tokenize import word_tokenize
is_verb = lambda pos: pos[:2] == 'VB'
str_ = 'Horses eat carrots'
text = word_tokenize(str_)
vbs = [word for (word, pos) in nltk.pos_tag(text) if is_verb(pos)]