import county_demographics
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
list_of_report = county_demographics.get_all_counties()
WIncomes = []
West = ["WA","OR","CA","NV","UT","CO","WY","ID","MO","AK","HI"]
SouthWest = ["AZ","NM","TX","OK"]
MidWest = ["ND","SD","MO","NE","OH","KS","IN","WI","IL","MI","MN","IA"]
SouthEast = ["FL","GA","AL","MS","LA","AR","TN","NC","SC","VA"]
NorthEast = ["WV","MD","RI","PA","NJ","CT","NY","MA","NH","VT","ME","DE"]
SWIncomes = []
MWIncomes = []
SEIncomes = []
NEIncomes = []
for i in range(len(list_of_report)):
    state = list_of_report[i]["State"]
    if state in West:
        WIncomes.append(list_of_report[i]["Income"]["Median Houseold Income"])
    if state in MidWest:
        MWIncomes.append(list_of_report[i]["Income"]["Median Houseold Income"])
    if state in SouthWest:
        SWIncomes.append(list_of_report[i]["Income"]["Median Houseold Income"])
    if state in SouthEast:
        SEIncomes.append(list_of_report[i]["Income"]["Median Houseold Income"])
    if state in NorthEast:
        NEIncomes.append(list_of_report[i]["Income"]["Median Houseold Income"])
W2040 = 0
W4060 = 0
W6080 = 0
W80100 = 0
W100120 = 0
for i in range(len(WIncomes)):
    if WIncomes[i] >= 20000 and WIncomes[i] < 40000:
        W2040 = W2040 + 1
    if WIncomes[i] >= 40000 and WIncomes[i] < 60000:
        W4060 = W4060 + 1
    if WIncomes[i] >= 60000 and WIncomes[i] < 80000:
        W6080 = W6080 + 1
    if WIncomes[i] >= 80000 and WIncomes[i] < 100000:
        W80100 = W80100 + 1
    if WIncomes[i] >= 100000 and WIncomes[i] < 120000:
        W100120 = W100120 + 1
SW2040 = 0
SW4060 = 0
SW6080 = 0
SW80100 = 0
SW100120 = 0
for i in range(len(SWIncomes)):
    if SWIncomes[i] >= 20000 and SWIncomes[i] < 40000:
        SW2040 = SW2040 + 1
    if SWIncomes[i] >= 40000 and SWIncomes[i] < 60000:
        SW4060 = SW4060 + 1
    if SWIncomes[i] >= 60000 and SWIncomes[i] < 80000:
        SW6080 = SW6080 + 1
    if SWIncomes[i] >= 80000 and SWIncomes[i] < 100000:
        SW80100 = SW80100 + 1
    if SWIncomes[i] >= 100000 and SWIncomes[i] < 120000:
        SW100120 = SW100120 + 1
MW2040 = 0
MW4060 = 0
MW6080 = 0
MW80100 = 0
MW100120 = 0
for i in range(len(MWIncomes)):
    if MWIncomes[i] >= 20000 and MWIncomes[i] < 40000:
        MW2040 = MW2040 + 1
    if MWIncomes[i] >= 40000 and MWIncomes[i] < 60000:
        MW4060 = MW4060 + 1
    if MWIncomes[i] >= 60000 and MWIncomes[i] < 80000:
        MW6080 = MW6080 + 1
    if MWIncomes[i] >= 80000 and MWIncomes[i] < 100000:
        MW80100 = MW80100 + 1
    if MWIncomes[i] >= 100000 and MWIncomes[i] < 120000:
        MW100120 = MW100120 + 1
SE2040 = 0
SE4060 = 0
SE6080 = 0
SE80100 = 0
SE100120 = 0
for i in range(len(SEIncomes)):
    if SEIncomes[i] >= 20000 and SEIncomes[i] < 40000:
        SE2040 = SE2040 + 1
    if SEIncomes[i] >= 40000 and SEIncomes[i] < 60000:
        SE4060 = SE4060 + 1
    if SEIncomes[i] >= 60000 and SEIncomes[i] < 80000:
        SE6080 = SE6080 + 1
    if SEIncomes[i] >= 80000 and SEIncomes[i] < 100000:
        SE80100 = SE80100 + 1
    if SEIncomes[i] >= 100000 and SEIncomes[i] < 120000:
        SE100120 = SE100120 + 1
NE2040 = 0
NE4060 = 0
NE6080 = 0
NE80100 = 0
NE100120 = 0
for i in range(len(NEIncomes)):
    if NEIncomes[i] >= 20000 and NEIncomes[i] < 40000:
        NE2040 = NE2040 + 1
    if NEIncomes[i] >= 40000 and NEIncomes[i] < 60000:
        NE4060 = NE4060 + 1
    if NEIncomes[i] >= 60000 and NEIncomes[i] < 80000:
        NE6080 = NE6080 + 1
    if NEIncomes[i] >= 80000 and NEIncomes[i] < 100000:
        NE80100 = NE80100 + 1
    if NEIncomes[i] >= 100000 and NEIncomes[i] < 120000:
        NE100120 = NE100120 + 1
W = (W2040,W4060,W6080,W80100,W100120)
SW = (SW2040+W2040,SW4060+W4060,SW6080+W6080,SW80100+W80100,SW100120+W100120)
MW = (MW2040+SW2040+W2040,MW4060+SW4060+W4060,MW6080+SW6080+W6080,MW80100+SW80100+W80100,MW100120+SW100120+W100120)
SE = (SE2040+MW2040+SW2040+W2040,SE4060+MW4060+SW4060+W4060,SE6080+MW6080+SW6080+W6080,SE80100+MW80100+SW80100+W80100,SE100120+MW100120+SW100120+W100120)
NE = (NE2040+SE2040+MW2040+SW2040+W2040,NE4060+SE4060+MW4060+SW4060+W4060,NE6080+SE6080+MW6080+SW6080+W6080,NE80100+SE80100+MW80100+SW80100+W80100, NE100120+SE100120+MW100120+SW100120+W100120)
X = np.arange(5)
WB = plt.bar(X, W, color = 'b')
SWB = plt.bar(X, SW, color = 'r', bottom = W)
MWB = plt.bar(X, MW, color = 'c', bottom = SW)
SEB = plt.bar(X, SE, color = 'g', bottom = MW)
NEB = plt.bar(X, NE, color = 'y', bottom = SE)
incomes=['20-40k','40-60k','60-80k','80-100k','100-120k']
plt.xticks(X, incomes)
plt.title("Average household incomes across United States counties")
plt.xlabel("Average yearly household income")
plt.ylabel("Number of counties in income bracket")
plt.legend((WB[0], SWB[0], MWB[0], SEB[0], NEB[0]), ('West', 'Southwest', 'Midwest','Southeast','Northeast'))
plt.show()
