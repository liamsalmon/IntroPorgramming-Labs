# File: Homework 2
# Liam Salmon - INTRO TO PROGRAMMING - CMPT 120L 901
# Assignment 2 - Programming Problem 1
# Date - 1 March 2021

# Question: Why is it a good idea to first write out an algorithm in pseudocode rather than jumping immediately to Python code?
# Answer: Pseudocode is just precise English that describes what a program does. It is a good idea to first write out an algorithm in pseudocode because it can communicate algorithms without the minor details needed in python code.


# File: Homework 2
# Liam Salmon - INTRO TO PROGRAMMING - CMPT 120L 901
# Assignment 2 - Programming Problem 2
# Date - 1 March 2021

# convert.py 
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell 
def  main():
    print ("This program is a temperature converter")
    celcius = eval(input("What is the Celcius temperature?"))
    fahrenheit =  ((9/5) * celcius) + 32
    print ("The temperature", celcius, "deg Celcius = ",fahrenheit,"deg fahrenheit")

main()

# File: Homework 2
# Liam Salmon - INTRO TO PROGRAMMING - CMPT 120L 901
# Assignment 2 - Programming Problem 3
# Date - 1 March 2021

# convert.py 
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell 
def  main():
    print ("This program is a temperature converter")
    
    celcius = eval(input("What is the Celcius temperature?"))
    fahrenheit =  ((9/5) * celcius) + 32
    
    print ("The temperature", celcius, "deg Celcius = ",fahrenheit,"deg fahrenheit")
    input("Press the <Enter> key to quit.")
    
main() 

# File: Homework 2
# Liam Salmon - INTRO TO PROGRAMMING - CMPT 120L 901
# Assignment 2 - Programming Problem 4
# Date - 1 March 2021

# futval.py 
# A program to compute the value of an investment 
# Carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
          
    years = eval(input("Enter the number of years of the investment: "))
    

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in ", years ,"years " "is:", principal)

main()


# File: Homework 2
# Liam Salmon - INTRO TO PROGRAMMING - CMPT 120L 901
# Assignment 2 - Programming Problem 5
# Date - 1 March 2021
    


def  main():
    
    
    print ("This program is a temperature converter")
    print ("1: Convert temperature from Fahrenheit to Celsius.")
    print ("2: Convert temperature from Celsius to Fahrenheit.")
    
    temperature = int(input("Enter your choice (1 or 2):"))
    
    if temperature >= 2:
            print("Enter the temperature in Celsius.")
            fahrenheitTemperature =  ((9/5) * celciusTemperature) + 32
            print ("The temperature", celciusTemperature, "deg Celsius = ",fahrenheitTemperature,"deg fahrenheit")
                      
    elif temperature <= 1:
            print("Enter the temperature in Fahrenheit.")
            celciusTemperature = (-32 + fahrenheitTemperature) / (9/5)
            print ("The temperature", fahrenheitTemperature, "deg Celsius = ",celciusTemperature,"deg fahrenheit")

    else:
        print("invalid option")


        
main()




