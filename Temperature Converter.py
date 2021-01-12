#Importing necessary modules
import os
import time

#For clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#Conversions which can be performed
print("The conversions which you can perform are :\n" "1. To convert celsius to farenheit\n"\
            "2. To convert  farenheit to celsius\n" "3. To convert celsius to kelvin\n"
            "4. To convert farenheit to kelvin\n" "5. To convert kelvin to celsius\n"
            "6. To convert kelvin to farenheit\n")

#while loop for doing conversions continuously until user ends the program
while True:

    #For user input of conversion(try-except to check if the input is an integer or not)
    try:
        user_input = int(input('Choose from 1, 2, 3, 4, 5, 6: '))
        
    except ValueError:
        print("Invalid input..\nTry again!")
        time.sleep(1)
        print("**There is a warning for you! If you enter any alphabet as the input once again then the program will end**")
        try:
            user_input = int(input('Choose from 1, 2, 3, 4, 5, 6: '))
            
        except:
            print("You have typed an alphabet again.\nThe program will end now.\nPlease Try again later.")
            time.sleep(2)
            break

#Commands for the conversions
    try:
        
        if user_input == 1:
            
            celsius = float(input("Enter the value of temperature in celsius: "))
        
            farenheit = celsius * 9 / 5 + 32
        
            print('The converted temperature from Celsius to Farenheit is:', farenheit)

    
        elif user_input == 2:
    
            farenheit = float(input("Enter the value of the temperature in farenheit: "))
    
            celsius = (farenheit - 32) * 5 / 9
    
            print('The converted temperature from farenheit to Celsius is:', celsius)
    

        elif user_input == 3:
    
            celsius = float(input("Enter the value of temperature in celsius: "))
    
            kelvin = celsius + 273.15
    
            print('The converted temperature from celsius to kelvin is:', kelvin)
    
    
        elif user_input == 4:
    
            farenheit = float(input("Enter the value of the temperature in farenheit: "))
    
            kelvin = (farenheit - 32) * 5/9 + 273.15
    
            print('The converted temperature from farenheit to kelvin is:', kelvin)
    
    
        elif user_input == 5:
    
            kelvin = float(input("Enter the value of the temperature in kelvin: "))
    
            celsius = kelvin - 273.15
    
            print('The converted temperature from kelvin to celsius is:', celsius)
    

        elif user_input == 6:
    
            kelvin = float(input("Enter the value of the temperature in kelvin: "))
    
            farenheit = (kelvin - 273.15) * 9/5 + 32
    
            print('The converted temperature from kelvin to farenheit is:',farenheit)
        
    
        else:
            print('Invalid Input\nTry again.')
            continue
    
    except:
        print('Enter an integer value!')
    
    #To rerun again
    rerun = input("Do you want to calculate again?\nPlease type 'yes' or 'no': ")
    
    if rerun == 'no' or rerun == 'No' or rerun == 'NO':
        print("Thank you.")
        break
    
    elif rerun == 'yes' or rerun == 'Yes' or rerun == 'YES':
        continue
    
    else:
        print("Invalid Input\nTry again...")
        rerun = input("Do you want to calculate again?\nPlease type 'yes' or 'no': ")
