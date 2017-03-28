import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models import Span, Label
from bokeh.charts import output_notebook, show, Bar, output_file, BoxPlot
import my
from my import topX, displayHTML
#datasetPath = "datasets/CO2-passenger-cars-v12-less.csv"
datasetPath = "../datasets/CO2-passenger-cars-v12-treated-less.csv"
#datasetPath = "datasets/CO2-passenger-cars-v12-treated.csv"
#datasetPath = "datasets/CO2_passenger_cars_v12.tsv" #use separator='\t
euCountriesPath = "../datasets/european-union-countries.csv"

data = pd.read_csv(datasetPath, header=0)

#create set with the existant fuel types
fuelTypes = set([])
fuelTypeColumn = data['Ft']
for i in fuelTypeColumn.values:
    fuelTypes.add(i)

#search for data on each fuel type
fuelTypeArray = []
emissionArray = []
fuelTypesDataframes = dict([])
fuelTypeRegs = pd.Series()
for f in fuelTypes:
    fuelTypesDataframes[f] = data[data.Ft == f]
    fuelTypeRegs[f] = 0;
    for label, row in fuelTypesDataframes[f].iterrows():
        rgs = row['r']
        fuelTypeRegs[f] = fuelTypeRegs[f] + rgs

sum = 0
for x in fuelTypeRegs:
    sum = sum + x

fuelTypeRegs = (fuelTypeRegs / sum)*100

ft = dict([])
ft['Usage %'] = []
ft['Fuel Type'] = []
ft['Fuel Type (detail)'] = []
for key,value in fuelTypeRegs.items():
    ft['Usage %'].append(value)
    ft['Fuel Type (detail)'].append(key)
    if(value < 10):
        ft['Fuel Type'].append('Others')
    else:
        ft['Fuel Type'].append(key)

p = Bar(ft, values='Usage %', label='Fuel Type', stack='Fuel Type (detail)', legend='top_center')
p.plot_height=500
p.plot_width=600
output_file("../results/bars_fueltypes.html", title="Use of different fuel types")
show(p)

box = BoxPlot(data, values='e', label='Ft',
              color='Ft', plot_width=900, legend=False)
output_file('../results/box.html')
show(box)
