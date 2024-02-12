from openstaad import Geometry

geometry = Geometry()

selected_nodes = geometry.GetSelectedNodes()
selected_beams = geometry.GetSelectedBeams()

print(selected_nodes)
print(selected_beams)