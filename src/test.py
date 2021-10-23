import random

def sort(list):
    for j in range(len(list)):
        for i in range(len(list)):
            if list[j] < list[i]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp


def main():
    userInput = "y"
    while userInput.isdigit() == False:
        try:
            userInput = input("Give me a number: ")
            if eval(userInput) > 10:
                print("This is greater than 10")
            else:
                print("This is less than 10")
        except (NameError):
            userInput = "y"



main()