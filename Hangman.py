from Hangman_files import stages, logo
import random

print(f"\nWelcome to the Hangman game! You know the rules, Let's play!\n{logo}")

word_list = ["rohit", "amlan", "suraj", "subhajit", "raimalu"]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
end_of_game = False
lives = 6

for _ in range(word_length):
    display.append('_')

while not end_of_game:
    guess = str(input("\nGuess a letter: ")).lower()
    if guess in display:
        print(f"\nYou've already guessed {guess}")
    else:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    
    if '_' not in display:
        print(stages[lives])
        print(*display)
        print("\nYou've won!")
        print(f"\nThe word was: {chosen_word}\n")
        break
        
    if lives == 0 and guess not in display:
        print(stages[0])
        print("\nYou've lost!\n")
        break
    
    if guess not in display:
        print(f"\nYou've chosen {guess}, that's incorrect, you've lost a life!")
        lives -= 1         
    print(stages[lives])
    print(*display)