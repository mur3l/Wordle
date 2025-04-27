import random
import os

WORDS = [
    "about", "after", "again", "below", "could", "every", "first", "found", "great", "heart",
    "knife", "large", "later", "light", "means", "money", "night", "place", "right", "short",
    "since", "small", "sound", "still", "table", "thing", "those", "under", "water", "while",
    "world", "young", "which", "women", "apple", "agree", "begin", "bring", "clean", "close",
    "glass", "drive", "enjoy", "exist", "fight", "floor", "focus", "front", "grace", "learn",
    "leave", "flame", "press", "quick", "ready", "reach", "scale", "share", "shine", "sight",
    "skill", "start", "stick", "study", "creep", "teach", "child", "grass", "waste", "watch",
    "write", "yearn", "yield", "admit", "alarm", "anger", "apply", "block", "bored", "check",
    "claim", "class", "clear", "clock", "ocean", "cloud", "crack", "crash", "creek", "drink",
    "earth", "empty", "enter", "error", "exact", "favor", "grape", "haste", "house", "climb",
    "happy", "knees", "lucky", "lunch", "major", "march", "model", "noble", "order", "paint",
    "plane", "power", "truck", "raise", "fruit", "stone", "shout", "space", "spend", "squad",
    "lever", "steer", "store", "strip", "straw", "sweep", "horse", "think", "thick", "touch",
    "trace", "trust", "unite", "verse", "video", "voice", "vowel", "plant", "wrist", "zebra"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_guess():
    while True:
        guess = input("Enter your word (5 letters): ").lower()  # Change all to lowercase
        if len(guess) == 5 and guess.isalpha():  #  Check if all are only letters
            return guess
        print("BIG ALARM! Enter 5 letters only.")

def check_guess(guess, target):
    result = []
    target_list = list(target)

    """First pass: mark correct letters"""
    for i in range(5):
        if guess[i] == target[i]:
            result.append("🟩")  # Correct letter, correct position
            target_list[i] = None
        else:
            result.append("⬜")  # Wrong letter

    """Second pass: mark letters in wrong position"""
    for i in range(5):
        if result[i] == "⬜":
            if guess[i] in target_list:
                result[i] = "🟨"  # Correct letter, wrong position
                target_list[target_list.index(guess[i])] = None

    return "".join(result)

def play_wordle():
    target_word = random.choice(WORDS)
    attempts = 6
    guessed_words = []

    print("Welcome to Wordle!")
    print("Guess a five letter word. You have six attempts.")
    print("🟩 - Correct letter in correct position.")
    print("🟨 - Correct letter in wrong position.")
    print("⬜ - Wrong letter.")

    """Prints attempts remaining and past guess"""
    while attempts > 0:
        print(f"\nRemaining attempts: {attempts}")
        print("Past guess:")
        for word, result in guessed_words:
            print(f"{word} - {result}")

        guess = get_valid_guess()
        result = check_guess(guess, target_word)
        guessed_words.append((guess, result))

        if guess == target_word:
            print(f"\nCongratulatioons! You guessed it: {target_word}")
            return True

        attempts -= 1

    print(f"\nIncorrect guess! The word was: {target_word}")
    return False

if __name__ == "__main__":
    while True:
        clear_screen()
        play_wordle()
        if input("\nDo you wish to play again? (yes/no): ").lower() != "yes":
            break
    print("Thanks for playing -Tauno & Robert!")