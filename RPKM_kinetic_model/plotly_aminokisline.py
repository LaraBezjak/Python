"""
Created on Mon Mar  2 09:37:00 2020

@author: Lara
"""
from xlrd import open_workbook
# Data
p = open_workbook('Aminokisline_ext.xlsx').sheet_by_index(0) #predicted
e = open_workbook('Aminokisline_ext.xlsx').sheet_by_index(1) #experimental

# Time points
time_p = [p.cell_value(i,0) for i in range(1,p.nrows)]
time_e = [e.cell_value(i,0) for i in range(1,e.nrows)]
t=[0,2,4,6,8,10,12]

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Initialize figure with subplots
fig = make_subplots(rows=3, cols=2, vertical_spacing=0.17)

# Add tracescoloraxis
fig.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,1) for i in range(1,p.nrows)], line=dict(color='blue'),name='predicted'), row=1, col=1)
fig.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,1) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red'), name='measured'), row=1, col=1)
fig.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,2) for i in range(1,p.nrows)], line=dict(color='blue')), row=1, col=2)
fig.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,2) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=1, col=2)
fig.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,3) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=1)
fig.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,3) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=1)
fig.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,4) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=2)
fig.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,4) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=2)
fig.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,5) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=1)
fig.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,5) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=1)
fig.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,6) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=2)
fig.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,6) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=2)

# Update xaxis properties
fig.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')

# Update yaxis properties
fig.update_yaxes(title_text='Ile', title_standoff = 3, row=1, col=1, range=[-0.2, 2.0], gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_yaxes(title_text='Ile', title_standoff = 3, row=1, col=2, range=[-0.2, 1.3], gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_yaxes(title_text='Leu', title_standoff = 3, row=2, col=1, range=[-0.2, 2.0], gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_yaxes(title_text='Leu', title_standoff = 3, row=2, col=2, range=[-0.2, 1.3], gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_yaxes(title_text='Cys', title_standoff = 3, row=3, col=1, range=[-0.2, 6.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig.update_yaxes(title_text='Cys', title_standoff = 3, row=3, col=2, range=[-0.2, 2.6], gridcolor='lightgray', zerolinecolor='lightgray')

# Update title and size
fig.update_layout(title_text='', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=8),
                  annotations=[dict(x=0.22,y=1.1,showarrow=False,text="CC", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0.77,y=1.1,showarrow=False,text="HD", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0,y=1.07,showarrow=False,text="a)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=1.07,showarrow=False,text="b)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.68,showarrow=False,text="c)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.68,showarrow=False,text="d)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.22,showarrow=False,text="e)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.22,showarrow=False,text="f)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=-0.10,y=0.3,showarrow=False,text="Conc [ProNorm]", textangle=-90, 
                                    xref="paper",yref="paper", font=dict(size=12))])
# Save figure
fig.write_image("aa_1.png")


# Initialize figure with subplots
fig2 = make_subplots(rows=3, cols=2, vertical_spacing=0.17)

# Add tracescoloraxis
fig2.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,7) for i in range(1,p.nrows)], line=dict(color='blue'), name='predicted'), row=1, col=1)
fig2.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,7) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red'), name='measured'), row=1, col=1)
fig2.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,8) for i in range(1,p.nrows)], line=dict(color='blue')), row=1, col=2)
fig2.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,8) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=1, col=2)
fig2.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,9) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=1)
fig2.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,9) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=1)
fig2.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,10) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=2)
fig2.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,10) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=2)
fig2.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,11) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=1)
fig2.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,11) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=1)
fig2.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,12) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=2)
fig2.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,12) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=2)

# Update xaxis properties
fig2.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')

