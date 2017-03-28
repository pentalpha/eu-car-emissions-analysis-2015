import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models import Span, Label
from bokeh.charts import output_notebook, show, Bar, output_file, BoxPlot, save
import math
#datasetPath = "datasets/CO2-passenger-cars-v12-less.csv"
#datasetPath = "../datasets/CO2-passenger-cars-v12-treated-less.csv"
datasetPath = "../datasets/CO2-passenger-cars-v12-treated.csv"
#datasetPath = "datasets/CO2_passenger_cars_v12.tsv" #use separator='\t
euCountriesPath = "../datasets/european-union-countries.csv"

kmPerYear=12284.03
data = pd.read_csv(datasetPath, header=0)

countriesDF = pd.read_csv(euCountriesPath)
countriesDF['totalEmission'] = ''
countriesDF['circleSize'] = ''
countriesDF['circleColor'] = ''
emissions = []
circleSize = []

for label, row in countriesDF.iterrows():
    print("Processing ", row['id'])
    id = row['id']
    countryDF = data[data.MS == id]
    emission = 0
    for label, row2 in countryDF.iterrows():
        e = row2['e']
        r = row2['r']
        if(math.isnan(r)):
            r = 0
        if(math.isnan(e)):
            e = 0
        emission = emission + (r * e)*kmPerYear
    emissions.append(emission)
    circleSize.append(32 + np.random.randint(low=0, high=10))

for i in range(len(emissions)):
    countriesDF.set_value(i, 'totalEmission', emissions[i]/1000/1000)
    countriesDF.set_value(i, 'circleSize', circleSize[i])
    colorFactor = np.random.randint(low=1, high=230)
    r = str("%0.2X" %(np.random.randint(low=30, high=240)))
    g = str("%0.2X" %(np.random.randint(low=30, high=240)))
    b = str("%0.2X" %(np.random.randint(low=0, high=100)))
    countriesDF.set_value(i, 'circleColor', "#"+r+g+b)

print("Making bokeh plot:")
countriesSource = ColumnDataSource(countriesDF)
p = figure(x_axis_label='Population (millions)', y_axis_label='Emission of CO2 (ton) in 2015', title='Emissions per Country', x_axis_type="log", x_range=[0, 90])
p.circle('POPULATION-MILLIONS', 'totalEmission', source=countriesSource, size='circleSize', alpha=0.8, color='circleColor')
p.text('POPULATION-MILLIONS', 'totalEmission',text='id', source=countriesSource, text_baseline="middle", text_align="center")
p.add_tools(HoverTool(tooltips=[('Name','@COUNTRYNAME'), ('Pop.', '@POPULATION-MILLIONS'), ('CO2', '@totalEmission')]))
p.plot_width=920
#p.xaxis[0].formatter.use_scientific = False

output_file('../results/eu-emission.html')
save(p)
