import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

data = pd.read_csv(datasetPath, header=0)
manufact = set([])
for i in data['Mh'].values:
    manufact.add(i)

manufactArray = []
registers = []
totalEmission = []
averageE = []
carsUnder95 = []
carsUnder95Percent = []
for m in manufact:
    mData = data[data.Mh == m]
    manufactArray.append(m)
    regs = 0
    em = 0
    c95 = 0
    for label, row in mData.iterrows():
        regs = regs + row['r']
        em = em + (row['e'] * row['r'])
        if(row['e'] <= 95):
            c95 = c95 + row['r']
    registers.append(regs)
    totalEmission.append(em)
    carsUnder95.append(c95)
    averageE.append(em / regs)
    carsUnder95Percent.append((c95/regs)*100)

manufactFrame = pd.DataFrame()
manufactFrame = manufactFrame.append(pd.DataFrame({'Mh' : manufactArray}))
manufactFrame['r'] = np.nan
manufactFrame['e'] = np.nan
manufactFrame['averageE'] = np.nan
manufactFrame['carsUnder95'] = np.nan
manufactFrame['carsUnder95Percent'] = np.nan
manufactFrame['circleSize'] = np.nan
manufactFrame['circleColor'] = ''

for i in range(len(registers)):
    manufactFrame.set_value(i, 'r', registers[i])
    manufactFrame.set_value(i, 'e', totalEmission[i])
    manufactFrame.set_value(i, 'carsUnder95', carsUnder95[i])
    manufactFrame.set_value(i, 'averageE', averageE[i])
    manufactFrame.set_value(i, 'carsUnder95Percent', carsUnder95Percent[i])
    manufactFrame.set_value(i, 'circleSize', (carsUnder95Percent[i]/2)+25)
    r = str("%0.2X" % int((averageE[i]/1000)*255))
    g = str("%0.2X" % int((carsUnder95Percent[i]/100)*255))
    b = str("%0.2X" % 30)
    manufactFrame.set_value(i, 'circleColor', "#"+r+g+b)
s = ColumnDataSource(manufactFrame)
p = figure(x_axis_label='Registers', y_axis_label='Average Emission (g/km)', title="Emission on Manufacturers")
p.circle('r', 'averageE', size='circleSize', source=s, alpha=0.6, fill_color='circleColor')

tips=[('Name','@Mh'),
     ('Cars under 95g/km','@carsUnder95')]

hline = Span(location=95, dimension='width', line_color='green', line_width=3, line_dash='dashed')
p.renderers.extend([hline])
p.add_layout(Label(x=40000, y=95, text='95 g/km target'))
hover = HoverTool(tooltips=tips)
p.add_tools(hover)
output_file("../results/emission_manufact.html")
show(p)
