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

vegetarian = Var('vegetarian')
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
    if customer.userprice == "low":
        if restaurant.price == "low":
            return low & ~med & ~high
        else:
            return low & ~med & ~high & ~low

    if customer.userprice == "med":
        if restaurant.price == "med":
            return med & ~high
        else:
            return med & ~high & ~high

    if customer.userprice == "high":
        if restaurant.price == "high":
            return high
        else:
            return ~high

def glutenConstraint(restaurant,customer):
    if 'gluten' in customer.userdiet:
        if restaurant.diet[2] == 'TRUE':
            return gluten
    else:
        return False

def lactoseConstraint(restaurant,customer):
    if 'lactose' in customer.userdiet:
        if restaurant.diet[3] == 'TRUE':
            return lactose
    else:
        return ~lactose
def veganConstraint(restaurant,customer):
    if 'vegan' in customer.userdiet:
        if restaurant.diet[0] == 'TRUE':
            return vegan
    else:
        return ~vegan
def vegetarianConstraint(restaurant,customer):
    if 'vegeterian' in customer.userdiet:
        if restaurant.diet[1] == 'TRUE':
            return vegetarian
    else:
        return ~vegetarian

def dineInConstraint(restaurant,customer):
    if customer.userdine_opt == 'dine-in':
        if restaurant.delivery[0] == 'TRUE':
            return dine_in & ~take_out & ~delivery
        else:
            return dine_in & ~dine_in

def takeOutConstraint(restaurant,customer):
    if customer.userdine_opt == 'take-out':
        if restaurant.delivery[1] == 'TRUE':
            return take_out & ~dine_in & ~delivery
        else:
            return take_out & ~take_out

def deliveryConstraint(restaurant,customer):
    if customer.userdine_opt == 'delivery':
        if restaurant.delivery[2] == 'TRUE':
            return delivery & ~take_out & ~dine_in
        else:
            return delivery & ~delivery

def distanceConstraint(restaurant,customer):
    if customer.distance == 'under 10':
        if restaurant.distance[0] == 'TRUE':
            return time_under_10 & ~time_10_to_20 & ~time_over_20
        else:
            return time_under_10 & ~time_under_10

    if customer.distance == '10 to 20':
        if restaurant.distance[1] == 'TRUE':
            return time_10_to_20 & ~time_under_10 & ~time_over_20
        else:
            return time_10_to_20 & ~time_10_to_20

    if customer.distance == 'over 20':
        if restaurant.distance[2] == 'TRUE':
            return time_over_20 & ~time_10_to_20 & ~time_under_10
        else:
            return time_over_20 & ~time_over_20

def example_theory(restaurant,customer):
    
    r = restaurant
    c = customer
    E = Encoding()

    E.add_constraint(priceConstraint(r,c) | dineInConstraint(r,c) | takeOutConstraint(r,c) | deliveryConstraint(r,c) | distanceConstraint(r,c) | glutenConstraint(r,c) | lactoseConstraint(r,c) | veganConstraint(r,c) | vegetarianConstraint(r,c))

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

        scores = {}
        finalListR = []
        for entry in restaurant_list:
            # iterating through each restaurant
            current_restaurant = example_theory(entry,user)
            # current_restaurant.is_satisfiable()
            scores[entry.name] = current_restaurant.count_solutions()

        
        for key, value in scores.items():
            print(key, ' : ', value)
