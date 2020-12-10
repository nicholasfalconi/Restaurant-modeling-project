from nnf import Var
from lib204 import Encoding
from csvReader import readCSV

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
    def __init__(self, price_opt, diet_opt, dine_opt):
        self.userprice = price_opt
        self.userdiet = diet_opt
        self.userdine_opt = dine_opt

low = Var('low')
med = Var('med')
high = Var('high')

vegetrarian = Var('vegetarian')
vegan = Var('vegan')
gluten = Var('gluten')
lactose = Var('lactose')

dine_in = Var('dine-in')
take_out = Var('take-out')
delivery = Var('delivery')

time_under_10 = Var('under 10')
time_10_to_20 = Var('10 to 20')
time_over_20 = Var('over 20')

# def example_theory(current_user):

#     # Creates variables for each restaurant

#     # Propositions
#     # price
#     # price[0] = $, price[1] = $$, price[2] = $$$
#     price = []
#     for i in range(3):
#         price.append(Var(f"price_{i}"))

#     # diet restrictions
#     # index 0 - 3 with each index corresponding to a certain dietary restriction
#     # index 0 = gluten free, index 1 = vegan, index 2 = vegetrarian, index 3 = lactose
#     diettype = []
#     for i in range(4):
#         diettype.append(Var(f"diettype_{i}"))

#     dietrestrictions = []
#     for i in range(4):
#         dietrestrictions.append(Var(f"dietrstrct_{i}"))
    

#     # Dine-in, take-out, delivery
#     # index 0 = dine-in, index 1 = take-out, index 2 = delivery
#     dine_options = []
#     for i in range(3):
#         dine_options.append(Var(f"dine_opt_{i}"))


#     E = Encoding()

#     # this is where our theory starts

#     # price constraints
#     # must be one of $, $$, $$$
#     E.add_constraint(price[0] | price[1] | price[2])

#     # user selected $ for price
#     if current_user.userprice == 3:
#         E.add_constraint((price[0] & price[1]).negate())
#     # user selected $$ for price
#     elif current_user.userprice == 2:
#         E.add_constraint((price[0] & price[2]).negate())
#     # user selected $$$ for price
#     elif current_user.userprice == 1:
#         E.add_constraint((price[1] & price[2]).negate())
#     # Can't be $ and $$ and $$$
#     E.add_constraint((price[0] & price[1] & price[2]).negate())

#     # diet constraints

#     # accommodate one restrictions
#     E.add_constraint(dietrestrictions[0] | dietrestrictions[1] | dietrestrictions[2] | dietrestrictions[3])
#     # accommodate all of the restrictions
#     E.add_constraint(dietrestrictions[0] & dietrestrictions[1] & dietrestrictions[2] & dietrestrictions[3])

#     # accommodate two of the restrictions
#     E.add_constraint(dietrestrictions[0] & (diettype[1] | diettype[2] | diettype[3]))
#     E.add_constraint(dietrestrictions[1] & (diettype[0] | diettype[2] | diettype[3]))
#     E.add_constraint(dietrestrictions[2] & (diettype[0] | diettype[1] | diettype[3]))
#     E.add_constraint(dietrestrictions[3] & (diettype[0] | diettype[1] | diettype[2]))

#     # accommodate three of the restrictions (Yes I know they don't go in logical order this is just what I have written down)

#     E.add_constraint(dietrestrictions[1] & dietrestrictions[3] & (diettype[0] | diettype[2]))
#     E.add_constraint(dietrestrictions[1] & dietrestrictions[0] & (diettype[3] | diettype[2]))
#     E.add_constraint(dietrestrictions[1] & dietrestrictions[2] & (diettype[3] | diettype[0]))

#     # Eating location? not too sure what to call this
#     # all three (dine-in, take-out and delivery)
#     E.add_constraint(dine_options[0] & dine_options[1] & dine_options[2])

#     # must be one
#     E.add_constraint(dine_options[0] | dine_options[1] | dine_options[2])

#     # can be two
#     E.add_constraint(dine_options[0] & (dine_options[1] | dine_options[2]))
#     E.add_constraint(dine_options[1] & (dine_options[0] | dine_options[2]))
#     E.add_constraint(dine_options[2] & (dine_options[0] | dine_options[1]))


#     return E


if __name__ == "__main__":
    # This is where we will get user input information and whatnot
    flag = True
    restaurant_list = readCSV()

    # While loop to start
    while flag:

        # creating example theory
        # T = example_theory()
        # Asking if user wants to continue or exit
        prog_exit = input('Welcome to the Queens restuarant finder! Press Q to quit or enter to continue.\n')

        # if statement to exit
        if prog_exit.lower() == 'q':
            break

        # Getting users price range information
        user_price = int(input('Please select a price range: \n 1. $ - most affordable'\
            '\n 2. $$ - intermediate \n 3. $$$ - most expensive\n'))

        # Telling user which price was selected as well as some exception handling
        if user_price in [1,2,3]:
            if user_price == 1:
                price = 'low'
                print('You selected $.')
            elif user_price == 2:
                price = 'med'
                print('You selected $$.')
            else:
                price = 'high'
                print('You selected $$$')
        else:
            print('Invalid input: Must be either option 1, 2 or 3')
        
        # Getting diet restrictions of the user
        user_restrictions_in = input('Please select the following diet restrictions '
        '(please separate by a comma if selecting multiple):'
        ' \n 1. Vegan \n 2. Vegetarian \n 3. Gluten-free \n'
        ' 4. lactose intolerant \n 5. No restrictions\n')

        # Since there is a possibility of having multiple restrictions, split into list
        user_selected_restrictions = user_restrictions_in.split(',')

        # Turning list of strings into list of integers
        for entry in range(len(user_selected_restrictions)):
            user_selected_restrictions[entry] = int(user_selected_restrictions[entry])

        if 1 in user_selected_restrictions:
            diet = 'vegan'
        elif 2 in user_selected_restrictions:
            diet = 'vegetarian'
        elif 3 in user_selected_restrictions:
            diet = 'gluten'
        elif 4 in user_selected_restrictions:
            diet = 'lactose'

        # Getting user preference for dining options
        user_dine_option = int(input('Please select a dining option: \n 1. Dine-in \n 2. Take-out\n 3. Delivery\n'))

        if user_dine_option == 1:
            dining = 'dine-in'
        elif user_dine_option == 2:
            dining = 'take-out'
        else:
            dining = 'delivery'
        # Getting user preference for distance
        user_distance_option = int(input('Please select a distance from Queens campus:'
        ' \n 1. Under 10 minutes \n 2. Between 10 and 20 minutes \n 3. Over 20 minutes\n'))

        if user_distance_option == 1:
            distance = 'under 10'
        elif user_distance_option == 2:
            distance = '10 to 20'
        else:
            distance = 'over 20'


        # Creating customer class to store information in an object for easier access
        user = customer(user_price, user_selected_restrictions, user_dine_option)
        
        # Need to iterate through the list and find which restaurants match with the users preference
        # using the example theory function. Use T.solve to find the solution to the users preferences and then match with
        # restaurants that match up

        # T = example_theory(user)
        # dictionary with the mappings of the solution
        # examplesolution = T.solve()

        for entry in restaurant_list:
            # iterating through to find which restaurant fits the solution
            print(entry.name)


        # print("\nSatisfiable: %s" % T.is_satisfiable())
        # print("# Solutions: %d" % T.count_solutions())
        # print("   Solution: %s" % T.solve())

'''
Haven't implemented this w/ our variables
    print("\nVariable likelihoods:")
    
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        print(" %s: %.2f" % (vn, T.likelihood(v)))
    print()
'''