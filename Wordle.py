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
        guess = input("Sisesta oma pakkumine (5 tähte): ").lower()
        if len(guess) == 5 and guess.isalpha():
            return guess
        print("Viga! Palun sisesta täpselt 5 tähte.")

def check_guess(guess, target):
    result = []
    target_list = list(target)

    """First pass: mark correct letters"""
    for i in range(5):
        if guess[i] == target[i]:
            result.append("")  # Correct letter, correct position
            target_list[i] = None
        else:
            result.append("")  # Wrong letter

    """Second pass: mark letters in wrong position"""
    for i in range(5):
        if result[i] == "":
            if guess[i] in target_list:
                result[i] = ""  # Correct letter, wrong position
                target_list[target_list.index(guess[i])] = None

    return "".join(result)