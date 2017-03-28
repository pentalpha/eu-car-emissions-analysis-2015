import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models import Span, Label
from bokeh.charts import output_notebook, show, Bar, output_file, BoxPlot
from my import topX, displayHTML
#datasetPath = "datasets/CO2-passenger-cars-v12-less.csv"
datasetPath = "../datasets/CO2-passenger-cars-v12-treated-less.csv"
#datasetPath = "datasets/CO2-passenger-cars-v12-treated.csv"
#datasetPath = "datasets/CO2_passenger_cars_v12.tsv" #use separator='\t
euCountriesPath = "../datasets/european-union-countries.csv"

data = pd.read_csv(datasetPath, header=0)

f = open('../results/lowestEmitters.txt', 'w')
f.write("\nThe lowest CO2 emitters: \n")
count = 0
for label, row in data.sort(['e'], ascending=True).iterrows():
    f.write(row['Mk'] + " " + row['Cn'] + ": " + str(row['e']) + '\n')
    if(count == 12):
        break
    else:
        count = count +1
f.close()
f = open('../results/biggestEmitters.txt', 'w')
f.write("The biggest CO2 emitters: \n")
count = 0
for label, row in data.sort(['e'], ascending=False).iterrows():
    f.write(row['Mk'] + " " + row['Cn'] + ": " + str(row['e'])+'\n')
    if(count == 12):
        break
    else:
        count = count +1
f.close()
