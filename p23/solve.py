import prime
MAX = 28124
prime._refresh(MAX/2)
abundants = [n for n in range(1, MAX) if sum(prime.all_factors(n)) > n+n]
abundants_dict = dict.fromkeys(abundants, 1)
total = 0
for n in range(1, MAX):
    sum_of_abundants = 0
    for a in abundants:
        if a > n: break
        if abundants_dict.get(n - a):
            sum_of_abundants = 1
            break
    if not sum_of_abundants:
        total = total + n
print(total)