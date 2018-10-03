import random

# mutate a permutation


def permutation_swap (individual):
    
    mutant = individual.copy()

    # student code begin

    # random two positions
    locus1 = random.randint(0, 7)
    locus2 = random.randint(0, 7)

    # swap these two positions
    temp = mutant[locus1]
    mutant[locus1] = mutant[locus2]
    mutant[locus2] = temp

    # student code end
    
    return mutant
