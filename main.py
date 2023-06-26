def main():
    
    ##################################################
    # Comlete your code here
    # Use the same variables: celcius fahrenheit 
    ##################################################
    celcius = float(input("Enter the temperature in Celsius: "))

    fahrenheit = float((9/5)*celcius +32)

    print(f' The temperature is Fahrenheit is: \t {fahrenheit: .2f}' )


    
    ########################################
    # Do not delete the return statement
    ########################################
    
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
