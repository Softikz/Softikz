import time
import os

frames = [
    r"""
    O
   /|\
   / \
    """,
    r"""
    \O/
     |
    / \
    """,
    r"""
     O
    /|\
    / \
    """,
    r"""
    O/
     |
    / \
    """
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    for frame in frames:
        clear_console()
        print(frame)
        time.sleep(0.3)