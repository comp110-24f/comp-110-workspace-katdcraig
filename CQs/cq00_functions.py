def mimic(message: str) -> str:
    """Repeats typed message"""
    return message


def main() -> None:
    """Prints result of mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
