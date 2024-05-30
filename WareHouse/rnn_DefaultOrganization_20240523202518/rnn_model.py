'''RNN Model Class'''
import numpy as np
class RNNModel:
    def __init__(self, seq_len, hidden_units):
        self.seq_len = seq_len
        self.hidden_units = hidden_units
        self.weights_xh = np.random.rand(hidden_units, seq_len)  # input to hidden weights
        self.weights_hh = np.random.rand(hidden_units, hidden_units)  # hidden to hidden weights
        self.biases = np.zeros((hidden_units, 1))
    def train(self, input_data, target_output):
        # Initialize hidden state
        hidden_state = np.zeros((self.hidden_units, 1))
        for t in range(self.seq_len):
            # Compute hidden state at time step t
            hidden_state = np.tanh(np.dot(self.weights_xh[:, t], input_data[t]) + np.dot(self.weights_hh, hidden_state) + self.biases)
        # Output computation
        output = np.dot(hidden_state.T, np.random.rand(self.hidden_units, 1))
        # Calculate loss and perform backpropagation
        loss = np.mean((output - target_output) ** 2)
        d_output = 2 * (output - target_output)
        d_hidden_state = d_output * (1 - hidden_state ** 2)
        for t in range(self.seq_len):
            d_weights_xh = np.dot(d_hidden_state, input_data[t].T)
            d_weights_hh = np.dot(d_hidden_state, hidden_state.T)
            d_biases = d_hidden_state
            self.weights_xh[:, t] -= 0.01 * d_weights_xh
            self.weights_hh -= 0.01 * d_weights_hh
            self.biases -= 0.01 * d_biases
        return loss