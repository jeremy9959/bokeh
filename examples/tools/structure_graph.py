from bokeh.io import show
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.models import HoverTool, ColumnDataSource, TapTool, ResetTool, BoxZoomTool
from bokeh.util.structure import BokehStructureGraph
import numpy as np

x=np.linspace(-10,10,100)
y=np.sin(x)
signal=y+np.random.normal(0,.3,size=x.shape[0])
source=ColumnDataSource({'x':x,'y':y,'signal':signal})
# draw the structure graph of a basic figure model
f=figure()
f.scatter(x='x',y='signal',source=source,  color='red', legend_label="measured")
f.line(x='x',y='y',source=source, color='blue', legend_label="truth")
f.xgrid.grid_line_color='white'
f.ygrid.grid_line_color='white'
f.background_fill_color="#eeeeee"
f.title.text = "Figure being analyzed"
f.legend.location = "top_left"
f.legend.click_policy="hide"
f.legend.background_fill_alpha = 0.0
T = HoverTool()
T.renderers=[f.renderers[0]]
S = TapTool()
S.renderers=[f.renderers[0]]
f.tools=[T,S, ResetTool(),BoxZoomTool()]
show(row(f,BokehStructureGraph(f).model()))
