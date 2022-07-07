import pandas as pd
import numpy as np
import datetime

class SupermarketCalculator:
    """
    Contains two methods:
    1. Calculates the transition matrix for each day
    2. Calculates the probabilities for the starting location for each day
    """

    def __init__(self):
        self.name = weekday
        self.transition_matrix = pd.DataFrame()
        self.df = pd.DataFrame()
 

    def calc_trans_matrix():
        """
        imports the respective weekday csv and cleans the data:
        - adds checkout and timestamp for customers which have not checkout

        """
        df = pd.DataFrame()
        counter = 0
        number_of_cust = 0
        
        # read the single .csv files by a loop
        for weekday in ["monday","tuesday","wednesday","thursday","friday"]:
            df_weekday = pd.DataFrame()
            df_weekday = pd.read_csv(f"../data/{weekday}.csv",sep = ";", index_col = 0, parse_dates=True )
            
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
        #print(counter)
        #self.df = df
        df["time"] = df.index
        df_shifted = df.sort_values(["customer_no","time"])
        df_shifted["next_location"] = df_shifted["location"].shift(-1)
        df_shifted=df_shifted.loc[df_shifted["location"]!="checkout"]
        df_shifted
        ### Create transition  matrix
        # create transition matrix between Location and next_Location
        trans_matrix = pd.crosstab(df_shifted["location"], df_shifted["next_location"],normalize="index")
        print(trans_matrix)

    def calc_starting_prob():
        """
        imports the respective weekday csv and cleans the data:
        - adds checkout and timestamp for customers which have not checkout

        """
        df = pd.DataFrame()
        counter = 0
        number_of_cust = 0
        
        # read the single .csv files by a loop
        for weekday in ["monday","tuesday","wednesday","thursday","friday"]:
            df_weekday = pd.DataFrame()
            df_weekday = pd.read_csv(f"../data/{weekday}.csv",sep = ";", index_col = 0, parse_dates=True )
            
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
        #print(counter)
        #self.df = df
        df_starting = df.drop_duplicates(subset=['customer_no'],keep='first')
        df_starting = df_starting.groupby("location").count()
        df_starting["start_prob"] = df_starting["customer_no"]/df_starting["customer_no"].sum()
        df_starting = df_starting["start_prob"] 
        prob=df_starting.to_dict()
        print(prob)

 
    def import_clean_csv(self):
        """
        imports the respective weekday csv and cleans the data:
        - adds checkout and timestamp for customers which have not checkout

        """
        df = pd.DataFrame()
        counter = 0
        number_of_cust = 0
        
        # read the single .csv files by a loop
        for weekday in ["monday","tuesday","wednesday","thursday","friday"]:
            df_weekday = pd.DataFrame()
            df_weekday = pd.read_csv(f"../data/{weekday}.csv",sep = ";", index_col = 0, parse_dates=True )
            
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
        self.df = df

    # def calc_trans_matrix():
        
    #     """
    #     calculates the transition matrix
    #     """
    #     df_week = import_clean_csv()
    #     df_shifted=df_week.sort_values(["customer_no","time"])
    #     df_shifted["next_location"] = df_shifted["location"].shift(-1)
    #     df_shifted=df_shifted.loc[df_shifted["location"]!="checkout"]
    #     df_shifted
    #     ### Create transition  matrix
    #     # create transition matrix between Location and next_Location
    #     trans_matrix = pd.crosstab(df_shifted["location"], df_shifted["next_location"],normalize="index")
    #     print(trans_matrix)
    
    # def calc_starting_prob():
    #     """
    #     imports the respective weekday csv and cleans the data:
    #     - adds checkout and timestamp for customers which have not checkout

    #     """
#if __name__ == "__main__":
    
    #SupermarketCalculator.import_clean_csv()
    #SupermarketCalculator.calc_trans_matrix