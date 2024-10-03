"""Calculate cost of tea party for you and friends"""

__author__: str = "730659835"


def main_planner(guests: int) -> None:
    """Prints final output"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# Defining variables tea_count and treat_count necessary?
# RESOLVED AT OFFICE HRS
# (No, see reasons below)


def tea_bags(people: int) -> int:
    """Determines number of tea bags needed"""
    return people * 2


# Not sure how to define tea_count to work in cost function
# RESOLVED AT OFFICE HRS
# (not needed; just fill in tea_count parameter with tea_bags(guests))


def treats(people: int) -> int:
    """Determines number of treats needed"""
    return int((tea_bags(people=people)) * 1.5)


# NEEDS KEYWORD ARGUMENT?
# RESOLVED AT OFFICE HRS
# (keyword argument is putting in a keyword as argument instead of a simple number)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines total cost"""
    return tea_count * 0.5 + treat_count * 0.75


# How to turn tea_bags into tea_count?
# RESOLVED AT OFFICE HRS
# (unnecessary as tea_count and treat_count are simply parameters;
# plug in whatever arg in function call)

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
