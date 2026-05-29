import random
import json

# Load markov chain
with open('./chain.json','r') as f:
    chain = json.load(f)

# Generate text
def query(word):
    if word not in chain:
        word = random.choice(list(chain.keys()))
    ordered_keys = list(chain[word].keys())
    ordered_probabilities = []
    for key in ordered_keys:
        ordered_probabilities.append(chain[word][key])
    # Convert the probabilities into a cumulative sum
    cumsum = [0]
    for prob in ordered_probabilities:
        cumsum.append(prob + cumsum[-1])
    cumsum.pop(0)
    # Randomly sample
    selected_index = 0
    r = random.randint(0, cumsum[-1])
    for index, value in enumerate(cumsum):
        if r <= value:
            selected_index = index
            break
    selected_word = ordered_keys[selected_index]
    return selected_word

# Inference
generated = ["the"] # Arbitrary choice of an initial token
for i in range(1000):
    generated_token = query(generated[-1])
    generated.append(generated_token)
print(' '.join(generated))
