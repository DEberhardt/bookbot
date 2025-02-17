
def main():
    path_to_file: str = 'books/frankenstein.txt'
    with open(path_to_file) as f:
        file_contents = f.read()

    words = file_contents.split()
    count = len(words)
    print (count)

# main()

def readText():
    path_to_file: str = 'books/frankenstein.txt'
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def countLetters(text: str) -> dict:
    text = text.lower()  # Convert text to lowercase to handle case insensitivity

    letter_dict = {}

    for char in text:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1

    return letter_dict

text = readText()
# print(countLetters(text))
letters_count = countLetters(text)

def Report(letters_count: dict):
    # Sort the dictionary by count in descending order
    sorted_letters_count = sorted(letters_count.items(), key=lambda item: item[1], reverse=True)

    for letter, count in sorted_letters_count:
        if letter.isalpha():
            print(f" The '{letter}' charachter was found {count} times")

Report(letters_count)
