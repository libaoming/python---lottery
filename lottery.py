import random

# User can pick 6 numbers
def get_user_number():
    number_csv = input("enter 6 number, separated by commas: ")
    number_list = number_csv.split(",")
    integer_set = {number for num in number_list}
    return integer_set


# lottery calculate 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1,20))
    return values


print(create_lottery_numbers())
