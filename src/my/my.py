import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models import Span, Label
from bokeh.charts import output_notebook, show, Bar, output_file, BoxPlot

import warnings
from IPython.core.display import display, HTML

#disable annoying warnings
warnings.filterwarnings('ignore')

#alternative to output_notebook which loads html from file
def displayHTML(file):
    with open(file, 'r') as myfile:
        data=myfile.read()
        display(HTML(data))

#returns a reduced version of a dataframe, given a percentage (topx) and a column to sort
def topX(dataFrame, topx, column, ascendingOrder=False):
    sorted = data.sort([column], ascending=ascendingOrder)
    nRows = data.shape[0]
    toRemain = nRows * topx
    toUse = []
    for i in range(nRows):
        if(i <= toRemain):
            toUse.append(True)
        else:
            toUse.append(False)
    return data[toUse]
