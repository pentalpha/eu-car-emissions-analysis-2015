import pandas as pd
def topX(dataFrame, topx, column, ascendingOrder=False):
    sorted = data.sort_values(column, ascending=ascendingOrder)
    nRows = data.shape[0]
    toRemain = nRows * topx
    toUse = []
    for i in range(nRows):
        if(i <= toRemain):
            toUse.append(True)
        else:
            toUse.append(False)
    return data[toUse]

data = pd.read_csv("../datasets/CO2_passenger_cars_v12.tsv", sep='\t', header=0)

nRows = data.shape[0] #get count of rows
print("Rows before: ")
print(nRows)

lessData = topX(data, 0.01, 'r')

print("Rows now: ")
print(lessData.shape[0])

lessData.to_csv("../datasets/CO2-passenger-cars-v12-less.csv")
