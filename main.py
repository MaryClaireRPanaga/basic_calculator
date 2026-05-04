class BasicCalculator:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
    def set_numbers(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
class Operations(BasicCalculator):
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return self.num1 / self.num2
class CalculatorApp(Operations):
    def run(self):
        while True:
            try:
                print("\nSelect operation:")
                print("Addition")
                print("Subtraction")
                print("Multiplication")
                print("Division")
                choice = input("Enter choice (1/2/3/4): ")
                if choice not in ['1', '2', '3', '4']:
                    print("Invalid input! Please choose a valid operation.")
                    continue
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                self.set_numbers(num1, num2)
                if choice == '1':
                    result = self.add()
                    operation = "Addition"
                elif choice == '2':
                    result = self.subtract()
                    operation = "Subtraction"
                elif choice == '3':
                    result = self.multiply()
                    operation = "Multiplication"
                elif choice == '4':
                    result = self.divide()
                    operation = "Division"
                print(f"\n{operation} of {num1} and {num2} is: {result}")
            except ValueError:
                print("Invalid input! Please enter numeric values for numbers.")
            except ZeroDivisionError as zde:
                print(zde)
            try_again = input("\nWould you like to try again? (yes/no): ").lower()
            if try_again not in ['yes', 'y']:
                print("Thank you!")
                break