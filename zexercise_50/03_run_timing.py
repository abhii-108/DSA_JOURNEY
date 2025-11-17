from decimal import Decimal

def run_timing():
    
    number_of_runs = 0 
    total_time = 0 

    while True:

        one_run = input('Enter 10km runtime..! ')

        if not one_run:
            break 

        number_of_runs += 1

        total_time += float(one_run)

        average_time = (total_time/number_of_runs)

    print(f'Average time is {average_time:.2f}, over {number_of_runs} runs..! ')


run_timing()

def decimal_add(first, second):
    """Accepts two strings, turns them into decimals, and returns a float
representing the sum of these two.
"""
    return float(Decimal(first) + Decimal(second))

print(decimal_add('10.10123','20.123'))