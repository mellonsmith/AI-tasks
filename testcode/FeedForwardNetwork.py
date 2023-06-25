from copy import deepcopy
from multiprocessing import dummy
from perceptron import *
import matplotlib.pyplot as plt

class FeedForwardNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate
        # Initialize weights 
        self.weights_input_to_hidden = np.random.rand(self.input_nodes,self.hidden_nodes)
        self.weights_output_to_hidden = np.random.rand(self.hidden_nodes,self.output_nodes)

    
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return self.sigmoid(x)*(1-self.sigmoid(x))  
    
    def think(self, inputs):
        hidden_inputs = np.dot(inputs, self.weights_input_to_hidden)
        hidden_outputs = self.sigmoid(hidden_inputs)
        final_inputs = np.dot(hidden_outputs, self.weights_output_to_hidden)
        final_outputs = self.sigmoid(final_inputs)
        return hidden_outputs, final_outputs

    def train(self, inputs, targets, epochs):
        for i in range(epochs):
            # Forwardpropagation
            hidden_outputs, final_outputs = self.think(inputs)
            # Backwardpropagation
            output_errors = targets - final_outputs
            hidden_errors = np.dot(output_errors, self.weights_output_to_hidden.transpose())
            self.weights_output_to_hidden += self.learning_rate * np.dot(hidden_outputs.transpose(), output_errors * self.sigmoid_derivative(final_outputs))
            self.weights_input_to_hidden += self.learning_rate * np.dot(inputs.transpose(), hidden_errors * self.sigmoid_derivative(hidden_outputs))

    
    def predict(self, input):
        hidden_outputs, final_outputs = self.think([input])
        return final_outputs



def read_data(data_list):
    inputs = []
    targets = []
    skipfirst = False

    for data in data_list:
        if skipfirst:
            skipfirst = False
            continue
        data = data.split(',')
        inputs.append(data[1:])
        targets.append(int(data[0]))

    inputs = np.array(inputs, dtype=float)
    return inputs, np.array(targets)


def normalize(inputs):
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            if inputs[i][j] != 0:
                inputs[i][j] = inputs[i][j]/255
            else:
                inputs[i][j] = 0.01
    return inputs

def change_target_array(targets, output_n):
    target_list= []
    for target in targets:
        target_list.append([0.01 for _ in range(output_n)])
        target_list[-1][target] = 0.99 
    return np.array(target_list)


n = FeedForwardNetwork(784, 200, 10, 0.1)

def softmax(predictions):
    return np.exp(predictions)/np.sum(np.exp(predictions), axis=1, keepdims=True)   


if __name__ == "__main__":
    trainfile = "mnist_train_full.csv"
    testfile = "mnist_test_full.csv"
    showimages = False
    
    
    
    training_data_file = open(trainfile, 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()

    test_data_file = open(testfile, 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()

    inputs, targets = read_data(training_data_list)
    targets = change_target_array(targets, 10)
    test_inputs, test_targets = read_data(test_data_list)
    
    
    
    trainlen = len(inputs)
    n.train(normalize(inputs[:trainlen]), targets[:trainlen], 500)

    csvlen =len(test_inputs)
    correct = 0
    for i in range(csvlen):
        if (showimages == True):
            print("plotting image: ")
            image_array = np.asfarray(test_inputs[i]).reshape((28,28))
            plt.imshow(image_array,cmap='Greys', interpolation='None')
            plt.show(block = True)
        
        
        predicted= np.argmax(n.predict(normalize([test_inputs[i]])))
        print("Predicted number:", predicted , "Correct number:", test_targets[i])
        correct += 1 if predicted == test_targets[i] else 0
        
    print("Accuracy: ", correct/csvlen*100, "%")




