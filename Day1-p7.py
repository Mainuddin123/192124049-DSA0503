import pandas as pd

data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Sale': [100, 200, 150, 300, 250, 120, 180, 220, 130, 280]
}

sales_data = pd.DataFrame(data)

pivot_table = sales_data.pivot_table(index='Item', values='Sale', aggfunc={'Sale': ['max', 'min']})


pivot_table.reset_index(inplace=True)


pivot_table.columns = ['Item', 'Max Sale', 'Min Sale']

print(pivot_table)

Item  Max Sale  Min Sale
0    A       150       100
1    B       250       200
2    C       300       180
