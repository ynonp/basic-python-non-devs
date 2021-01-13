import pandas as pd

# df -> data frame
df = pd.read_csv('BankChurners.csv')
new_data = df.loc[:,['Credit_Limit', 'Customer_Age']]
new_data.to_csv('bref.csv')
