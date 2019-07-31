import county_demographics
import numpy as np
import matplotlib.pyplot as plt
list_of_report = county_demographics.get_all_counties()
incomes = []
for i in range(len(list_of_report)):
    incomes.append(list_of_report[i]["Income"]["Median Houseold Income"])
plt.hist(incomes, bins = [0,20000,40000,60000,80000,100000,120000])
plt.xlabel("Median household income of county")
plt.ylabel("Number of counties in income bracket")
plt.show()
