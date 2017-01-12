import random

# menu
def menu():
  user_enter = get_user_number()
  lottery_number = create_lottery_numbers()
  match_numbers = user_enter.intersection(lottery_number)
  print("you got {}, you won ${}!".format(len(match_numbers),100**len(match_numbers)))



# User can pick 6 numbers
def get_user_number():
    number_csv = input("enter 6 number, separated by commas: ")
    number_list = number_csv.split(",")
    integer_set = {int(num) for num in number_list}
    return integer_set


# lottery calculate 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1,20))
    return values



menu()
