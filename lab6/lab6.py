
from itertools import product

def truth_table_entailment():

    print("P Q R | Q->P | P->~Q | QvR | KB")

    models = []

    # Generate all possible truth assignments
    for P, Q, R in product([True, False], repeat=3):

        s1 = (not Q) or P
        s2 = (not P) or (not Q)
        s3 = Q or R

        KB = s1 and s2 and s3

        print(P, Q, R, "|", s1, "|", s2, "|", s3, "|", KB)

        if KB:
            models.append((P, Q, R))

    # Check query entailment
    query1 = all(R for P, Q, R in models)

    query2 = all((not R) or P for P, Q, R in models)

    query3 = all((not Q) or R for P, Q, R in models)

    print("\nModels of KB:", models)

    print("\nKB entails R:", query1)
    print("KB entails R -> P:", query2)
    print("KB entails Q -> R:", query3)


truth_table_entailment()
