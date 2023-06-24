import math
import random
import numpy as np;

class Perceptron:
    def __init__(self, n_inputs):
        self.synaptic_weights =np.array([random.random() for _ in range(n_inputs)])

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return self.sigmoid(x)*(1-self.sigmoid(x))

    def train(self, inputs, outputs, iterations):
        for _ in range(iterations):
            output = self.think(inputs) # O = S(I x W)
            error = outputs - output   # E = T - O
            delta_weight = np.dot(inputs.transpose(), error*self.sigmoid_derivative(output)) # ΔW = I.T x (E * S(O))
            self.synaptic_weights += delta_weight	
    
    def think(self, inputs):
        return self.sigmoid(np.dot(inputs, self.synaptic_weights)) 
    
    def predict(self,input):
        #print(self.think(input))
        return round(self.think(input))

if __name__ == "__main__":
    initial_iterations = 1
    for _ in range(4): # train the network 3 times with different iterations
        p = Perceptron(3)
        initial_iterations*=10
        print("Initial iterations:", initial_iterations)
        print("Weights before: ", p.synaptic_weights)
        p.train(np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]]), np.array([0,1,1,0]), initial_iterations)
        print("Predicted logical output: ", p.predict(np.array([0,1,0])))
        print("Weights after: " , p.synaptic_weights)
        print("\n")
