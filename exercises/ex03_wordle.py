"""Wordle game!"""

__author__: str = "730659835"


def input_guess(secret_word_len: int) -> str:
    """Returns user's guess"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    # note f-string usage
    while len(guess) != secret_word_len:
        # protects against incorrect character count
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, character: str) -> bool:
    """Searches secret word for character"""
    assert len(character) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == character:
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns accuracy of user guess in emojis"""
    assert len(guess) == len(secret_word)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    # ^^^ these are hex keys for emoji outputs
    index: int = 0
    emojis: str = ""
    # "" because we start with no output
    while index < len(guess):
        """Concatenates emojis for output"""
        if guess[index] == secret_word[index]:
            # for correct letter in correct place
            emojis += green_box
        elif contains_char(secret_word=secret_word, character=guess[index]) is True:
            # for correct letter in incorrect place
            emojis += yellow_box
        else:
            # for incorrect letter
            emojis += white_box
        index += 1
    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    secret_word_len = len(secret)
    guess = ""
    turn: int = 1
    while turn <= 6 and guess != secret:
        # 6 guesses to find word
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len)
        print(emojified(guess, secret_word=secret))
        turn += 1
    if guess == secret:
        print(f"You won in {turn-1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    # exits are not mentioned in the instructions BUT I think they improve style
    # since they close the REPL and stop the program at the natural conclusion


if __name__ == "__main__":
    main(secret="codes")
# ^^^ allows file to be run as module
