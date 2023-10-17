import pandas as pd
import numpy as np

np.random.seed(0)
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

def highlight_numbers(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

styled_df = df.applymap(highlight_numbers)
print(styled_df)

Column1       Column2       Column3       Column4
0  color: black  color: black  color: black  color: black
1  color: black    color: red  color: black    color: red
2    color: red  color: black  color: black  color: black
3  color: black  color: black  color: black  color: black
4  color: black    color: red  color: black    color: red
5    color: red  color: black  color: black    color: red
6  color: black    color: red  color: black    color: red
7  color: black  color: black  color: black  color: black
8    color: red    color: red    color: red  color: black
9  color: black  color: black    color: red    color: red
