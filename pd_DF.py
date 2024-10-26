import pandas as pd

data = pd.DataFrame({'Brand': ['Maruti', 'Hyundai', 'Tata', 'Mahindra','Maruti', 'Hyundai', 'Renault', 'Tata', 'Maruti'], 
    'Year': [2012, 2014, 2011, 2015, 2012, 2016, 2014, 2018, 2019], 
    'KM Driven': [50000, 30000, 60000, 25000, 10000, 46000, 31000, 15000, 12000], 
    'City': ['Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Ghaziabad'], 
    'Mileage': [28, 27, 25, 26, 28, 29, 24, 21, 24]})

print(data)

print(data.loc[0])

print(data.loc[0:3])
# range 3 include

#  select and display rows from the DataFrame where the brand is ‘Maruti’ and the 
# mileage is greater than 25, showing relevant information about Maruti cars with high
# mileage.

print(data.loc[(data.Brand == 'Maruti')&(data.Mileage>25)])

#  select range of rows from 2 to 5 
print(data.loc[2:5])

# update the ‘Mileage’ values to 22 for cars in the DataFrame where the manufacturing
# year is before 2015 

data.loc[(data.Year < 2015),['Mileage']]=22
print(data)

#  extract and display specific rows with indices 0, 2, 4, and 7
print(data.iloc[[0,2,4,7]])

# extract and display a subset of the DataFrame, including rows 1 to 4 and cols 2 to 4.
print(data.iloc[3:5,2:5])
# exclude the last range