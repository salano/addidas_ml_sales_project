# addidas_ml_sales_project

This machine language project (ML) uses an Addidas sales dataset to predict total sales.
The dataset consists of 17 column and 9648 rows.

Exploratory data analysis was done in Jupyter notebook (included)

The ML project evaluated the below Linear models using the datasets and select the best models for predict on unseen data

The output:

                Model Name  R2_Score

5 XGBRegressor 0.948962
2 Gradient Boosting 0.941864
6 CatBoosting Regression 0.941740
0 Random Forest 0.941219
9 Lasso Regression 0.902021
10 ElasticNet Regression 0.901928
8 Ridge Regression 0.901837
3 Linear Regression 0.901591
1 Decision Tree 0.898055
7 ADABoost Regression 0.871441
4 K-Neighbors Regression 0.569129

      Actual Value  Predicted Value    Difference

0 200000.0 183489.390625 16510.609375
1 10019.0 6124.300781 3894.699219
2 9024.0 4899.485352 4124.514648
3 292500.0 289755.500000 2744.500000
4 120000.0 132041.500000 -12041.500000
... ... ... ...
1925 192500.0 126729.132812 65770.867188
1926 704.0 1376.284790 -672.284790
1927 1400.0 1238.208496 161.791504
1928 972.0 6767.209473 -5795.209473
1929 373750.0 359863.281250 13886.718750

[1930 rows x 3 columns]

unseen inputS
Units Sold Campaign Retailer Region City Product Sales Method Sales person Category Segment
0 1200 21 Walmart Midwest Chicago Women's Apparel In-store Oby Sorrel Accessory Accessory
Predicted value: 315228.0000
