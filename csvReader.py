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
        # Need more info on whats going to be passed to make sure its all good


def readCSV(): 
    
    restaurants = []

    with open('restaurants.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        # header = next(csv_reader)
        # Check file as empty
            # Iterate over each row after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            # print(row)
            diet_sel = [row[2],row[3],row[4],row[5]]
            dine_sel = [row[6],row[7],row[8]]
            time_sel = [row[9],row[10],row[11]]
            restaurants.append(restaurant(row[0],row[1], diet_sel,dine_sel,time_sel))
    return restaurants

if __name__ == "__main__":
    readCSV()