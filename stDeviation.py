import csv
import math

with open('Data.csv',newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]    

#function for calculating mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + x

    mean = total/n
    return mean

#squaring and getting the values
squared_list = []
for num in data:
    a = (int(num)-mean(data))
    a = a**2
    squared_list.append(a)

# sum of all elements in the squared_list
sum = 0
for i in squared_list:
    sum = sum + i

#divide the sum by total no. of values by N-1
result = sum/(len(data)-1)

#square root of result
std_deviation = math.sqrt(result)

print("standard deviation is: "+std_deviation)






