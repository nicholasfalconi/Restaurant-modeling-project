"""
Nicholas Falconi
Lizzy Klosa
Kaitlyn hung
Alex baldassare

CISC 204
Modelling project
Wed december 9th 2020
Professor Muise
"""

#Import
from nnf import Var
from nnf import Or
import nnf
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

#Defining variables for encoding

#Price point variables
low = Var('low')
med = Var('med')
high = Var('high')

#Dietary restriction food options variables
vegetarian = Var('vegetarian')
vegan = Var('vegan')
gluten = Var('gluten')
lactose = Var('lactose')

#Dining variables
dine_in = Var('dine-in')
take_out = Var('take-out')
delivery = Var('delivery')

#Distance variables
time_under_10 = Var('under 10')
time_10_to_20 = Var('10 to 20')
time_over_20 = Var('over 20')


#Constraints

"""
If the user selected a price constraint and it matches 
$,$$,$$$. If the restaurant matches the price point then
the constraint will get returned so that its only holds true 
for that instance.

Parameters: Restaurant object, Customer object
Returns: A price constraint
"""
def price_constraint(restaurant,customer):
    
    #For low price point
    if "low" in customer.userprice:
        if restaurant.price == "$":
            return low & ~med & ~high
        else:
            return low & ~low

    #For the med price point
    if "med" in customer.userprice:
        if restaurant.price == "$$":
            return med & ~high & ~low
        else:
            return med & ~med

    #For the high price point
    if "high" in customer.userprice:
        if restaurant.price == "$$$":
            return high & ~low & ~med
        else:
            return high & ~high

"""
If the user selected a single dietary restriction the
appropriate constraint will get returned so it only 
holds true for that instance.

Parameters: Restaurant object, Customer object
Returns: A single dietary restriction constraint
"""
def single_diet_constraint(restaurant, customer):
    
    #For gluten free 
    if 'gluten' in customer.userdiet:
        if 'TRUE' in restaurant.diet[2]:
            return gluten & ~vegan & ~vegetarian & ~lactose
        else:
            return ~gluten & gluten

    #For lactose
    elif 'lactose' in customer.userdiet:
        if 'TRUE' in restaurant.diet[3]:
            return ~gluten & ~vegan & ~vegetarian & lactose
        else:
            return ~lactose & lactose

    #For vegetarian
    elif 'vegetarian' in customer.userdiet:
        if 'TRUE' in restaurant.diet[1]:
            return ~gluten & ~vegan & vegetarian & ~lactose
        else:
            return ~vegetarian & vegetarian

    #For vegan
    elif 'vegan' in customer.userdiet:
        if 'TRUE' in restaurant.diet[0]:
            return ~gluten & vegan & ~vegetarian & ~lactose
        else:
            return ~vegan & vegan

"""If the user selected two dietary restrictions the 
appropriate constrain will get returned so it only 
holds true for that instance 

Parameters: Restaurant object, Customer object
Returns: A single two dietary restriction constraint
"""
def two_diet_constraint(restaurant, customer):
    
    #For vegetarian and vegan customers
    if ('vegetarian' in customer.userdiet) and ('vegan' in customer.userdiet):
        if ('TRUE' in restaurant.diet[0]) and ('TRUE' in restaurant.diet[1]):
            return vegetarian & vegan & ~lactose & ~gluten
        else: 
            return vegetarian & ~vegetarian
    
    #For vegan and lactose free customers
    elif ('vegan' in customer.userdiet) and ('lactose' in customer.userdiet): 
        if ('TRUE' in restaurant.diet[0]) and ('TRUE' in restaurant.diet[3]):
            return ~vegetarian & vegan & lactose & ~gluten
        else: 
            return vegan & ~vegan

    #For vegetarian and gluten free customers
    elif ('vegan' in customer.userdiet) and ('gluten' in customer.userdiet): 
        if ('TRUE' in restaurant.diet[0]) and ('TRUE' in restaurant.diet[2]):
            return ~vegetarian & vegan & ~lactose & gluten
        else: 
            return vegan & ~vegan
    #For gluten free and lactose free customers
    elif ('gluten' in customer.userdiet) and ('lactose' in customer.userdiet): 
        if ('TRUE' in restaurant.diet[2]) and ('TRUE' in restaurant.diet[3]):
            return ~vegetarian & ~vegan & lactose & gluten
        else: 
            return gluten & ~gluten

    #For gluten free and vegitarian customers
    elif ('gluten' in customer.userdiet) and ('vegitarian' in customer.userdiet): 
        if ('TRUE' in restaurant.diet[2]) and ('TRUE' in restaurant.diet[1]):
            return vegetarian & ~vegan & ~lactose & gluten
        else: 
            return gluten & ~gluten
    #For lactose free and vegetarian customers
    elif ('lactose' in customer.userdiet) and ('vegitarian' in customer.userdiet): 
        if ('TRUE' in restaurant.diet[1]) and ('TRUE' in restaurant.diet[1]):
            return vegetarian & ~vegan & lactose & ~gluten
        else: 
            return lactose & ~lactose


