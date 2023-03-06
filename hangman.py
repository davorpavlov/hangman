import time
import os

def clear():
    os.system('cls')

def hangman_animation():
    frames = [
        r"""
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========""",
        r"""
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========""",
        r"""
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========""",
        r"""
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========""",
        r"""
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========""",
        r"""
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========""",
        r"""
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========""",
        r"""
              +---+
              |   |
             \O/  |
              |   |
             / \  |
                  |
            =========""",
        r"""
              +---+
              |   |
             \O/  |
              |   |
             / \  |
            _/   \_
            =========""",
    ]

    for frame in frames:
        clear()
        print(frame)
        time.sleep(1)  # Adjust the time delay as needed

hangman_animation()
