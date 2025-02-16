import sys
import pandas as pd

from src.exception import CustomException
from src.exception import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:

            model_path = 'artifacts\model.pk1'
            preprocessor_path = 'artifacts\preprocessor.pk1'

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)
            predicts = model.predict(data_scaled)

            return predicts
        except Exception as e:
            raise CustomException(e, sys)



class CustomData:
    def __init__(self,
                 Units_Sold: float,
                 Campaign: int,
                 Retailer: str,
                 Region: str,
                 City: str,
                 Product: str,
                 Sales_Method: str,
                 Sales_person: str,
                 Category: str,
                 Segment: str
                 
                 ):
        
        self.Units_Sold = Units_Sold
        self.Campaign = Campaign
        self.Retailer = Retailer
        self.Region = Region
        self.City = City
        self.Product = Product
        self.Sales_Method = Sales_Method
        self.Sales_person = Sales_person
        self.Category = Category
        self.Segment = Segment


    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Units Sold' : [self.Units_Sold],
                'Campaign' : [self.Campaign],
                'Retailer' : [self.Retailer],
                'Region' : [self.Region],
                'City' : [self.City],
                'Product' : [self.Product],
                'Sales Method' : [self.Sales_Method],
                'Sales person' : [self.Sales_person],
                'Category' : [self.Category],
                'Segment' : [self.Segment]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)