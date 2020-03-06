from bokeh.io import show
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.util.structure import BokehStructureGraph

# draw the structure graph of a basic figure model
f=figure()
f.line(x=[1,2,3],y=[1,2,3])
show(row(f,BokehStructureGraph(f).model()))
