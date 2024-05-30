python
'''
GUI Components Class
'''
import tkinter as tk
class GUIComponents:
    def __init__(self, root):
        self.root = root
        self.labels = []
        self.entries = []
        self.buttons = []
    def create_label(self, text, row, column):
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=column)
        self.labels.append(label)
    def create_entry(self, row, column):
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=column)
        self.entries.append(entry)
    def create_button(self, text, row, column, command):
        button = tk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=column)
        self.buttons.append(button)
    def get_entry(self, index):
        return self.entries[index].get()
    def set_label(self, row, column, text):
        self.labels[row * 2 + column].config(text=text)