# Update yaxis properties
fig2.update_yaxes(title_text='Ala', title_standoff = 3, row=1, col=1, range=[-0.2, 2.0], gridcolor='lightgray', zerolinecolor='lightgray',secondary_y=False)
fig2.update_yaxes(title_text='Ala', title_standoff = 3, row=1, col=2, range=[-0.2, 3], gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_yaxes(title_text='Gln', title_standoff = 3, row=2, col=1, range=[-0.2, 5.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_yaxes(title_text='Gln', title_standoff = 3, row=2, col=2, range=[-0.2, 6], gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_yaxes(title_text='Asn', title_standoff = 3, row=3, col=1, range=[-0.2, 3], gridcolor='lightgray', zerolinecolor='lightgray')
fig2.update_yaxes(title_text='Asn', title_standoff = 3, row=3, col=2, range=[-0.2, 4.5], gridcolor='lightgray', zerolinecolor='lightgray')

# Update title and size
fig2.update_layout(title_text='', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=8),
                  annotations=[dict(x=0.22,y=1.1,showarrow=False,text="CC", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0.77,y=1.1,showarrow=False,text="HD", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0,y=1.07,showarrow=False,text="a)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=1.07,showarrow=False,text="b)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.68,showarrow=False,text="c)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.68,showarrow=False,text="d)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.22,showarrow=False,text="e)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.22,showarrow=False,text="f)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=-0.10,y=0.3,showarrow=False,text="Conc [ProNorm]", textangle=-90, 
                                    xref="paper",yref="paper", font=dict(size=12))])
# Save figure
fig2.write_image("aa_2.png")


# Initialize figure with subplots
fig3 = make_subplots(rows=3, cols=2, vertical_spacing=0.17)

# Add tracescoloraxis
fig3.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,13) for i in range(1,p.nrows)], line=dict(color='blue'),name='predicted'), row=1, col=1)
fig3.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,13) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red'),name='measured'), row=1, col=1)
fig3.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,14) for i in range(1,p.nrows)], line=dict(color='blue')), row=1, col=2)
fig3.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,14) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=1, col=2)
fig3.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,38) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=1)
fig3.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,38) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=1)
fig3.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,39) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=2)
fig3.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,39) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=2)
fig3.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,17) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=1)
fig3.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,17) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=1)
fig3.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,18) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=2)
fig3.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,18) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=2)

# Update xaxis properties
fig3.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')

# Update yaxis properties
fig3.update_yaxes(title_text='His', title_standoff = 3, row=1, col=1, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray',secondary_y=False)
fig3.update_yaxes(title_text='His', title_standoff = 3, row=1, col=2, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_yaxes(title_text='Phe', title_standoff = 3, row=2, col=1, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_yaxes(title_text='Phe', title_standoff = 3, row=2, col=2, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_yaxes(title_text='Arg', title_standoff = 3, row=3, col=1, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')
fig3.update_yaxes(title_text='Arg', title_standoff = 3, row=3, col=2, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')

# Update title and size
fig3.update_layout(title_text='', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=8),
                  annotations=[dict(x=0.22,y=1.1,showarrow=False,text="CC", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0.77,y=1.1,showarrow=False,text="HD", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0,y=1.07,showarrow=False,text="a)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=1.07,showarrow=False,text="b)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.68,showarrow=False,text="c)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.68,showarrow=False,text="d)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.22,showarrow=False,text="e)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.22,showarrow=False,text="f)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=-0.10,y=0.3,showarrow=False,text="Conc [ProNorm]", textangle=-90, 
                                    xref="paper",yref="paper", font=dict(size=12))])
# Save figure
fig3.write_image("aa_3.png")



# Initialize figure with subplots
fig4 = make_subplots(rows=4, cols=2, vertical_spacing=0.14)

# Add tracescoloraxis
fig4.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,29) for i in range(1,p.nrows)], line=dict(color='blue'),name='predicted'), row=1, col=1)
fig4.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,29) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red'),name='measured'), row=1, col=1)
fig4.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,30) for i in range(1,p.nrows)], line=dict(color='blue')), row=1, col=2)
fig4.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,30) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=1, col=2)
fig4.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,33) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=1)
fig4.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,33) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=1)
fig4.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,34) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=2)
fig4.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,34) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=2)
fig4.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,25) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=1)
fig4.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,25) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=1)
fig4.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,26) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=2)
fig4.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,26) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=2)
fig4.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,35) for i in range(1,p.nrows)], line=dict(color='blue')), row=4, col=1)
fig4.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,35) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=4, col=1)
fig4.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,36) for i in range(1,p.nrows)], line=dict(color='blue')), row=4, col=2)
fig4.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,36) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=4, col=2)

