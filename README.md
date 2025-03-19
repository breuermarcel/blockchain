# Simple Blockchain in Python

## 📖 About the Project

This project is a simple implementation of a blockchain written in Python. It was created as a learning exercise to understand how blockchains work at their core.

The blockchain supports:

- Creating and adding new blocks
- Proof of Work (PoW) algorithm
- Verifying the validity of the blockchain
- A minimal Flask-based API with endpoints for mining and viewing the chain

## 🛠 Requirements

- Python 3
- pip
- Flask

## 📦 Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the Flask app:

```bash
python blockchain.py
```

The script will automatically start a local Flask server if run directly.

2. Available endpoints:

- **/mine_block** — Mines a new block and adds it to the chain
- **/get_chain** — Returns the current blockchain

## ✅ Endpoints Example

### Mine a block

```
GET http://127.0.0.1:5000/mine_block
```

### Get the blockchain

```
GET http://127.0.0.1:5000/get_chain
```

The `/get_chain` endpoint also returns a validity check for the current blockchain.

## 📚 Key Concepts Illustrated

- Block structure with index, timestamp, proof, and previous hash
- Hashing and linking blocks
- Proof-of-Work for block validation
- Chain validation
- JSON-formatted block output using Python dataclasses