"""If the user selected three dietary restrictions the 
appropriate constrain will get returned so it only 
holds true for that instance 

Parameters: Restaurant object, Customer object
Returns: a single three dietary constraint
"""
def three_diet_constraint(restaurant,customer):

    # For vegetarian and vegan and gluten free customers
    if ('vegetarian' in customer.userdiet) and ('vegan' in customer.userdiet) and ('gluten' in customer.userdiet):
        if ('TRUE' in restaurant.diet[0]) and ('TRUE' in restaurant.diet[1]) and ('TRUE' in restaurant.diet[2]):
            return vegetarian & vegan & ~lactose & gluten
        else: 
            return vegetarian & ~vegetarian

    # For vegetarian and vegan and lactose free customers
    elif ('vegetarian' in customer.userdiet) and ('vegan' in customer.userdiet) and ('lactose' in customer.userdiet):
        if ('TRUE' in restaurant.diet[0]) and ('TRUE' in restaurant.diet[1]) and ('TRUE' in restaurant.diet[3]):
            return vegetarian & vegan & lactose & ~gluten
        else: 
            return vegetarian & ~vegetarian

    # For gluten free and vegan and lactose free customers
    elif ('gluten' in customer.userdiet) and ('vegan' in customer.userdiet) and ('lactose' in customer.userdiet):
        if ('TRUE' in restaurant.diet[2]) and ('TRUE' in restaurant.diet[1]) and ('TRUE' in restaurant.diet[3]):
            return ~vegetarian & vegan & lactose & gluten
        else: 
            return vegetarian & ~vegetarian

"""If the user selected all dietary restrictions the 
appropriate constrain will get returned so it only 
holds true for that instance 

Parameters: Restaurant object, Customer object
Returns: a single all dietary constraint
"""
def all_diet_constraint(restaurant,customer):
    
    # For users that have all the dietary restrictions
    if ('vegetarian' in customer.userdiet) and ('vegan' in customer.userdiet) and ('gluten' in customer.userdiet) and ('lactose' in customer.userdiet):
        if ('TRUE' in restaurant.diet[0]) and ('TRUE' in restaurant.diet[1]) and ('TRUE' in restaurant.diet[2]) and ('TRUE' in restaurant.diet[3]):
            return vegetarian & vegan & lactose & gluten
        else: 
            return vegetarian & ~vegetarian

"""If the user selected one dining restrictions the 
appropriate constrain will get returned so it only 
holds true for that instance 

Parameters: Restaurant object, Customer object
Returns: a single dining constraint
"""
def one_dining_constraints(restaurant, customer):
    
    # For dine in customers
    if 'dine-in' in customer.userdine_opt:
        if restaurant.delivery[0] == 'TRUE':
            return dine_in
        else:
            return ~dine_in & dine_in 

    # For take out customers
    elif 'take-out' in customer.userdine_opt:
        if restaurant.delivery[1] == 'TRUE':
            return take_out
        else:
            return ~take_out & take_out

    # For delivery customers
    elif 'delivery' in customer.userdine_opt:
        if restaurant.delivery[2] == 'TRUE':
            return delivery
        else:
            return ~delivery & delivery

"""If the user selected two dining restrictions the 
appropriate constrain will get returned so it only 
holds true for that instance 

Parameters: Restaurant object, Customer object
Returns: two dining constraint
"""
def two_dining_constraints(restaurant, customer):
    
    #For users that want dine in and take out
    if ('dine-in' in customer.userdine_opt) and ('take-out' in customer.userdine_opt):
        if restaurant.delivery[0] == 'TRUE' and restaurant.delivery[1] == 'TRUE':
            return dine_in & take_out & ~delivery
        else:
            return ~dine_in & dine_in 
    #For users that want Dine in and Delivery
    elif ('dine-in' in customer.userdine_opt) and ('delivery' in customer.userdine_opt):
        if restaurant.delivery[0] == 'TRUE' and restaurant.delivery[2] == 'TRUE':
            return dine_in & ~take_out & delivery
        else:
            return ~dine_in & dine_in
    
    #For users that want Take out and Delivery
    elif ('take-out' in customer.userdine_opt) and ('delivery' in customer.userdine_opt):
        if restaurant.delivery[1] == 'TRUE' and restaurant.delivery[2] == 'TRUE':
            return ~dine_in & take_out & delivery
        else:
            return ~dine_in & dine_in

"""If the user selected all dining restrictions the 
appropriate constrain will get returned so it only 
holds true for that instance 

Parameters: Restaurant object, Customer object
Returns: all dining constraint
"""
def all_dining_constraints(restaurant, customer):
    
    # For users that want dine in, Take out and delivery
    if ('take-out' in customer.userdine_opt) and ('delivery' in customer.userdine_opt) and ('dine-in' in customer.userdine_opt):
        if restaurant.delivery[0] == 'TRUE' and restaurant.delivery[1] == 'TRUE' and restaurant.delivery[2] == 'TRUE':
            return dine_in & take_out & delivery
        else:
            return ~dine_in & dine_in 

