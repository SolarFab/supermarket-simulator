import pandas as pd
import numpy as np
import datetime

class SupermarketCalculator:

    """
    This class reflects the logic of the supermarket based on data how customers move
    around the supermarket
    1. Builds one df out of 5 daily csv files
    2. Calculates the transition matrix 
    3. Calculates the probabilities for the starting location of each customer
    """

    def __init__(self):
        self.name = ""
        self.dataframe = pd.DataFrame()
        self.get_csv()


    def get_csv(self):
        """
        - Create a single DF out of the different weekday files
        - Add checkout stamp for certain customers since when the supermarket is closing,
          some customer are not recorded as checked out. 
        - Renumber the customer_no, since all customer_no start with 1 
          again in the different daily .csv files. Customer_no will continue from the customer_no
          from the previous day.
        """

        df = pd.DataFrame()
        counter = 0
        #number_of_cust = 0
        
        # read the single .csv files by a loop
        for weekday in ["monday","tuesday","wednesday","thursday","friday"]:
            df_weekday = pd.DataFrame()
            df_weekday = pd.read_csv(f"/home/fabian/spiced_projects/student_code/week08/week_project/data/{weekday}.csv",sep = ";", index_col = 0, parse_dates=True )
            
            if weekday!="monday": #if the weekday is monday, the counter stays zero, since no data from the previous day need to be added
                df_weekday["customer_no"] =  df_weekday["customer_no"] + counter
            
            # set a counter, which counts the customers of the previous days and than adds them to currently loaded customer file.
            counter += df_weekday["customer_no"].nunique()   
            
            # Check which customer have not checkout
            df_no_dup=df_weekday.drop_duplicates(subset=['customer_no'],keep='last')
            df_no_dup = df_no_dup.loc[(df_no_dup["location"]!="checkout")]
        
            # create a DF coLumn whcih contains onLy "checkout" 
            checkout_list = []
            for i in range(0,len(df_no_dup)):
                checkout_list.append("checkout")
            checkout_list
            df_no_dup["location"] = checkout_list

            # create a list with timestamp of the date and last hour 22:00:00
            time_list = []
            for i in range(0,len(df_no_dup)):
                time_list.append(datetime.datetime.combine(df_no_dup.index[0].date(), 
                                    datetime.time(22, 0,0)))

            # resets the index of the checkout-df to the date and 22:00:00
            df_no_dup.index=time_list
        
            df_weekday = pd.concat([df_weekday,df_no_dup])
            df = pd.concat([df,df_weekday])
        self.dataframe = df
    
 

    def calc_trans_matrix(self):
        """
        Returns a transition matrix which contain the probabilities to which supermarket
        department the customer goes next based on his current location

        """
 
        self.dataframe["time"] = self.dataframe.index
        df_shifted = self.dataframe.sort_values(["customer_no","time"])
        df_shifted["next_location"] = df_shifted["location"].shift(-1)
        df_shifted=df_shifted.loc[df_shifted["location"]!="checkout"]
        df_shifted
        trans_matrix = pd.crosstab(df_shifted["location"], df_shifted["next_location"],normalize="index")
        return(trans_matrix)


    def calc_starting_prob(self):
        """
        Returns probabilities of where the customer starts in the supermarket
        """

        df_starting = self.dataframe.drop_duplicates(subset=['customer_no'],keep='first')
        df_starting = df_starting.groupby("location").count()
        df_starting["start_prob"] = df_starting["customer_no"]/df_starting["customer_no"].sum()
        df_starting = df_starting["start_prob"] 
        prob=df_starting.to_list()
        return(prob)

 
    # def import_clean_csv(self):
    #     """
    #     imports the respective weekday csv and cleans the data:
    #     - adds checkout and timestamp for customers which have not checkout

    #     """
    #     df = pd.DataFrame()
    #     counter = 0
    #     number_of_cust = 0
        
    #     # read the single .csv files by a loop
    #     for weekday in ["monday","tuesday","wednesday","thursday","friday"]:
    #         df_weekday = pd.DataFrame()
    #         df_weekday = pd.read_csv(f"./data/{weekday}.csv",sep = ";", index_col = 0, parse_dates=True )
            
    #         if weekday!="monday": #if the weekday is monday, the counter stays zero, since no data from the previous day need to be added
    #             df_weekday["customer_no"] =  df_weekday["customer_no"] + counter
            
    #         # set a counter, which counts the customers of the previous days and than adds them to currently loaded customer file.
    #         counter += df_weekday["customer_no"].nunique()   
            
    #         # Check which customer have not checkout
    #         df_no_dup=df_weekday.drop_duplicates(subset=['customer_no'],keep='last')
    #         df_no_dup = df_no_dup.loc[(df_no_dup["location"]!="checkout")]
        
    #         # create a DF coLumn whcih contains onLy "checkout" 
    #         checkout_list = []
    #         for i in range(0,len(df_no_dup)):
    #             checkout_list.append("checkout")
    #         checkout_list
    #         df_no_dup["location"] = checkout_list

    #         # create a list with timestamp of the date and last hour 22:00:00
    #         time_list = []
    #         for i in range(0,len(df_no_dup)):
    #             time_list.append(datetime.datetime.combine(df_no_dup.index[0].date(), 
    #                                 datetime.time(22, 0,0)))

    #         # resets the index of the checkout-df to the date and 22:00:00
    #         df_no_dup.index=time_list
        
    #         df_weekday = pd.concat([df_weekday,df_no_dup])
    #         df = pd.concat([df,df_weekday]) 
    #     self.df = df

