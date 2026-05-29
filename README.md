# simple-markov-chain
A very simple implementation of a unigram Markov chain.

To use, simply run **create-markov-chain.py** and then **run-markov-chain.py** in the same directory, along with the training data (In this case I used Alice in Wonderland, sourced from Project Gutenberg).

A Markov chain can be thought of as a kind of single layer neural network (aka a perceptron) for text generation that has a "context window" of exactly one token. Though they are really in a different category of machine learning altogether.

While the capabilities of a Markov chain are obviously quite limited, they are surprisingly capable given their incredible simplicity, able to generate pseudo-realistic (but meaningless) text that looks convincing from a distance.

They can be trained on other kinds of data to. In general terms, the purpose of a Markov chain is to model any kind of process where context prior to the current state doesn't matter.

Markov chains can be extended into n-gram chains that _do_ consider a limited amount of context in their predictions (but without the ability to generalize like neural networks can), although this implementation is a simple unigram chain that does not consider any context other than the current word.
