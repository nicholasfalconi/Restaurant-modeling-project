'''
Restaurant class

Used to create a class containing information on a resaurant.
Makes it easier to track data involving each restaurant

actually will be implemented in the csv reader so this is irrelavant
'''
import csv

class restaurant:
    def __init__(self, name, price_opt, diet_opt, delivery_opt, distance_opt):
        self.name = name
        self.price = price_opt
        self.diet = diet_opt
        self.delivery = delivery_opt
        self.distance = distance_opt


def readCSV(): 
    # Creating a list to contain restaurant objects
    restaurants = []

    # opening file to read
    with open('restaurants.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        # skip header
        next(csv_reader, None)

        # iterate through each row
        for row in csv_reader:
            # setting variables to pass to restaurant constructor
            diet_sel = [row[2],row[3],row[4],row[5]]
            dine_sel = [row[6],row[7],row[8]]
            time_sel = [row[9],row[10],row[11]]

            # Appending restaurant objects to list
            restaurants.append(restaurant(row[0],row[1], diet_sel,dine_sel,time_sel))

    # Returning list of restaurant objects
    return restaurants

# testing
if __name__ == "__main__":
    x = readCSV()

    for entry in x:
        print(entry.name)