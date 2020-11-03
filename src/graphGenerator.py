from tulip import tlp
import sys
params = tlp.getDefaultPluginParameters('Grid')

# set any input parameter value if needed
# params['width'] = ...
# params['height'] = ...
# params['connectivity'] = ...
# params['oppositeNodesConnected'] = ...
# params['spacing'] = ...

# graph = tlp.importGraph('Grid', params)
filename = sys.path[0]+'\data\graph.json'
# params = tlp.getDefaultPluginParameters('JSON Export', graph)

# set any input parameter value if needed
# params['Export id'] = True
graph = tlp.newGraph()
n0 = graph.addNode({"label":100})
n1=graph.addNode({"id":3})
# e0=graph.addEdge
outputFile = filename
success = tlp.exportGraph('JSON Export', graph, outputFile, params)
