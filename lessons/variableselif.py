# name:type = value
def number_info(num: int) -> int:
    if num < 10:
        print("sm #")
    else:
        if num % 2 == 0:
            print("even #")
        else:
            print("odd #")
    return num


number_info(num=11)
print(number_info(num=4))


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather


get_weather_report()
