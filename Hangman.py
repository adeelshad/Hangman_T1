import random

def choose_word():
    words = ["adeel", "sunflower", "peter", "gwen", "spiderman"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    
    print("Welcome to Hangman 69!")
    
    while incorrect_guesses < max_attempts:
        print("\nWord: ", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! {max_attempts - incorrect_guesses} attempts left.")
    else:
        print("Game over! The word was:", word)

if __name__ == "__main__":
    hangman()
