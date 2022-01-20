from replit import clear
import random
from hangman_words import word_list
from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)

l = len(chosen_word)
replacement = 'x' * l
display = ['_'] * l
lives = 6
end_of_game = False

while not end_of_game:
    print(f'The word you need to guess is {replacement}.\n')
    print(f'You have {lives} left to win this game!')
    #Let the user input
    guess = input('Please guess a letter: ')
    clear()

    if guess in display:
        print(f"You have already guessed {guess}")

    if guess not in chosen_word:
        print(f'You guess {guess}, That is not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            print('You are out of life. You lose.')
            end_of_game = True
    # guess in chosen_word
    for i in range(l):
        if guess == chosen_word[i]:
            display[i] = guess
    #switch display from a list to a string
    print(f"{' '.join(display)}")
    if '_' not in display:
        print('You win.')
        end_of_game = True

    from hangman_art import stages
    print(stages[lives])

print(f'The chosen word is {chosen_word}.')