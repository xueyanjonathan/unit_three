def add_one(number):
    number += 1
    print("number in function is", number)  # 28


def main():
    number = 27
    add_one(number)
    print("number in main is", number)  # 27


main()
