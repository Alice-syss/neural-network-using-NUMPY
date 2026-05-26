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


# Study Buddy — AI-powered tutor built with Claude

A chatbot that actually teaches you instead of just answering your questions.
Built with the Anthropic API and Streamlit.

## What it does

- Explains any concept simply when you ask
- Quizzes you after you say you understood something
- Tells you honestly if your answer is wrong
- Remembers the full conversation so context carries through

## Why I built it

Most AI chatbots just give you the answer. This one forces you to actually learn
by testing you after every explanation. Inspired by how I actually study.

## Stack

- Python
- Anthropic API (claude-sonnet-4-20250514)
- Streamlit
- python-dotenv
