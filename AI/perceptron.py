import numpy as np

# Define input vectors X1, X2, X3
X1 = np.array([1, -2, 0, -1])
X2 = np.array([0, 1.5, -0.5, -1])
X3 = np.array([-1, 1, 0.5, -1])

X = [X1, X2, X3]

# Initialize weight vector W
W = np.array([1, -1, 0, 0.5])

# Define target outputs (desired classes) for the training examples
d = [-1, -1, 1]

# Set learning rate (step size)
c = 0.1

# Number of training epochs
epochs = 2

for epoch in range(epochs):
    print(f"Epoch {epoch + 1}: ")
    # Iterate through each training example
    for idx, x in enumerate(X):
        # Compute the net input to the perceptron (dot product)
        net = np.dot(x, W)

        # Activation function (Sign function)
        output = np.sign(net)

        # Perceptron learning rule
        error = d[idx] - output
        dW = c * error * x
        W += dW

        print(f"Weight after iteration {idx + 1}: {W}")

print("Final Weight after", epochs, "epochs:", W)
