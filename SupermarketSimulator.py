"""
Simulates the supermarket and let's customer move around the different supermarkt departments.
Creates a .csv file which tracks the movements. 
"""

import numpy as np
import pandas as pd
from CustomerSimulator import Customer
from datetime import datetime
from datetime import timedelta



class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """
    def __init__(self):        
        self.time = ""
        self.list_of_customers = [] # list of customers currently in the supermarket
        self.number_of_customers = 0
        self.csv_list = []
        
    def open_supermarket(self):
        """Initiate the supermarket
        """
        self.time = datetime.now()
        for time_step in range(40):
            self.time = self.time + timedelta(minutes=1)
            self.add_new_customers()
            self.fill_csv()
            self.checkout_customers()
            self.move_customers()
        self.save_csv()


    def add_new_customers(self):
        """randomly creates new customers.
        """
        for _ in range(np.random.randint(3)):
            customer = Customer()
            self.list_of_customers.append(customer)
        self.number_of_customers = len(self.list_of_customers)

    def move_customers(self):
        """randomly creates new customers.
        """
        for customer in self.list_of_customers:
            customer.next_location()
                 
    # def checkout_customers(self):
    #     """checks which customers are currently at checkout point and 
    #     deletes these from the list_of_customers.        
    #     """
	#     ids_to_delete = []

	#     for customer_id, customer in enumerate(self.list_of_customers):
	#     	if customer.location == 'checkout':
	#     		ids_to_delete.append(customer_id)
	#     ids_to_delete.reverse()
	#     for customer_id in ids_to_delete:
	#     	del self.list_of_customers[customer_id]

    def checkout_customers(self):
            ids_to_delete = []
            for customer_id, customer in enumerate(self.list_of_customers):
                if customer.location == 'checkout':
                    ids_to_delete.append(customer_id)
            ids_to_delete.reverse()
            for customer_id in ids_to_delete:
                #print(self.list_of_customers[customer_id])
                del self.list_of_customers[customer_id]

    def fill_csv(self):
        "Creates a csv list wich tracks the time and location of the movement of customers "
        for customer in self.list_of_customers:
            self.csv_list.append([self.time, customer.name,customer.location])
    
    def save_csv(self):
        df = pd.DataFrame(self.csv_list)
        df.to_csv("./supermarket.csv")


if __name__== "__main__":
    supermarket = Supermarket()
    supermarket.open_supermarket()
    print(supermarket)
