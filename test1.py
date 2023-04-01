import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


openai.api_key = open_file('openaiKey.txt')
print(openai.api_key)