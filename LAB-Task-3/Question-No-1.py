def cli_calculator():
    print("Welcome to the CLI Calculator!")
    while True:
        command = input("Enter a command (add, subtract, multiply, divide, power, modulus, quit): ").strip().lower()
        
        if command == "quit":
            print("Exiting the calculator. Goodbye!")
            break
        
        try:
            if command == "power":
                base = float(input("Enter the number: "))
                exponent = float(input("Enter the power: "))
                print(f"Result: {base ** exponent}")
            elif command in ["add", "subtract", "multiply", "divide", "modulus"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if command == "add":
                    print(f"Result: {num1 + num2}")
                elif command == "subtract":
                    print(f"Result: {num1 - num2}")
                elif command == "multiply":
                    print(f"Result: {num1 * num2}")
                elif command == "divide":
                    if num2 == 0:
                        print("Error: Division by zero.")
                    else:
                        print(f"Result: {num1 / num2}")
                elif command == "modulus":
                    if num2 == 0:
                        print("Error: Modulus by zero.")
                    else:
                        print(f"Result: {num1 % num2}")
            else:
                print("Invalid command. Try again.")
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

cli_calculator()