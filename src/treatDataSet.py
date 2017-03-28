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

#data = pd.read_csv("datasets/CO2_passenger_cars_v12.tsv", sep='\t', header=0)#treating the original data
data = pd.read_csv("../datasets/CO2-passenger-cars-v12-less.csv", header=0)#treating the -less data

data = pd.concat([data[col].astype(str).str.upper() for col in data.columns], axis=1)
data['id'] = data['id'].astype(int)
data['r'] = data['r'].astype(int)
data['e (g/km)'] = data['e (g/km)'].astype(float)
data['m (kg)'] = data['m (kg)'].astype(float)
data['w (mm)'] = data['w (mm)'].astype(float)
data['at1 (mm)'] = data['at1 (mm)'].astype(float)
data['at2 (mm)'] = data['at2 (mm)'].astype(float)
data['ec (cm3)'] = data['ec (cm3)'].astype(float)
data['z (Wh/km)'] = data['z (Wh/km)'].astype(float)
data['Er (g/km)'] = data['Er (g/km)'].astype(float)
data['ep (KW)'] = data['ep (KW)'].astype(float)
data.rename(columns={'e (g/km)': 'e', 'm (kg)': 'm'}, inplace=True)

data = data.drop('MP', 1);
data = data.drop('MMS', 1);
data = data.drop('T', 1);
data = data.drop('w (mm)', 1);
data = data.drop('at1 (mm)', 1);
data = data.drop('at2 (mm)', 1);
data = data.drop('TAN', 1);

emission = data['e']
kg = data['m']
ePerKG = emission / kg
data['ePerKG(e/m)'] = ePerKG

#data.to_csv("CO2-passenger-cars-v12-treated.csv")
data.to_csv("../datasets/CO2-passenger-cars-v12-treated-less.csv")
