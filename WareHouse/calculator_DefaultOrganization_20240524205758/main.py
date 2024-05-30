python
'''
Calculator Application Main File
'''
import tkinter as tk
from gui_components import GUIComponents
from calculator_operations import CalculatorOperations
class Calculator:
    def __init__(self, root):
        self.root = root
        self.gui_components = GUIComponents(self.root)
        self.calculator_operations = CalculatorOperations()
        self.create_gui()
    def create_gui(self):
        # Create GUI layout and widgets
        self.gui_components.create_label("Enter Number 1:", 0, 0)
        self.gui_components.create_entry(0, 1)
        self.gui_components.create_label("Enter Number 2:", 1, 0)
        self.gui_components.create_entry(1, 1)
        self.gui_components.create_label("Result:", 2, 0)
        self.gui_components.create_label("", 2, 1)
        self.gui_components.create_button("Add", 3, 0, lambda: self.perform_calculation("add"))
        self.gui_components.create_button("Subtract", 3, 1, lambda: self.perform_calculation("subtract"))
        self.gui_components.create_button("Multiply", 4, 0, lambda: self.perform_calculation("multiply"))
        self.gui_components.create_button("Divide", 4, 1, lambda: self.perform_calculation("divide"))
    def perform_calculation(self, operation):
        num1 = float(self.gui_components.get_entry(0))
        num2 = float(self.gui_components.get_entry(1))
        result = self.calculator_operations.perform_operation(operation, num1, num2)
        self.gui_components.set_label(2, 1, str(result))
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()