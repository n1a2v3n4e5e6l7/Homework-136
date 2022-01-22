import pandas as pd
import csv
df = pd.read_csv("filtered_stars.csv")
df.head()
df.drop(['Unnamed: 0'],axis = 1,inplace = True)
name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
gravity = df["Gravity"].to_list()
distance = df["Distance"].to_list()
finallist = []
tempdict = {}
for i in range(0,len(name)):
    tempdict["name"] = name[i]
    tempdict["mass"] = mass[i]
    tempdict["gravity"] = gravity[i]
    tempdict["distance"] = distance[i]
    tempdict["radius"] = radius[i]
    finallist.append(tempdict)
print(finallist)