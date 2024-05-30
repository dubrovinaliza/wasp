python
'''
Calculator Operations Class
'''
class CalculatorOperations:
    def perform_operation(self, operation, num1, num2):
        if operation == "add":
            return self.add_numbers(num1, num2)
        elif operation == "subtract":
            return self.subtract_numbers(num1, num2)
        elif operation == "multiply":
            return self.multiply_numbers(num1, num2)
        elif operation == "divide":
            return self.divide_numbers(num1, num2)
    def add_numbers(self, num1, num2):
        return num1 + num2
    def subtract_numbers(self, num1, num2):
        return num1 - num2
    def multiply_numbers(self, num1, num2):
        return num1 * num2
    def divide_numbers(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"