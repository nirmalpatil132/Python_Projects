import random
from hangman_wods import word_list
from hangman_stages import stages
from hangman_logo import logo

lives = 6
print(logo)

choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    
    
    print(f"************************{lives}/6 LIVES LEFT************************")
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed : {guess}")
    
    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: \n" +  display)
    
    

    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess} thats not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            
            print(f"************************IT WAS {choosen_word}! YOU LOSE************************")
            print("You Lose.")
            
    
    if "_" not in display:
        game_over = True
        print("************************YOU WIN************************")

    print(stages[lives])