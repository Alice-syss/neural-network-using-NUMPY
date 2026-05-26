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

# Stock Market Analysis — Apple, Microsoft, Google

Data analysis of 40 years of stock market data using Python and pandas.

## Questions I answered

**1. How has Apple's price grown over 40 years?**
Flat from 1980–2005, then explosive growth after the iPhone launch in 2007.

**2. What were the most volatile days in Apple's history?**
The data surfaced real historical events — Black Monday 1987, the 2008 financial 
crisis, and the 2010 Flash Crash — purely from price movement numbers.

**3. If you invested $100 in 2004, what would it be worth today?**
- Apple → $17,000
- Google → $2,500  
- Microsoft → $800

## What I learned
- How to calculate volatility from raw OHLC price data
- How to normalize prices to compare stocks fairly regardless of their price
- How price data tells the story of real world events

## Stack
- Python
- pandas
- matplotlib
- NumPy

- ## Data
Download the dataset from Kaggle:
https://kaggle.com/datasets/jacksoncrow/stock-market-dataset

Place the stocks folder inside a `data/` folder in this directory.
