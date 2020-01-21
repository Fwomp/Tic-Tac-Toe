import numpy as np

def sigmoid(x):
	return 1.0 / (1+np.exp(-x))

def sigmoid_derivative(x):
	return x * (1.0 - x)

class NeuralNetwork:
	def __init__(self, x, y):
			self.input		= x
			self.weights1	= np.random.rand(self.input.shape[1],9)
			self.weights2	= np.random.rand(9,1)
			self.y			= y
			self.output		= np.zeros(self.y.shape)

	# Feed foreward function to calculate the output, using:
	# y^ = sigmoid(W2 * sigmoid(W1 * x + b1) + b2)
	# Note: For simplicity, we have assumed the biases to be 0
	def feedforward(self):
		self.layer1 = sigmoid(np.dot(self.input, self.weights1))
		self.output = sigmoid(np.dot(self.layer1, self.weights2))

	# Our goal in training is to find the best set of weights 
	# and biases that minimizes the loss function.
	# We cannot directly calculate the derivative of the loss
	# function with respect to the weights and biases because
	# the equation of the loss function does not contain the 
	# weights and biases. Therefore, we need the chain rule to
	# help us calculate it.

	# Note: For simplicity, this has only displayed the partial
	# derivative assuming a 1-layer Neural Network.

	# To calculate our loss function what we actually need to do
	# is create a reward/punishment system

	def backprop(self):
		# application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
		d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
		d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

		# update the weights with the derivative (slope) of the loss function
		self.weights1 += d_weights1
		self.weights2 += d_weights2