# Update xaxis properties
fig4.update_xaxes(title_text='Time [day]', title_standoff = 1, row=1, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_xaxes(title_text='Time [day]', title_standoff = 3, row=4, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_xaxes(title_text='Time [day]', title_standoff = 3, row=4, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')

# Update yaxis properties
fig4.update_yaxes(title_text='Lys', title_standoff = 3, row=1, col=1, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray',secondary_y=False)
fig4.update_yaxes(title_text='Lys', title_standoff = 3, row=1, col=2, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_yaxes(title_text='Met', title_standoff = 3, row=2, col=1, range=[-0.2, 1.7], gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_yaxes(title_text='Met', title_standoff = 3, row=2, col=2, range=[-0.2, 1.7], gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_yaxes(title_text='Thr', title_standoff = 3, row=3, col=1, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_yaxes(title_text='Thr', title_standoff = 3, row=3, col=2, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_yaxes(title_text='Val', title_standoff = 3, row=4, col=1, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')
fig4.update_yaxes(title_text='Val', title_standoff = 3, row=4, col=2, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')

# Update title and size
fig4.update_layout(title_text='', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=8),
                  annotations=[dict(x=0.22,y=1.1,showarrow=False,text="CC", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0.77,y=1.1,showarrow=False,text="HD", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0,y=1.07,showarrow=False,text="a)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=1.07,showarrow=False,text="b)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.78,showarrow=False,text="c)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.78,showarrow=False,text="d)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.47,showarrow=False,text="e)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.47,showarrow=False,text="f)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.17,showarrow=False,text="g)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.17,showarrow=False,text="h)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=-0.10,y=0.3,showarrow=False,text="Conc [ProNorm]", textangle=-90, 
                                    xref="paper",yref="paper", font=dict(size=12))])
# Save figure
fig4.write_image("aa_4.png")


# Initialize figure with subplots
fig5 = make_subplots(rows=3, cols=2, vertical_spacing=0.17)

# Add tracescoloraxis
fig5.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,31) for i in range(1,p.nrows)], line=dict(color='blue'),name='predicted'), row=1, col=1)
fig5.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,31) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red'),name='measured'), row=1, col=1)
fig5.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,32) for i in range(1,p.nrows)], line=dict(color='blue')), row=1, col=2)
fig5.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,32) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=1, col=2)
fig5.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,15) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=1)
fig5.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,15) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=1)
fig5.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,16) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=2)
fig5.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,16) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=2)
fig5.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,21) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=1)
fig5.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,21) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=1)
fig5.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,22) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=2)
fig5.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,22) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=2)

# Update xaxis properties
fig5.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')

