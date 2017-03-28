import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models import Span, Label
from bokeh.charts import output_notebook, show, Bar, output_file, BoxPlot
from my import topX

data = pd.read_csv("../datasets/CO2_passenger_cars_v12.tsv", sep='\t', header=0)

nRows = data.shape[0] #get count of rows
print("Rows before: ")
print(nRows)

lessData = topX(data, 0.01, 'r')

print("Rows now: ")
print(lessData.shape[0])

lessData.to_csv("../datasets/CO2-passenger-cars-v12-less.csv")
