# supermarket-simulator

The goal of this project is to build a small programm which simulates the movements of customers in a supermarket.
There is a data set for each weekday which tracks the movement of customer in the supermarkt in the following format:


| timestamp  | customer_no | location |
| ------------- | ------------- | ------------- |
| 2019-09-02 07:03:00 | 1  | fruits |
| 2019-09-02 07:03:00 | 2  | dairy |

In total three python scripts have been created:

### MovementCalculator
  This file creates one big dataframe out of the 5 single weekday csv files, cleans the data and adds missing values. Further it calculates
  the probability in which department the customer starts and calculates a transition matrix, this shows the probabilities where a customer moves
  next based on his current position:
  ![image](https://user-images.githubusercontent.com/101807190/196924535-034ebd73-6c92-45ec-83e6-e2e2631c3504.png)

### CustomerSimulator
  Creates a customer class which simulates  a single customer:
    - assigns a random name to customer
    - assings a starting location based on the calculated probabilities
    - assings the transition matrix to the customer
    - calculates the next location
    
### SupermarketSimulator
  Creates a supermarket class which simulates the movement of customers in the supermarket:
    - adds new customers
    - moves around customers
    - checks out customers
    - creates a final .csv with the movement of the customers.
  
