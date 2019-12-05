# The First Ace
# Shuffle an ordinary deck of 52 playing cards containing four aces.
# Then turn up cards from the top until the first ace appears.
# On the average, how many cards are required until the first ace appears?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 40

import random

def first_ace():
    Ncards = 52
    Naces = 4

    samples = 100000
    total = 0

    for i in range(samples):
        deck = [x for x in range(Ncards)]
        random.shuffle(deck)

        count = 1
        for card in deck:
            if card < Naces:
                break
            else:
                count += 1
        total += count

    average = total / samples
    print("Average number of cards until the first ace:", average)
    print("Expected position:", (Ncards+1)/(Naces+1))


if __name__ == '__main__':
    first_ace()
