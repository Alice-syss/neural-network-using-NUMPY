# Neural Network from Scratch — NumPy only

Built a fully functional neural network using nothing but NumPy. No PyTorch, no TensorFlow, no ML libraries. Just matrix math and Python.

## What this is


- **Forward pass** — data flows through layers as dot products + activation functions
- **Backpropagation** — error flows backwards using the chain rule to calculate gradients
- **Gradient descent** — weights update every loop, stepping downhill toward the correct answer
- **Loss function** — binary cross-entropy measures how wrong the network is after each prediction

## The problem — XOR

XOR is the classic test for neural networks because it cannot be solved by a single neuron. A straight line cannot separate the correct answers. You need at least one hidden layer — multiple neurons drawing multiple lines that together form a boundary.

| Input 1 | Input 2 | Correct answer |
|---------|---------|----------------|
| 0       | 0       | 0              |
| 0       | 1       | 1              |
| 1       | 0       | 1              |
| 1       | 1       | 0              |

## Results

After 5000 training loops, the network solves XOR perfectly:
