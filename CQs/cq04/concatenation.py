"""Concatenates 2 input strings"""

__author__: str = "730659835"


def concat(input1: str, input2: str) -> str:
    """Concatenates input strings together"""
    return input1 + input2


if __name__ == "__main__":
    # so these aren't registered when imported
    word1 = "happy"
    word2 = "tuesday"
    print(concat(input1=word1, input2=word2))
