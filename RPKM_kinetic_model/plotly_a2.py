"""
Created on Wed Mar 18 16:08:33 2020

@author: Lara
"""
from xlrd import open_workbook
# Data
p = open_workbook('A2_ext.xlsx').sheet_by_index(0) #predicted
e = open_workbook('A2_ext.xlsx').sheet_by_index(1) #experimental

# Time points
time_p = [p.cell_value(i,0) for i in range(1,p.nrows)]
time_e = [e.cell_value(i,0) for i in range(1,e.nrows)]
t=[0,2,4,6,8,10,12]

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Initialize figure with subplots
fig = make_subplots(rows=2, cols=1, vertical_spacing=0.25)

# Add tracescoloraxis
fig.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,1) for i in range(1,p.nrows)], line=dict(color='blue'),name='predicted'), row=1, col=1)
fig.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,1) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red'), name='measured'), row=1, col=1)
fig.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,2) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=1)
fig.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,2) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=1)


# Update xaxis properties
fig.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')

# Update yaxis properties
fig.update_yaxes(title_text='A2 Fraction [/]', title_standoff = 3, row=1, col=1, range=[0., 1], gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_yaxes(title_text='A2 Fraction [/]', title_standoff = 3, row=2, col=1, range=[0, 1], gridcolor='lightgray', zerolinecolor='lightgray')

# Update title and size
fig.update_layout(title_text='', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=8),
                  annotations=[dict(x=0.49,y=1.1,showarrow=False,text="CC", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0.49,y=0.45,showarrow=False,text="HD", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0,y=1.07,showarrow=False,text="a)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.45,showarrow=False,text="b)", xref="paper",yref="paper", font=dict(size=10))])
# Save figure
fig.write_image("a2.png")
