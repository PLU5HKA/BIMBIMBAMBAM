import string
import matplotlib.pyplot as plt


def read_sentence(file_name):
    with open(file_name, 'r') as file:
        sentence = file.readline().strip()
    return sentence


def count_words(sentence):
    words = sentence.split()
    return len(words)


def reverse_letters(word):
    return word[::-1]

def replace_nth_word(sentence, n, new_word):
    words = sentence.split()
    if n <= len(words):
        words[n-1] = new_word
    new_sentence = ' '.join(words)
    return new_sentence

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


def capitalize_first_letter(sentence):
    return sentence.capitalize()


def save_result(result, file_name):
    with open(file_name, 'w') as file:
        file.write(result)


def histogram(sentence):
    letter_freq = {}
    for letter in sentence:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    letters = list(letter_freq.keys())
    frequencies = list(letter_freq.values())

    plt.bar(letters, frequencies)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Histogram')
    plt.show()



file_name = 'sentence.txt'
sentence = read_sentence(file_name)
word_count = count_words(sentence)

third_word = sentence.split()[2]
reversed_third_word = reverse_letters(third_word)
modified_sentence = replace_nth_word(sentence, 3, reversed_third_word)
reversed_sentence = reverse_sentence(modified_sentence)
capitalized_sentence = capitalize_first_letter(reversed_sentence)

result_file_name = 'result.txt'
save_result(capitalized_sentence, result_file_name)
print(word_count)
histogram(sentence)
