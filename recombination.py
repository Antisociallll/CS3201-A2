
import random

# cut-and-crossfill crossover for permutations
def permutation_cut_and_crossfill (parent1, parent2):
    
    offspring1 = []
    offspring2 = []
    
    # student code begin

    """
        random a cut point:
        12345678
        _|
        _______|    <= largest range(not include cut-point itself)
        01234567    cut fragment from parent[0] to parent[4]
        
        slice a layout to [ parent_a + parent_b ]
        
    """
    cut_point = random.randint(1, 7)

    p1a = parent1[:cut_point]
    p1b = parent1[cut_point:]
    p2a = parent2[:cut_point]
    p2b = parent2[cut_point:]

    offspring1 = p1a + p2b
    offspring2 = p2a + p1b

    """
    print(p1a, p1b)
    print(p2a, p2b)
    """

    return offspring1, offspring2


"""
    test here
"""
"""
parent = [2, 8, 5, 7, 1, 4, 3, 6]

print( parent[:4] )
print( parent[4:] )
# print( [1, 2, 3, 4] - [2, 3] )

p1b_diff_p2a = [2, 6, 4, 7, 8]

for num in [8, 7, 6] :
    if num in p1b_diff_p2a :
        p1b_diff_p2a.remove(num)

print(p1b_diff_p2a)
"""