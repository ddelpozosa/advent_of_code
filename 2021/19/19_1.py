from itertools import permutations, product

values = [1, 2, 3]
def plusAndMinusPermutations(items):
    for p in permutations(items):
        for signs in product([-1,1], repeat=len(items)):
            yield [a*sign for a,sign in zip(p,signs)]
perms = list(plusAndMinusPermutations(values))

print(len(a))