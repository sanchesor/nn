import numpy as np

class Network:

    def __init__(self, sizes):
        self.sizes = sizes;
        self.biases = [np.random.randn(y,1) for y in self.sizes[1:]]
        self.weights = [np.random.randn(y,x)
            for x,y in zip(self.sizes[:-1], self.sizes[1:]) ]

    def show(self):
        np.set_printoptions(precision=2)
        for l in range(0, len(self.sizes)-1):
            print('=== layer',l+1, ' ===')
            print(self.weights[l])
            print(self.biases[l])

        np.set_printoptions(precision=8)
