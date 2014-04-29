import math

def digit_factorial_chains(n=1000000):
    number_of_chains = 0
    for i in range(1, n):
        if chains_length(i) == 60:
            number_of_chains += 1

    return number_of_chains
        

def sum_of_factorial(number):
    return sum(math.factorial(int(i)) for i in str(number))

def chains_length(number):
    chains = set()
    chains.add(number)
    t = number
    while True:
        t = sum_of_factorial(t)
        if t not in chains:
            chains.add(t)
        else:
            break
    return len(chains)

if __name__ == "__main__":
    print(digit_factorial_chains())