import time
from random import choice


def get_word_from_file(filename):
    with open(filename) as fp:
        words = fp.readlines()
    return choice(words).strip()


def get_hidden_word(word):
    out = []
    for i in range(len(word)):
        out.append('_')
    return out


def process_guess(chosen, hidden, guess, current_fails):
    if chosen.count(guess) <= 0:
        return hidden, current_fails + 1
    for i in range(len(chosen)):
        if chosen[i] == guess:
            hidden[i] = guess
    return hidden, current_fails


def test_end_conditions(curr_fail, max_fail, chosen, hidden):
    if curr_fail > max_fail:
        return False
    if ''.join(hidden) == chosen:
        return False
    return True


def get_stats(filename, length):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', '-', '(', ')', '.', '/', "'", '`, ', '\x03']
    letters_count = [0] * len(letters)
    count = 0
    with open(filename) as fp:
        words = fp.readlines()
        for word in words:
            word = word.strip()
            count += 1
            if len(word) == length:
                for letter in word:
                    try:
                        i = letters.index(letter)
                    except:
                        letters.append(letter)
                    letters_count[i] += 1
    return letters, letters_count


def get_guess(letters, letters_count):
    largest_value = max(letters_count)
    index_largest_value = letters_count.index(largest_value)
    most_likely = letters[index_largest_value]
    letters_count[index_largest_value] = 0
    return most_likely


file_name = 'better_words.txt'
chosen_word = get_word_from_file(file_name)
hidden_word = get_hidden_word(chosen_word)

playing = True
max_fails = 10
current_fails = 0
print(chosen_word)

letters, letters_count = get_stats(file_name, len(hidden_word))
print(letters, letters_count)

while playing:
    print(f'Current guess {"".join(hidden_word)}. You have {max_fails - current_fails} chances left.')
    # guess = input("Guess a letter: ")
    guess = get_guess(letters, letters_count)
    print(f"You guessed {guess}")
    #todo update the stats based off of what we know
    hidden_word, current_fails = process_guess(chosen_word, hidden_word, guess, current_fails)
    playing = test_end_conditions(current_fails, max_fails, chosen_word, hidden_word)
    time.sleep(1)

if ''.join(hidden_word) == chosen_word:
    print("You are the winner!")
else:
    print(f"You are a loser! The word was {chosen_word}")
