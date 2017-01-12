import random

def ask_user_and_check_number():
    user_number = int(input("input numbers"))
    if user_number in magic_number:
        #print("this is your "+ str(attempt+1) + " attempt")
        return "you got it "

    if user_number not in magic_number:
       return "wrong......."

magic_number = [random.randint(1,9),random.randint(1,9)]


def run_program(chance):
    for attempt in range(chance):
       message = ask_user_and_check_number()
       print(message)
 

run_program(5)

##chance = 10
##min_number = 100 
##
##for time in range(chance):
##    random_number = random.randint(0,9)
##    if random_number < min_number:
##        min_number =  random_number
##
##
##print(min_number)

    
    