# Update yaxis properties
fig5.update_yaxes(title_text='Tyr', title_standoff = 3, row=1, col=1, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_yaxes(title_text='Tyr', title_standoff = 3, row=1, col=2, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_yaxes(title_text='Ser', title_standoff = 3, row=2, col=1, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray',secondary_y=False)
fig5.update_yaxes(title_text='Ser', title_standoff = 3, row=2, col=2, range=[-0.2, 2], gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_yaxes(title_text='Asp', title_standoff = 3, row=3, col=1, range=[-0.2, 1.6], gridcolor='lightgray', zerolinecolor='lightgray')
fig5.update_yaxes(title_text='Asp', title_standoff = 3, row=3, col=2, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')

# Update title and size
fig5.update_layout(title_text='', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=8),
                  annotations=[dict(x=0.22,y=1.1,showarrow=False,text="CC", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0.77,y=1.1,showarrow=False,text="HD", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0,y=1.07,showarrow=False,text="a)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=1.07,showarrow=False,text="b)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.68,showarrow=False,text="c)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.68,showarrow=False,text="d)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.22,showarrow=False,text="e)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.22,showarrow=False,text="f)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=-0.10,y=0.3,showarrow=False,text="Conc [ProNorm]", textangle=-90, 
                                    xref="paper",yref="paper", font=dict(size=12))])
# Save figure
fig5.write_image("aa_5.png")


# Initialize figure with subplots
fig6 = make_subplots(rows=4, cols=2, vertical_spacing=0.17)

# Add tracescoloraxis
fig6.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,23) for i in range(1,p.nrows)], line=dict(color='blue'),name='predicted'), row=1, col=1)
fig6.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,23) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red'),name='measured'), row=1, col=1)
fig6.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,24) for i in range(1,p.nrows)], line=dict(color='blue')), row=1, col=2)
fig6.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,24) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=1, col=2)
fig6.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,19) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=1)
fig6.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,19) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=1)
fig6.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,20) for i in range(1,p.nrows)], line=dict(color='blue')), row=2, col=2)
fig6.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,20) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=2, col=2)
fig6.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,27) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=1)
fig6.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,27) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=1)
fig6.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,28) for i in range(1,p.nrows)], line=dict(color='blue')), row=3, col=2)
fig6.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,28) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=3, col=2)
fig6.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,39) for i in range(1,p.nrows)], line=dict(color='blue')), row=4, col=1)
fig6.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,39) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=4, col=1)
fig6.add_trace(go.Scatter(x=time_p,y=[p.cell_value(i,40) for i in range(1,p.nrows)], line=dict(color='blue')), row=4, col=2)
fig6.add_trace(go.Scatter(x=time_e,y=[e.cell_value(i,40) for i in range(1,e.nrows)], mode="markers", marker=dict(color='red')), row=4, col=2)

# Update xaxis properties
fig6.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_xaxes(title_text='Time [day]', title_standoff = 3, row=1, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_xaxes(title_text='Time [day]', title_standoff = 3, row=2, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_xaxes(title_text='Time [day]', title_standoff = 3, row=3, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_xaxes(title_text='Time [day]', title_standoff = 3, row=4, col=1, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_xaxes(title_text='Time [day]', title_standoff = 3, row=4, col=2, range=[-0.2, 12.5], tickvals=t, gridcolor='lightgray', zerolinecolor='lightgray')

# Update yaxis properties
fig6.update_yaxes(title_text='Glu', title_standoff = 3, row=1, col=1, range=[-0.2, 3], gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_yaxes(title_text='Glu', title_standoff = 3, row=1, col=2, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_yaxes(title_text='Gly', title_standoff = 3, row=2, col=1, range=[-0.2, 3.5], gridcolor='lightgray', zerolinecolor='lightgray',secondary_y=False)
fig6.update_yaxes(title_text='Gly', title_standoff = 3, row=2, col=2, range=[-0.2, 3], gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_yaxes(title_text='Pro', title_standoff = 3, row=3, col=1, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_yaxes(title_text='Pro', title_standoff = 3, row=3, col=2, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_yaxes(title_text='Trp', title_standoff = 3, row=4, col=1, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')
fig6.update_yaxes(title_text='Trp', title_standoff = 3, row=4, col=2, range=[-0.2, 1.5], gridcolor='lightgray', zerolinecolor='lightgray')

# Update title and size
fig6.update_layout(title_text='', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=8),
                  annotations=[dict(x=0.22,y=1.1,showarrow=False,text="CC", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0.77,y=1.1,showarrow=False,text="HD", xref="paper",yref="paper", font=dict(size=12)),
                               dict(x=0,y=1.07,showarrow=False,text="a)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=1.07,showarrow=False,text="b)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.78,showarrow=False,text="c)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.78,showarrow=False,text="d)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.47,showarrow=False,text="e)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.47,showarrow=False,text="f)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0,y=0.16,showarrow=False,text="g)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=0.57,y=0.16,showarrow=False,text="h)", xref="paper",yref="paper", font=dict(size=10)),
                               dict(x=-0.10,y=0.3,showarrow=False,text="Conc [ProNorm]", textangle=-90, 
                                    xref="paper",yref="paper", font=dict(size=12))])
# Save figure
fig6.write_image("aa_6.png")
