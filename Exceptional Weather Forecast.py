def temp_conversion():
    try:
        user_input = (input("Please enter a temperature in Farenheit: "))#Question 1 Task 1
        user_temp = float(user_input)
        temp_in_celsius = (user_temp - 32) * 5 / 9 #Question 1 Task 2
        rounded_number = round(temp_in_celsius, 2)
    except ValueError as ve:
        if "string to float" in str(ve):
            print("That is not a number. Please enter valid number.")
    else:
        print(f"{user_input} degrees Farenheit is {rounded_number} degrees Celsius!")#Question 1 Task 3
    finally:
        print("Thank you for using the weather forecast application!")#Question 1 Task 4
        
temp_conversion()