# разбить на абзацы - примитивный способ есть
# генерировать рандомные числа, чтобы получить рандомный текст
# 1) ген-им рандомное число, чтобы выбрать книгу
# 2) ген-им рандомное число, чтобы выбрать абзац
# 3) возвращаем этот абзац для работы
#
#

import os

import random


def count_files_in_folder(folder_path):
    # Get list of files in the folder
    files = os.listdir(folder_path)
    # Count the number of files
    num_files = len(files)
    return num_files


# Define the range
start_range = 1
end_range = count_files_in_folder('C:/Users/User/Downloads/English Books Library for test 1')

random_number = random.randint(start_range, end_range)

# print("Random number:", random_number)

def read_file_into_paragraphs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Split text into paragraphs based on empty lines
        paragraphs = text.split('\n\n')
        # Remove any leading or trailing whitespaces from paragraphs
        paragraphs = [paragraph.strip() for paragraph in paragraphs if paragraph.strip()]
    return paragraphs


def generate_paragraph():
    file_path = f'C:/Users/User/Downloads/English Books Library for test 1/{random_number}.txt'  # Replace 'your_file.txt' with the path to your UTF-8 encoded text file
    paragraphs = read_file_into_paragraphs(file_path)
    random_paragraph = random.randint(100, len(paragraphs) - 100)
    if len(paragraphs[random_paragraph]) < 175:
        return generate_paragraph()
    return paragraphs[random_paragraph]

# print(generate_paragraph())