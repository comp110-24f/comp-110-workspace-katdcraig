def remove_chars(msg: str, char: str) -> str:
    index: int = 0
    copy: str = ""
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
        index += 1
    return copy


word: str = "yoyo"
print(remove_chars(msg=word, char="y"))
print(remove_chars(msg=word, char="o"))
