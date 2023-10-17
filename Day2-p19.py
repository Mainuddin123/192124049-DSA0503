import pandas as pd
w_a_con = pd.read_csv(r"C:\Users\mainu\Desktop\world_alcohol_consumption.csv")
print("World alcohol consumption sample data:")
print(w_a_con.head())
print('\nShape of the dataframe: ',w_a_con.shape)
print('\nNumber of rows: ',w_a_con.shape[0])
print('\nNumber of column: ',w_a_con.shape[1])
print("\nExtract Column Names:")
print(w_a_con.columns)

World alcohol consumption sample data:
   Year           WHO region  ...      Types DisplayValue
0  1986   Western region      ...   Wine            0.000
1  1986  Americas             ...   Other           0.500
2  1985              Africa   ...    Wine           1.620
3  1986       Americans       ...    Beer           4.427
4  1987    Americans          ...    Beer           1.980

[5 rows x 5 columns]

Shape of the dataframe:  (5, 5)

Number of rows:  5

Number of column:  5

Extract Column Names:
Index(['Year', 'WHO region', ' Country Bevarage', 'Types', 'DisplayValue'], dtype='object')
