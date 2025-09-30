# Chapter 4 Age Group Classifier with Repetition and Decision Structures
# Author: Blake Reed
# Date: 9/17/2025

def get_valid_age():
    """
    Prompt the user to enter their age until they provide
    a valid positive integer. Returns the valid age as an integer.
    """
    while True:
        age_input = input("Enter your age: ")
        if age_input.isdigit():  #Checks if the input is only digits
            age = int(age_input)
            if age > 0:
                return age
            else:
                print("Please enter a valid positive number for age.")
        else:
            print("Please enter a valid positive number for age.")

def classify_age(age):
    """
    Classify the user based on their age and print the message.
    """
    if 6 <= age <= 10:
        print("You are in Primary or Elementary School.")
    elif 11 <= age <= 13:
        print("You are in Middle School.")
    elif 14 <= age <= 18:
        print("You are in High School.")
    elif age >= 19:
        print("You are an adult. Choose your career path.")
    else:  #Age < 6
        print("You are too young for elementary school.")

def main():
    """
    Main function to control the program flow.
    """
    while True:  #Outer loop for repeating the whole process
        age = get_valid_age()  #Validate age
        classify_age(age)      #Classify age group

        #Ask if user wants to repeat
        repeat = input("Would you like to enter another age? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Thank you for using the Age Group Classifier. Goodbye!")
            break  #Exit the loop and end program

#Run the program
if __name__ == "__main__":
    main()
