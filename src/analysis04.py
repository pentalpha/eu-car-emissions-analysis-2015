import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models import Span, Label
from bokeh.charts import output_notebook, show, Bar, output_file, BoxPlot
import my
#datasetPath = "datasets/CO2-passenger-cars-v12-less.csv"
datasetPath = "../datasets/CO2-passenger-cars-v12-treated-less.csv"
#datasetPath = "datasets/CO2-passenger-cars-v12-treated.csv"
#datasetPath = "datasets/CO2_passenger_cars_v12.tsv" #use separator='\t
euCountriesPath = "../datasets/european-union-countries.csv"

kmPerYear=12284.03
data = pd.read_csv(datasetPath, header=0)

countriesDF = pd.read_csv("../datasets/european-union-countries.csv")
countriesDF['totalEmission'] = ''
countriesDF['totalPerHab'] = ''
countriesDF['circleSize'] = ''
countriesDF['circleColor'] = ''
emissions = []
emissionsPerHab = []
circleSize = []

for label, row in countriesDF.iterrows():
    id = row['id']
    countryDF = data[data.MS == id]
    emission = 0
    for label, row2 in countryDF.iterrows():
        emission = emission + (row2['r'] * row2['e'])*kmPerYear
    emissions.append(emission)
    ePerHab = emission/row['POPULATION']
    emissionsPerHab.append(ePerHab)
    circleSize.append(26+ePerHab*0.014)

for i in range(len(emissions)):
    countriesDF.set_value(i, 'totalEmission', emissions[i]/1000/1000)
    countriesDF.set_value(i, 'totalPerHab', emissionsPerHab[i]/1000)
    countriesDF.set_value(i, 'circleSize', circleSize[i])
    pollutionFactor = int(emissionsPerHab[i]*0.07)
    r = str("%0.2X" %(pollutionFactor + 0))
    g = str("%0.2X" %(255 - int(pollutionFactor)))
    b = str("%0.2X" % 0)
    countriesDF.set_value(i, 'circleColor', "#"+r+g+b)

countriesSource = ColumnDataSource(countriesDF)
p = figure(x_axis_label='POPULATION', y_axis_label='Emission of CO2 (ton) in 2015', title='Emissions per Country')
p.circle('POPULATION', 'totalEmission', source=countriesSource, size='circleSize', alpha=0.8, color='circleColor')
p.text('POPULATION', 'totalEmission',text='id', source=countriesSource, text_baseline="middle", text_align="center")
p.add_tools(HoverTool(tooltips=[('Name','@COUNTRYNAME'), ('Emissions (kg) per hab.','@totalPerHab')]))
p.plot_width=920
p.xaxis[0].formatter.use_scientific = False

output_file('../results/eu-emission.html')
show(p)
