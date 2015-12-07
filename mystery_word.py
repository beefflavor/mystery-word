import random


def word_list():
    with open("/usr/share/dict/words") as word_bank:
        clean_bank = word_bank.read().lower().split('\n')

    return clean_bank


def easy_words(word):
    print("easy mode")
    all_easy_words = list(filter((lambda x: len(x) >= 4 and len(x) <= 6 ), word))

    return all_easy_words


def medium_words(word):
    print("medium mode")
    all_medium_words = list(filter((lambda x: len(x) >= 6 and len(x) <= 8), word))

    return all_medium_words


def hard_words(word):
    print("hard mode")
    all_hard_words = list(filter((lambda x: len(x) >= 8), word))

    return all_hard_words


def random_word(word):
    return random.choice(word)


def pick_mode():
    while True:
        players_input = input('type in easy, medium, or hard')
        if players_input == "easy":
            return "easy"
        elif players_input == "medium":
            return "medium"
        elif players_input == "hard":
            return "hard"
        else:
            print("try again")


def guess():
    while True:
        players_guess = input("guess a letter >")
        if len(players_guess) == 1:
            return players_guess
        else:
            print("enter a letter")
            continue


def display_word(word, letter_list):
    show_list = []
    for letter in word:
        if letter in letter_list:
            show_list.append(letter.upper())
        else:
            show_list.append("_")
    show = (" ".join(show_list))
    return show


def is_word_complete(word,  letter_list):
    for letter in word:
        if letter in letter_list:
            continue
        else:
            return False
    return True


def game():
    word_list_for_game = word_list()
    mode = pick_mode()
    if mode == "easy":
        word = random_word(easy_words(word_list_for_game))
    elif mode == "medium":
        word = random_word(medium_words(word_list_for_game))
    else:
        word = random_word(hard_words(word_list_for_game))
        print("{} letters".format(len(word)))
    max_guess = 8
    number_of_guess = []
    used_guesses = 0

    while used_guesses < max_guess:
        players_guess = guess()
        if players_guess in number_of_guess:
            print("already guessed")
            continue
        number_of_guess.append(players_guess)
        if is_word_complete(word, number_of_guess):
            print("winner")
            print(word)
            break
        if players_guess in word:
            print("yes, you have {} guesses left".format(max_guess - used_guesses))
            print(display_word(word, number_of_guess))
        else:
            used_guesses += 1
            print("no, you have {} guesses left".format(max_guess - used_guesses))
            print(display_word(word, number_of_guess))
        if max_guess - used_guesses == 0:
            print("loser")
            print(word)


def again():
    while True:
        play_again = input("play again? yes or no >{}")
        if play_again == "yes":
            return True
        elif play_again == "no":
            return False
        else:
            print("try again")

if __name__ == '__main__':
    game_on = True
    while game_on:
        game()
        game_on = again()
    print("thanks for playing")
