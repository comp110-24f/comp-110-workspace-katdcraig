"""Basic syntax of lists"""

# on lists:
my_numbers: list[float] = []

print(my_numbers)

my_name: str = ""
my_name: str = str()

# on appending lists:
# <list name>.append(<item>)

my_numbers.append(1.5)
print(my_numbers)

# creating populated list:
game_points: list[int] = [102, 86, 94]
print(game_points)
# print(game_points[4])

# modifying lists:
game_points[1] = 102
print(game_points)

# mutability and lists/str/int:
class_1: int = 110
# class_1[0] = 2
# doesn't work, only works w lists

# removing value from list:
game_points.pop(2)
print(game_points)


def display(list_num: list[int]) -> None:
    index: int = 0
    while index < len(list_num):
        print(list_num[index])
        index += 1


display(game_points)
