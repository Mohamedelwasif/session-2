class SimpleCalculator:
    def __init__(self):
        self.running = True
    
    def run(self):
        # Main loop of the calculator
        while self.running:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == '5':
                self.exit_program()
            elif choice in ['1', '2', '3', '4']:
                self.perform_operation(choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 5.\n")
    
    def display_menu(self):
        # Display the list of operations to the user
        print("Simple Calculator")
        print("-----------------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
    
    def get_number(self, prompt):
        # Get a valid number from the user, retrying if input is invalid
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def perform_operation(self, choice):
        # Perform the selected operation based on the user's choice
        num1 = self.get_number("Enter the first number: ")
        num2 = self.get_number("Enter the second number: ")

        if choice == '1':
            result = self.add(num1, num2)
            print(f"The result of addition is: {result}\n")
        elif choice == '2':
            result = self.subtract(num1, num2)
            print(f"The result of subtraction is: {result}\n")
        elif choice == '3':
            result = self.multiply(num1, num2)
            print(f"The result of multiplication is: {result}\n")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.\n")
            else:
                result = self.divide(num1, num2)
                print(f"The result of division is: {result}\n")
        
        self.ask_to_continue()

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
    
    def ask_to_continue(self):
        # Ask the user if they want to perform another calculation
        while True:
            choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if choice == 'yes':
                return
            elif choice == 'no':
                self.exit_program()
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    
    def exit_program(self):
        # Exit the calculator program
        print("Exiting the program. Goodbye!")
        self.running = False

# Instantiate and run the calculator
calculator = SimpleCalculator()
calculator.run()
