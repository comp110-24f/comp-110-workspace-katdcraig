"""Conditionals practice"""


def less_than_10(num: int) -> None:
    """Say if # is <10"""
    if num < 10:
        print("Small #")
    else:
        print("Big #")
    print("Goodbye")


less_than_10(num=2)


def check_first_letter(word: str, letter: str) -> None:
    if word[0] == letter[0]:
        print("match!")
    else:
        print("no match!")


check_first_letter(word="plant", letter="b")
check_first_letter(word="plant", letter="P")
