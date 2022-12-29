# append stock price in pandas dataframe

import pandas as pd

data = {'Name': ['Tom', 'nick', 'krish', 'jack'], 'Age': [20, 21, 19, 18]} 

# Create DataFrame 
df = pd.DataFrame(data) 

# append stock price 
df['Stock Price'] = [12.45, 14.50, 15.60, 11.20]

print(df)