"""If the user selected distance restrictions the 
appropriate constrain will get returned so it only 
holds true for that instance 

Parameters: Restaurant object, Customer object
Returns: distance constraint
"""
def distanceConstraint(restaurant,customer):
    
    #For customers that want under 10 to campus
    if customer.distance == 'under 10':
        if restaurant.distance[0] == 'TRUE':
            return time_under_10 & ~time_10_to_20 & ~time_over_20
        else:
            return time_under_10 & ~time_under_10

    # For customers that want 10-20 min to campus
    if customer.distance == '10 to 20':
        if restaurant.distance[1] == 'TRUE':
            return time_10_to_20 & ~time_under_10 & ~time_over_20
        else:
            return time_10_to_20 & ~time_10_to_20

    # For customers that dont mind over the distance being over 20 minutes to campus
    if customer.distance == 'over 20':
        if restaurant.distance[2] == 'TRUE':
            return time_over_20 & ~time_10_to_20 & ~time_under_10
        else:
            return time_over_20 & ~time_over_20

"""
This function is where the constraints get added to our
theory.

Parameters: Restaurant object and Customer object
"""
def example_theory(restaurant,customer):

    # Shorter variables for the objects
    r = restaurant
    c = customer

    # Defining encoding variable
    E = Encoding()

    # Add distance constraint
    E.add_constraint(distanceConstraint(r,c))
    E.add_constraint(price_constraint(r,c))

    # Add dining constraints
    if len(user.userdine_opt) == 1:
        E.add_constraint(one_dining_constraints(r,c))
    elif len(user.userdine_opt) == 2:
        E.add_constraint(two_dining_constraints(r,c))
    elif len(user.userdine_opt) == 3:
        E.add_constraint(all_dining_constraints(r,c))

    # Add Diet constraints
    if len(user.userdiet) == 1:
        if 5 in user.userdiet:
            pass
        else:
            E.add_constraint(single_diet_constraint(r,c))
    elif len(user.userdiet) == 2:
        E.add_constraint(two_diet_constraint(r,c))
    elif len(user.userdiet) == 3:
        E.add_constraint(three_diet_constraint(r,c))
    elif len(user.userdiet) == 4:
        E.add_constraint(all_diet_constraint(r,c))

    # return the Encoding variable
    return E

        

"""
Main method: Where the implementation happens. The theory gets solved 
where a sorted list from best result to worst result is displayed
to the screen. 

The user also inputs their prefrences
"""
if __name__ == "__main__":
    # This is where we will get user input information
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

        # Getting user input for dietary restrictions
        diet = []
        if 1 in user_selected_restrictions:
            diet.append('vegan')
        if 2 in user_selected_restrictions:
            diet.append('vegetarian')
        if 3 in user_selected_restrictions:
            diet.append('gluten')
        if 4 in user_selected_restrictions:
            diet.append('lactose')
        
        # Getting user preference for dining options
        user_dine_option = input('Please select a dining option. If multiple separate by a comma: \n 1. Dine-in \n 2. Take-out\n 3. Delivery\n')
        dine_in_list = user_dine_option.split(',')

        final_list = []
        if '1' in dine_in_list:
            final_list.append('dine-in')
        if '2' in dine_in_list:
            final_list.append('take-out')
        if '3' in dine_in_list:
            final_list.append('delivery')
        

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
        user = customer(price, diet, final_list, distance)
        
        # Need to iterate through the list and find which restaurants match with the users preference
        # using the example theory function. Use T.solve to find the solution to the users preferences and then match with
        # restaurants that match up

        # T = example_theory(user)
        
        # List to display results 
        finalListR = []

        # Loops through each restaurant in the csv file
        for entry in restaurant_list:
            
            # Variable for example theory method
            T = example_theory(entry, user)
        
            """ Checks if the theory is satisfiable for each restaurant.
            this is where we determine if the restaurant is a good fit 
            or not"""

            y = example_theory(entry,user).is_satisfiable()
            
            # if the theory is satified
            if y == True:
                finalListR.insert(0, entry.name)
            else:
                finalListR.insert(len(finalListR), entry.name)

        # to display all the results of restaurants best fit to worst fit
        for i in range(len(finalListR)):
            if i < 4:
                print(f"{i + 1}. %s" % finalListR[i] + '    ' + '★ ★ ★ ★ ★')
            elif i >= 4 and i < 7:
                print(f"{i + 1}. %s" % finalListR[i] + '    ' + '★ ★ ★ ★')
            elif i <= 7 and i < 11: 
                print(f"{i + 1}. %s" % finalListR[i] + '    ' + '★ ★ ★')
            elif i <= 11 and i < 15: 
                print(f"{i + 1}. %s" % finalListR[i] + '    ' + '★ ★')
            else: 
                print(f"{i + 1}. %s" % finalListR[i] + '    ' + '★')