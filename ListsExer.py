mylist = (10, 12, 34, 55, 34, 125, 78, 90)
print(mylist)
#printing highest and lowest numbers from "mylist"
print("Highest value in list:")
print(max(mylist))
print("Lowest values in list:")
print(min(mylist))
#removing duolicated number from "mylist"
mylist = list(dict.fromkeys(mylist))
print(mylist)


