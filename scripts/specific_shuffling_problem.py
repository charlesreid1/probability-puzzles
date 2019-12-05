# A specific shuffling problem:
# Suppose you have a shuffled deck containing 13 cards. Each card has a number
# from 1 to 13 and each number appears on exactly one card. You look at the
# number on the first card — suppose it’s k — and then you reverse the order
# of the first k cards. You continue this procedure — reading the first card’s
# number and then reversing the order of the corresponding number of cards — until
# the first card reads 1. Clearly, the number of reversals depends on the initial
# order of the cards. What is the largest number of reversals that you might have to do?
# What order are the cards in before you start shuffling the maximum-reversal deck?
# Extra credit: What if the deck contains 53 cards?

# From https://fivethirtyeight.com/features/how-long-will-you-shuffle-this-damn-deck-of-cards/

import random

Niter = 10
Ncards = 13

def specific_shuffle():
    samples = 100000
    deck = list(range(1,Ncards+1))
    reversals = 0

    for i in range(samples):
        random.shuffle(deck)
        orig_deck = deck[:]
        rev = 0
        while deck[0] != 1:
            k = deck[0]
            deck[0:k] = reversed(deck[0:k])
            rev += 1
        if rev > reversals:
            reversals = rev
            print("%3d %s"%(rev, orig_deck))

    print("Maximum number of reversals:", reversals)

if __name__ == '__main__':
    for i in range(Niter):
        specific_shuffle()
