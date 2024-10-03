"""Wordle-esque game"""

__author__: str = "730659835"


def input_word() -> str:
    """User input for word"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return word


def input_letter() -> str:
    """User input for letter"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    """Checks if user's word contains guessed character"""
    print("Searching for", letter, "in", word)
    count: int = 0
    # general difficulty with static type errors on this section,
    # fixed by not redefining type in "else" block
    if word[0] == letter:
        print(letter, "found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter, "found at index 1")
        count = count + 1
        # don't need to add else in this in place of ->
        # if word[1] == letter --> count = count + 1
    if word[2] == letter:
        print(letter, "found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter, "found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter, "found at index 4")
        count = count + 1
        # endpoint of index checking

    if count == 1:
        print(count, "instance of", letter, "found in", word)
    elif count >= 2:
        print(count, "instances of", letter, "found in", word)
    else:
        print("No instances of", letter, "found in", word)
        # returns number of matches


def main() -> None:
    """Main function"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
# allows for file to be run as module
