import pandas as pd
import sys 

from src.logger import logging
from src.exception import CustomException


def clean_input_data(df):
    try:
        ### Convert Price per Unit, Units Sold, and Total Sales to float
        logging.info('Start cleaning data')

        df['Total Sales'] = df['Total Sales'].str.replace(r'$', '')
        df['Total Sales'] = df['Total Sales'].str.replace(r',', '')

        df['Units Sold'] = df['Units Sold'].str.replace(',','')
        #df.replace(',','', regex=True, inplace=True

        df['Units Sold'] = df['Units Sold'].astype('float64') 
        df['Total Sales'] = df['Total Sales'].astype('float64') 
        
        return df
    except Exception as e:
        raise CustomException(e, sys)
   