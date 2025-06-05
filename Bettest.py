import random
import matplotlib.pyplot as plt

def bet(bet_size):
    if random.random() > 0.5:
        return bet_size * 3
    else:
        return 0

def run_a_test(stack_percentage, number_of_tests):
    result_list = []
    for i in range(number_of_tests):
        starting_stack = 100
        for j in range(100):
            starting_stack -= stack_percentage * starting_stack
            starting_stack += bet(stack_percentage * starting_stack)
        result_list.append(starting_stack)

    return sum(result_list) / number_of_tests

# Running the tests
all_results = []
stack_percentages = []
for i in range(1001):
    stack_percentage = i / 1000
    all_results.append(run_a_test(stack_percentage, 10000))
    stack_percentages.append(stack_percentage)

# Plotting the histogram
plt.figure(figsize=(10,6))
plt.bar(stack_percentages, all_results, width=0.001)
plt.xlabel('Stack Percentage')
plt.ylabel('Average Stack Value after 100 Iterations')
plt.title('Stack Value vs. Stack Percentage')
plt.grid(True)
plt.show()
