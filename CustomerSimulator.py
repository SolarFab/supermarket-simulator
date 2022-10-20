from MovementCalculator import MovementCalculator
import numpy as np
import pandas as pd
from faker import Faker

class Customer:
    """
    Simulates a single customer that moves through the supermarket
    in a MCMC simulation
    - assigns a random name to customer
    - assings a starting location based on the calculated probabilities
    - assings the transition matrix to the customer
    - calculates the next location
    """
    ...
    def __init__(self):
        self.name = ""
        #self.customer_id = customer_id
        self.location = ""
        self.matrix = []
        self.initialize()

    def initialize(self):
        self.initialize_name()
        self.initialize_start_location()
        self.initialize_trans_matrix()
    
    def initialize_name(self):
        """
        Creates a random name for the customer
        """
        ### Gives customer a name
        f = Faker()
        self.name = f.name()
    
    def initialize_start_location(self):
        """
        This method defines the starting location of the customer and assigns it as an attribute: self_location
        """
        ### Defines the starting locaiton of the customer
        m = MovementCalculator()  #initiates the Class
        starting_prob = m.calc_starting_prob() #receives a list with the probabilities at which location to start
        start_location = np.random.choice(["dairy","drinks","fruit","spices"], size=1, p=starting_prob)[0] #return the start_location
        self.location = start_location
        #print(f"{self.name} starts: ", self.location)

    def initialize_trans_matrix(self):
        """
        This method loads the trans_matrix from the class SupermarketCalculator
        and assigns it as an attribute: self.matrix
        """
        ### Assign the trans_matrix as a attribute to the customer
        m = MovementCalculator() #initiates the class
        trans_matrix = m.calc_trans_matrix() #calls the trans_matrix
        self.matrix = trans_matrix

    def next_location(self):
        """
        This function calculates the next location of the customer
        based on his current location and the transition matrix
         
        """
        prob_next_location = self.matrix.loc[self.location].to_list() #creates a list with probabilities. Normaly current location should be the input
        next_location = np.random.choice(["checkout","dairy","drinks","fruit","spices"], size=1, p=prob_next_location)[0] #randomly returns the next_location based on probability
        self.location = next_location
        


