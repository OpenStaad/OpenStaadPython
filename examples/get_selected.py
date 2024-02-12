from openstaad import Get
import pandas as pd

get = Get()


selected_nodes = get.geometry.GetSelectedNodes()
selected_beams = get.geometry.GetSelectedBeams()

print(selected_nodes)
print(selected_beams)