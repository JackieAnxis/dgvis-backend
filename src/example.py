from tulip import tlp
from tulipgui import tlpgui

class GraphObserver(tlp.Observable):
  def __init__(self):
    tlp.Observable.__init__(self)

  def treatEvent(self, event):
    if isinstance(event, tlp.GraphEvent):
      graph = event.getGraph()
      if event.getType() == tlp.GraphEvent.TLP_ADD_NODE:
        print("The node", event.getNode(), "has been added to the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_DEL_NODE:
        print("The node", event.getNode(), "has been deleted from the graph", graph)

      if event.getType() == tlp.GraphEvent.TLP_ADD_EDGE:
        print("The edge", event.getEdge(), "has been added to the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_DEL_EDGE:
        print("The edge", event.getEdge(), "has been deleted from the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_REVERSE_EDGE:
        print("The edge", event.getEdge(), "has been reversed in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_SET_ENDS:
        print("The edge", event.getEdge(), "will have its ends modified. Current source is", graph.source(event.getEdge()),\
              "Current target is", graph.target(event.getEdge()))

      elif event.getType() == tlp.GraphEvent.TLP_AFTER_SET_ENDS:
        print("The edge", event.getEdge(), "had its ends modified. Current source is", graph.source(event.getEdge()),\
              "Current target is", graph.target(event.getEdge()))

      elif event.getType() == tlp.GraphEvent.TLP_ADD_NODES:
        print("The nodes", event.getNodes(), "have been added to the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_ADD_EDGES:
        print("The edges", event.getEdges(), "have been added to the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_ADD_DESCENDANTGRAPH:
        print("A descendant graph", event.getSubGraph(), "is about to be added in the subgraphs hierarchy of graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_AFTER_ADD_DESCENDANTGRAPH:
        print("A descendant graph", event.getSubGraph(), "has been added in the subgraphs hierarchy of graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_DEL_DESCENDANTGRAPH:
        print("A descendant graph", event.getSubGraph(), "is about to be deleted in the subgraphs hierarchy of graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_AFTER_DEL_DESCENDANTGRAPH:
        print("A descendant graph", event.getSubGraph(), "has been deleted in the subgraphs hierarchy of graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_ADD_SUBGRAPH:
        print("A subgraph", event.getSubGraph(), "is about to be added in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_AFTER_ADD_SUBGRAPH:
        print("A subgraph", event.getSubGraph(), "has been added in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_DEL_SUBGRAPH:
        print("A subgraph", event.getSubGraph(), "is about to be deleted in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_AFTER_DEL_SUBGRAPH:
        print("A subgraph", event.getSubGraph(), "has been deleted in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_ADD_LOCAL_PROPERTY:
        print("A local property", event.getPropertyName(), "is about to be added in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_ADD_LOCAL_PROPERTY:
        print("A local property", event.getPropertyName(), "has been added in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_DEL_LOCAL_PROPERTY:
        print("A local property", event.getPropertyName(), "is about to be deleted in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_AFTER_DEL_LOCAL_PROPERTY:
        print("A local property", event.getPropertyName(), "has been deleted in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_ADD_INHERITED_PROPERTY:
        print("An inherited property", event.getPropertyName(), "is about to be added in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_ADD_INHERITED_PROPERTY:
        print("An inherited property", event.getPropertyName(), "has been added in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_DEL_INHERITED_PROPERTY:
        print("An inherited property", event.getPropertyName(), "is about to be deleted in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_AFTER_DEL_INHERITED_PROPERTY:
        print("An inherited property", event.getPropertyName(), "has been deleted in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_BEFORE_SET_ATTRIBUTE:
        print("An attribute", event.getAttributeName(), "is about to be set/modified in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_AFTER_SET_ATTRIBUTE:
        print("An attribute", event.getAttributeName(), "has been set/modified in the graph", graph)

      elif event.getType() == tlp.GraphEvent.TLP_REMOVE_ATTRIBUTE:
        print("An attribute", event.getAttributeName(), "has been removed in the graph", graph)

root = tlp.newGraph()
root.setName("root")
graph = root.addSubGraph("graph")

obs = GraphObserver()
graph.addListener(obs)

n = graph.addNode()
n2 = graph.addNode()
e = graph.addEdge(n, n2)
graph.reverse(e)
graph.setEnds(e, n, n2)

nodes = graph.addNodes(4)
edges = graph.addEdges([(nodes[0], nodes[1]), (nodes[2], nodes[3])])

sg = graph.addSubGraph("sg1")
sg2 = sg.addSubGraph("sg2")

# sg.delSubGraph(sg2)
# graph.delSubGraph(sg)

prop = graph.getDoubleProperty("metric")
propRoot = root.getDoubleProperty("metric_root")

# graph.delLocalProperty("metric")
# root.delLocalProperty("metric_root")

graph.setAttribute("author", "me")
# graph.removeAttribute("author")
view = tlpgui.createNodeLinkDiagramView(graph)
viewColor = graph.getColorProperty("viewColor")
for n in graph.getNodes():
    viewColor[n] = tlp.Color(0, 255, 0)

# graph.delEdge(e)
# graph.delNode(n)
# graph.delNode(n2)