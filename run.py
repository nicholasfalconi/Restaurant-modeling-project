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
    def __init__(self, price_opt, diet_opt, dine_opt,distance):
        self.userprice = price_opt
        self.userdiet = diet_opt
        self.userdine_opt = dine_opt
        self.distance = distance

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

#Users option selection

#Restaurant

def priceConstraint(restaurant,customer):
      if customer.userPrice == "low":
        if restaurant.price == "low":
            return low & ~med & ~high
        else:
            return low & ~med & ~high & ~low

    if customer.userPrice == "med":
        if restaurant.price == "med":
            return low & ~med & ~high
        else:
            return med & ~high & ~low

    if customer.userPrice == "high":
        if restaurant.price == "high":
            return low & ~med & ~high
        else:
            return low & ~med & ~high & ~low

def glutenConstraint(restaurant,customer):

def lactoseConstraint(restaurant,customer):

def veganConstraint(restaurant,customer):

def vegetarianConstraint(restaurant,customer):

def dineInConstraint(restaurant,customer):

def takeOutConstraint(restaurant,customer):

def deliveryConstraint(restaurant,customer):

def distanceConstraint(restaurant,customer):

def example_theory(restaurant,customer):
    
    r = restaurant
    E = Encoding()

    E.add_constraint(priceConstraint(r) | dineInConstraint(r) | takeOutConstraint(r) | deliveryConstraint(r) | distanceConstraint(r) | glutenConstraint(r) | lactoseConstraint(r) | veganConstraint(r) | vegetarianConstraint(r))

    return E

        


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

        diet = []
        if 1 in user_selected_restrictions:
            diet.append('vegan')
        elif 2 in user_selected_restrictions:
            diet.append('vegetarian')
        elif 3 in user_selected_restrictions:
            diet.append('gluten')
        elif 4 in user_selected_restrictions:
            diet.append('lactose')

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
        user = customer(price, diet, user_dine_option, distance)
        
        # Need to iterate through the list and find which restaurants match with the users preference
        # using the example theory function. Use T.solve to find the solution to the users preferences and then match with
        # restaurants that match up

        # T = example_theory(user)
        # dictionary with the mappings of the solution
        # examplesolution = T.solve()



        for entry in restaurant_list:
            # iterating through each restaurant
            retaurant = example_theory(entry,user)
            entry.is_satisfiable()
            [] = entry.count_solutions()

'''
Haven't implemented this w/ our variables
    print("\nVariable likelihoods:")
    
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        print(" %s: %.2f" % (vn, T.likelihood(v)))
    print()
'''