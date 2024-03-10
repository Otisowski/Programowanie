def zad_1():
    name = input("Your name: ")
    surname = input("Your surname: ")
    greeting = f"Cześć {name} {surname}!"
    print(greeting)

def zad_2():
    num_one = int(input("Enter first integer: "))
    num_two = int(input("Enter second integer: "))

    result = num_one * num_two
    print(f"The multiplication of {num_one} and {num_two} is {result}.")

def is_even(number: int) -> bool:
    return number % 2 == 0

def zad_3():
    num = int(input("Enter a number: "))

    if is_even(num):
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

def is_sum_greater_or_equal(a: int, b: int, c: int) -> bool:
    return (a + b) >= c

def zad_4():
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    num3 = int(input("Enter third integer: "))

    if is_sum_greater_or_equal(num1, num2, num3):
        print("The sum of the first two numbers is greater than or equal to the third number.")
    else:
        print("The sum of the first two numbers is less than the third number.")

def contains_value(lst: list, value: int) -> bool:
    return value in lst


def zad_5():
    numbers = [1, 3, 5, 7, 9]
    value_to_find = 5
    value_not_in_list = 6

    if contains_value(numbers, value_to_find):
        print(f"{value_to_find} is in the list.")
    else:
        print(f"{value_to_find} is not in the list.")

    if contains_value(numbers, value_not_in_list):
        print(f"{value_not_in_list} is in the list.")
    else:
        print(f"{value_not_in_list} is not in the list.")

def combine_lists(lst1: list, lst2: list) -> list:
    combined = lst1 + lst2
    unique = list(set(combined))
    cubed = [x ** 3 for x in unique]
    return cubed


def zad_6():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]

    result = combine_lists(list1, list2)
    print(result)


if __name__ == "__main__":
    # zad_1()
    # zad_2()
    # zad_3()
    # zad_4()
    # zad_5()
    zad_6()
