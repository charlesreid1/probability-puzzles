# Curing the Compulsive Gambler
# Mr. Brown always bets a dollar on the number 13 at roulette against
# the advice of Kind Friend. To help cure Mr. Brown of playing roulette,
# Kind Friend always bets Brown $20 at even money that Brown will be
# behind at the end of 36 plays. How is the cure working?
# (Most American roulette wheels have 38 equally likely numbers.
# If the player's number comes up, he is paid 35 times his stake and
# gets his original stake back; otherwise he loses his stake.)
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 7

import random

def curing_the_compulsive_gambler():
    samples = 100000
    total = 0
    total_wins = 0
    total_brown = 0

    for i in range(samples):
        bank = 0
        wins = 0
        for j in range(36):
            spin = random.randint(1, 38)
            if spin == 13:
                bank += 35
                wins += 1
            else:
                bank -= 1

        if bank >= 0:
            bank += 20
            total_brown += 1
        else:
            bank -= 20

        total += bank
        total_wins += wins

    average = total / samples
    average_wins = total_wins / samples
    average_brown = total_brown / samples
    print("Average prob of winning after 36 spins:", average_wins)
    print("Average winnings after 36 spins:", average)
    print("Average number of times brown gets paid:", average_brown)
        

if __name__ == '__main__':
    curing_the_compulsive_gambler()
