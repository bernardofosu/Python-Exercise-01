import sort
import pandas as pd

# How to sort an array
array = [2, 5, 6, 0, 4]
array = [11, 45, 80, 7, 9, 68, 20, 0, 2, 4, 2, 3, 34]

a=sort.sorting(array)
print(a)
b = sort.length(array)
print(b)


a = pd.to_datetime("2024-11-20")

# Create the pandas DataFrame
df = pd.DataFrame([["M", 10,"A"], ["F", 15,"A"], ["F", 24,"D"],["M", 10,"D"],
                   ["M", 14,"B"], ["F", 18,"B"], ["F", 27,"E"],["M", 15,"E"],
                   ["M", 17,"C"], ["F", 20,"C"]], columns = ['Gender', 'Population','Section'])
# print dataframe.
df

# simple list comprehension
array1 = (2, 5, 8, 9)
a = [i for i in array1 if i > 2]
print(a)