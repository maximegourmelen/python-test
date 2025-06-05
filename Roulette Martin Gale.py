import random
import matplotlib.pyplot as plt

def bet():
    roulette = random.randint(0, 36)
    if roulette <= 13:
        return 0
    else:
        return 1
    

def run_test(n_of_tests, number_of_mg_rounds, starting_stack, bet_size):

    for i in range(n_of_tests):
        stack = starting_stack
        test_list = []
        for j in range(number_of_mg_rounds):
            round_stack = stack
            while True:
                n=1
                round_bet = bet()
                if round_bet == 0:
                    round_stack -= bet_size*n
                    n+=1
                else:
                    round_stack += bet_size*n
                    break
            test_list.append()

            stack += bet(bet_size) - bet_size
