from nnf import Var
from lib204 import Encoding

# Variables for our 
# price
price = []
for i in range(2):
    price.append(Var(f"price_{i}"))

# index 0 - 3 with each index corresponding to a certain dietary restriction
dietrestrictions = []
for i in range(3):
    dietrestrictions.append(Var(f"dietrstrct_{i}"))

#
# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    E = Encoding()
    # reference for my peanut brain
    # E.add_constraint(a | b)
    # E.add_constraint(~a | ~x)
    # E.add_constraint(c | y | z)

    # this is where our theory starts

    # price constraints
    E.add_constraint(price[0] | price[1] | price[2])
    E.add_constraint((price[0] & price[1]).negate())
    E.add_constraint((price[0] & price[2]).negate())
    E.add_constraint((price[1] & price[2]).negate())
    E.add_constraint((price[0] & price[1] & price[2]).negate())

    # diet constraints
    E.add_constraint(dietrestrictions[0] | dietrestrictions[1] | dietrestrictions[2] | dietrestrictions[3])
    E.add_constraint((dietrestrictions[1] & dietrestrictions[2]).negate())
    E.add_constraint((dietrestrictions[2] & dietrestrictions[3]).negate())
    E.add_constraint((dietrestrictions[0] & dietrestrictions[1]).negate())

    

    return E


if __name__ == "__main__":

    T = example_theory()

    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        print(" %s: %.2f" % (vn, T.likelihood(v)))
    print()
