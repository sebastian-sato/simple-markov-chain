import random

# Initialize markov chain
chain = {}

# Read training data
with open("./alice-in-wonderland.txt", 'r') as f:
    raw_txt = f.read()

# Format
formatted_txt = ""
for char in raw_txt:
    if char.isalnum() or char == " ":
        formatted_txt += char.lower()
    elif char == "\n" or char == "-":
        formatted_txt += " "

# Tokenize
split = formatted_txt.split(" ")
# Remove empty strings
tokenized = []
for word in split:
    if word != "":
        tokenized.append(word)
tokens = set()
for token in tokenized:
    tokens.add(token)

# Train
for i in range(len(tokenized)-1):
    token = tokenized[i]
    next_token = tokenized[i+1]
    if token not in chain:
        chain[token] = {}
    if next_token not in chain[token]:
        chain[token][next_token] = 0
    chain[token][next_token] += 1

# Save the chain
import json
with open("./chain.json","w+") as f:
    json.dump(chain, f) 
