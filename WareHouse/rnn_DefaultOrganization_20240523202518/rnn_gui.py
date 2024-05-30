'''RNN GUI Main File'''
import tkinter as tk
from tkinter import messagebox
from rnn_model import RNNModel
class RNNGUI:
    def __init__(self, master):
        self.master = master
        master.title("RNN GUI")
        self.create_widgets()
    def create_widgets(self):
        # Create input fields for sequence length and hidden units
        tk.Label(self.master, text="Sequence Length:").grid(row=0)
        self.seq_len_entry = tk.Entry(self.master)
        self.seq_len_entry.grid(row=0, column=1)
        tk.Label(self.master, text="Hidden Units:").grid(row=1)
        self.hidden_units_entry = tk.Entry(self.master)
        self.hidden_units_entry.grid(row=1, column=1)
        # Create button to train the model
        tk.Button(self.master, text="Train Model", command=self.train_model).grid(row=2)
        # Create label to display loss
        self.loss_label = tk.Label(self.master, text="Loss: ")
        self.loss_label.grid(row=3)
    def train_model(self):
        seq_len = int(self.seq_len_entry.get())
        hidden_units = int(self.hidden_units_entry.get())
        rnn_model = RNNModel(seq_len, hidden_units)
        loss = rnn_model.train(np.random.rand(seq_len, 1), np.random.rand(1, 1))
        self.loss_label.config(text=f"Loss: {loss:.4f}")
root = tk.Tk()
rnn_gui = RNNGUI(root)
root.mainloop()