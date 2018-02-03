import numpy as np

class Network:

    def __init__(self, sizes):
        self.sizes = sizes;
        self.num_layers = len(sizes)
        self.biases = [np.random.randn(y) for y in self.sizes[1:]]
        self.weights = [np.random.randn(y,x)
            for x,y in zip(self.sizes[:-1], self.sizes[1:]) ]
        self.nets = [np.zeros(y) for y in self.sizes[1:]]
        self.outputs = [np.zeros(y) for y in self.sizes[1:]]

    def forward(self, input):
        l_input = input
        for l in range(0, self.num_layers-1):
            self.nets[l] = np.dot(self.weights[l], l_input) + self.biases[l]
            self.outputs[l] = self.activation(self.nets[l])
            l_input = self.outputs[l]

    def activation(self, x):
        return 1.0/(1.0 + np.exp(-x))

    def show(self):
        np.set_printoptions(precision=2)
        for l in range(0, len(self.sizes)-1):
            print('=== layer',l+1, ' ===')
            print('weights',self.weights[l])
            print('biases',self.biases[l])
            print('net',self.nets[l])
            print('out',self.outputs[l])

        np.set_printoptions(precision=8)
