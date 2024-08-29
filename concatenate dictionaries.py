"""
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create an empty dictionary 'dic4' that will store the combined key-value pairs from 'dic1', 'dic2', and 'dic3'.
dic4 = {}

# Iterate through each dictionary ('dic1', 'dic2', and 'dic3') using a loop.
for d in (dic1, dic2, dic3):
    # Update 'dic4' by adding the key-value pairs from the current dictionary 'd'.
    dic4.update(d)

# Print the combined dictionary 'dic4' containing all the key-value pairs from 'dic1', 'dic2', and 'dic3'.
print(dic4)
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4) 
