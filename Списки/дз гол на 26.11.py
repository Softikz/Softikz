import random
number = 0
def check_for_goal():

    random_numbers = [random.randint(0, 5) for _ in range(1000)]

    for numbers in random_numbers:
        if numbers == 5:
            print("ГООООЛ")

check_for_goal()
