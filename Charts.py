#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:56:27 2022

@author: theju
"""

import yfinance
tsla = yfinance.Ticker('TSLA')
hist = tsla.history(period='1y')

import plotly.graph_objects as go

from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=hist.index,y=hist['Close'],name='Price'),secondary_y=False)
fig.add_trace(go.Bar(x=hist.index,y=hist['Volume'],name='Volume'),secondary_y=True)


fig.update_yaxes(range=[0,7000000000],secondary_y=True)
fig.update_yaxes(visible=False, secondary_y=True)


fig.show()



fig.write_html("/Users/theju/Desktop/USD/Business Analytics Fund./Chart.html")
