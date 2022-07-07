
from SupermarketCalculator2 import CalcTransMatrix
from SupermarketCalculator2 import CalcStartingProb
import numpy as np
import pandas as pd

class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    ...

    def __init__(self,name):
        self.name = name
        self.location = ""
         #self.next_location = next_location
    
    def starting_location(self):
        """
        This method defines the starting location form the customer
        """

        m = CalcStartingProb  #initiates the Class
        starting_prob = m.calc_starting_prob() #receives a list with the probabilities at which location to start
        start_location = np.random.choice(["dairy","drinks","fruit","spices"], size=1, p=starting_prob)[0] #return the start_location
        self.location = start_location
        print("Customer starts: ", self.location)


    def next_location(self):
        """
        This function calls the class CalcTransMatrix to receive the trans_matrix and return the next location
         
        """
        
        m = CalcTransMatrix #initiates the class
        trans_matrix = m.calc_trans_matrix() #calls the trans_matrix
        prob_next_location = trans_matrix.loc[self.location].to_list() #creates a list with probabilities. Normaly current location should be the input
        next_location = np.random.choice(["checkout","dairy","drinks","fruit","spices"], size=1, p=prob_next_location)[0] #randomly returns the next_location based on probability
        #self.location = next_location
        print("next location: ",next_location)
        self.location = next_location
        
        """
        This function takes the values from transition matrix to define customer behaviour.
        Depends on the weekday
        Calculating the transition matrix should 
        """

# customer1 = Customer("Heiko")
# customer2 = Customer("Stefan")

if __name__ == "__main__":
    print("xxxx")
    customer1 = Customer("Heiko")
    customer2 = Customer("Stefan")
