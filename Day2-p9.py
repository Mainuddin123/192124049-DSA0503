import pandas as pd

data = {
    'OrderDate': ['1-6-18', '1-23-18', '2-9-18', '2-26-18', '3-15-18', '4-1-18', '4-18-18', '5-5-18', '5-22-18', '6-8-18', '6-25-18', '7-12-18', '7-29-18', '8-15-18', '9-1-18', '9-18-18', '10-5-18', '10-22-18'],
    'Region': ['East', 'Central', 'Central', 'Central', 'West', 'East', 'Central', 'Central', 'West', 'East', 'Central', 'East', 'East', 'East', 'Central', 'East', 'Central', 'East'],
    'Manager': ['Martha', 'Hermann', 'Hermann', 'Timothy', 'Timothy', 'Martha', 'Martha', 'Hermann', 'Douglas', 'Martha', 'Hermann', 'Martha', 'Douglas', 'Martha', 'Douglas', 'Hermann', 'Martha', 'Martha'],
    'SalesMan': ['Alexander', 'Shelli', 'Luis', 'David', 'Stephen', 'Alexander', 'Steven', 'Luis', 'Michael', 'Alexander', 'Sigal', 'Diana', 'Karen', 'Alexander', 'John', 'Alexander', 'Sigal', 'Alexander'],
    'Item': ['Television', 'Home Theater', 'Television', 'Cell Phone', 'Television', 'Home Theater', 'Television', 'Television', 'Television', 'Home Theater', 'Television', 'Home Theater', 'Home Theater', 'Television', 'Desk', 'Video Games', 'Home Theater', 'Cell Phone'],
    'Units': [95, 50, 36, 27, 56, 60, 75, 90, 32, 60, 90, 29, 81, 35, 2, 16, 28, 64],
    'Unit_price': [1198.00, 500.00, 1198.00, 225.00, 1198.00, 500.00, 1198.00, 1198.00, 1198.00, 500.00, 1198.00, 500.00, 500.00, 1198.00, 125.00, 58.50, 500.00, 225.00],
}

sales_data = pd.DataFrame(data)


pivot_table = sales_data.pivot_table(index=['Region', 'Manager', 'SalesMan'], values='Unit_price', aggfunc='sum')

pivot_table.reset_index(inplace=True)

pivot_table.columns = ['Region', 'Manager', 'SalesMan', 'Total Sale Amount']

print(pivot_table)

Region  Manager   SalesMan  Total Sale Amount
0   Central  Douglas       John              125.0
1   Central  Hermann       Luis             2396.0
2   Central  Hermann     Shelli              500.0
3   Central  Hermann      Sigal             1198.0
4   Central   Martha      Sigal              500.0
5   Central   Martha     Steven             1198.0
6   Central  Timothy      David              225.0
7      East  Douglas      Karen              500.0
8      East  Hermann  Alexander               58.5
9      East   Martha  Alexander             3621.0
10     East   Martha      Diana              500.0
11     West  Douglas    Michael             1198.0
12     West  Timothy    Stephen             1198.0

