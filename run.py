from nnf import Var
from lib204 import Encoding

'''
Customer class

Used to create a class containing the various restrictions a 
person might have with a restaurant
Paramaters:
    price: Price range being searched for
    diet: any diet restrictions
    dine_opt: preferred dining options
'''
class customer:
    def __init__(self, price, diet, dine_opt):
        self.price = price
        self.diet = diet
        self.dine_opt = dine_opt


'''
Restaurant class

Used to create a class containing information on a resaurant.
Makes it easier to track data involving each restaurant
'''
class restaurant:
    def __init__(self):
        # Need more info on whats going to be passed to make sure its all good
        pass

'''
Have this here for reference, I know it is not how its supposed to work using this lib

# Propositions
# price
price = []
for i in range(3):
    price.append(Var(f"price_{i}"))

# diet restrictions
# index 0 - 3 with each index corresponding to a certain dietary restriction
# index 0 = gluten free, index 1 = vegan, index 2 = vegetrarian, index 3 = lactose
diettype = []
for i in range(4):
    diettype.append(Var(f"diettype_{i}"))

dietrestrictions = []
for i in range(4):
    dietrestrictions.append(Var(f"dietrstrct_{i}"))

# Dine-in, take-out, delivery
# index 0 = dine-in, index 1 = take-out, index 2 = delivery
dine_options = []
for i in range(3):
    dine_options.append(Var(f"dine_opt_{i}"))
'''

def example_theory():
    E = Encoding()

    # this is where our theory starts

    # price constraints
    # pretty self explanitory
    E.add_constraint(price[0] | price[1] | price[2])
    E.add_constraint((price[0] & price[1]).negate())
    E.add_constraint((price[0] & price[2]).negate())
    E.add_constraint((price[1] & price[2]).negate())
    E.add_constraint((price[0] & price[1] & price[2]).negate())

    # diet constraints

    # accommodate one restrictions
    E.add_constraint(dietrestrictions[0] | dietrestrictions[1] | dietrestrictions[2] | dietrestrictions[3])
    # accommodate all of the restrictions
    E.add_constraint(dietrestrictions[0] & dietrestrictions[1] & dietrestrictions[2] & dietrestrictions[3])

    # accommodate two of the restrictions
    E.add_constraint(dietrestrictions[0] & (diettype[1] | diettype[2] | diettype[3]))
    E.add_constraint(dietrestrictions[1] & (diettype[0] | diettype[2] | diettype[3]))
    E.add_constraint(dietrestrictions[2] & (diettype[0] | diettype[1] | diettype[3]))
    E.add_constraint(dietrestrictions[3] & (diettype[0] | diettype[1] | diettype[2]))

    # accommodate three of the restrictions (Yes I know they don't go in logical order this is just what I have written down)
    # accommodate three of the restrictions (Yes I know they don't go in logical order this is just what I have written down)
    E.add_constraint(dietrestrictions[1] & dietrestrictions[3] & (diettype[0] | diettype[2]))
    E.add_constraint(dietrestrictions[1] & dietrestrictions[0] & (diettype[3] | diettype[2]))
    E.add_constraint(dietrestrictions[1] & dietrestrictions[2] & (diettype[3] | diettype[0]))

    # Eating location? not too sure what to call this
    # all three (dine-in, take-out and delivery)
    E.add_constraint(dine_options[0] & dine_options[1] & dine_options[2])

    # must be one
    E.add_constraint(dine_options[0] | dine_options[1] | dine_options[2])

    # can be two
    E.add_constraint(dine_options[0] & (dine_options[1] | dine_options[2]))
    E.add_constraint(dine_options[1] & (dine_options[0] | dine_options[2]))
    E.add_constraint(dine_options[2] & (dine_options[0] | dine_options[1]))


    return E


if __name__ == "__main__":
    # This is where we will get user input information and whatnot

    T = example_theory()

    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    print("   Solution: %s" % T.solve())

'''
Haven't implemented this w/ our variables
    print("\nVariable likelihoods:")
    
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        print(" %s: %.2f" % (vn, T.likelihood(v)))
    print()
'''