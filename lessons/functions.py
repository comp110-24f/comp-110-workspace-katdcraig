def sum(num1: int, num2: int) -> int:
    return num1 + num2


print(sum(num1=5, num2=3))


def comm_add(num_11: int, num_12: int) -> int:
    return num_11 + num_12


print(comm_add(num_11=sum(num1=2, num2=3), num_12=3))


def echo(word: str, times: int) -> str:
    return word * times


print(echo(word="hello", times=4))


def flavor(taste: str, percent: float) -> None:
    print("This flavor is " + str(percent) + "% " + taste)


flavor(taste="umami", percent=100)


def eat(food: str) -> None:
    print("Eating " + food)


def main(food: str) -> None:
    food_item = "apple"
    eat(food=food)


main(food="apple")


def have_done(task, completed) -> str:
    return "Completed " + task + ": " + str(completed)


print(have_done("homework", False))


def start_end(word: str) -> str:
    return word[0] + word[len(word) - 1]


start_end(word="kitkat")
print(start_end(word="skittles"))
