# The Flippant Juror
# A three-man jury has two members each of whom independently has
# probability p of making the correct decision and a third member
# who flips a coin for each decision (majority rules). A one-man
# jury has probability p of making the correct decision. Which jury
# has the better probability of making the correct decision?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 3

import random

def flippant_juror():
    samples = 1000000
    correct = 0

    P = 0.2

    for i in range(samples):
        juror1 = random.random() < P
        juror2 = random.random() < P
        juror3 = random.random() < 0.5

        # check to see if two out of three jurors came
        # up with the "correct" decision (True).
        decision = juror1 if (juror1 == juror2) else juror3
        if decision:
            correct += 1

    average = correct / samples
    print("One-person jury probability:", P)
    print("Three-person jury probability:", average)


if __name__ == '__main__':
    flippant_juror()
