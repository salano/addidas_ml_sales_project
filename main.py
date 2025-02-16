from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipelines.predict_pipeline import CustomData, PredictPipeline

if __name__ == "__main__":
    #Uncomment the below to retrain the model
    
    data_file_path = r'notebook\data\Adidas US Sales Datasets.csv'
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion(data_file_path)
    tgt_column_name = 'Total Sales'
    r_columns = ['Retailer ID', 'Invoice Date', 'State','Operating Profit', 'Operating Margin','Total Sales','Price per Unit']

    #dynamic categorization
    train_df = pd.read_csv(train_data)
    num_columns = train_df.select_dtypes(exclude="object").columns.tolist()
    cat_columns = train_df.select_dtypes(include="object").columns.tolist()

    #remove unwanted columns
    for col in r_columns:
        if col in num_columns:
            num_columns.remove(col)
        else:
            cat_columns.remove(col)

    data_transformation = DataTransformation()
    data_transformation.get_data_transformation_object(numerical_columns=num_columns, categorical_columns=cat_columns)
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data, 
        numerical_columns=num_columns, categorical_columns=cat_columns,
        target_column_name=tgt_column_name, removed_columns=r_columns
        )

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr, test_arr)
    
    # Make a prediction on unseen data
    data = CustomData(
            Units_Sold= 1200,
            Campaign= 21,
            Retailer= 'Walmart',
            Region= 'Midwest',
            City= 'Chicago',
            Product= 'Women\'s Apparel',
            Sales_Method= 'In-store',
            Sales_person='Oby Sorrel',
            Category='Accessory',
            Segment= 'Accessory'    

    )
  
    predict_df = data.get_data_as_dataframe()
    print(predict_df)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(predict_df)
    print("Predicted value: {:.4f}".format(results[0]))