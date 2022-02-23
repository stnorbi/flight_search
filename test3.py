import csv
from collections import defaultdict
import json
import os

os.system('clear')

# add nodes
def addNode(graph, nodeToAdd):
    if nodeToAdd not in graph:
        graph[nodeToAdd]=[]

    return graph

# add connections:
def addConnection(graph, origin, destination):
    #print(origin,destination)
    addNode(graph, origin)
    addNode(graph, destination)
    if str(destination) not in graph[origin]:
      graph[origin].append(str(destination))
    

    return graph

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(graph,v1, v2, e1):
  # global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = [v2, e1]
    graph[v1].append(temp)
    return graph


def find_all_paths(graph, start, end, path =[]):
  path = path + [start]

  if start == end:

    return [path]

  paths = []
  for node in graph[start]:
    # print(node)
    # print(path)
    if node not in path:

      newpaths = find_all_paths(graph, node, end, path)

      for newpath in newpaths:

        paths.append(newpath)

  return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


# add nodes
graph=defaultdict(list)
filepath='example/example0.csv'
with open(filepath) as csvFile:
    csvReader=csv.DictReader(csvFile)
    for row in csvReader:
        #graph=addNode(graph,row['origin'])
        graph=addConnection(graph, row['origin'],row['destination'])
        #graph=add_edge(graph,row['origin'],row['destination'],row)

#print("Nodes:", graph)

#add connection
with open(filepath) as csvFile:
    csvReader=csv.DictReader(csvFile)
    for row in csvReader:
        graph=addConnection(graph, row['origin'],row['destination'])

print("connections:", graph)


data=find_all_paths(graph, 'WIW', 'ECV')
#print(data)

# shortdata=find_shortest_path(graph, 'WIW', 'ECV')
# print(shortdata)
# for i in data:
#     print(i)

# list=[]
# with open(filepath) as csvFile:
#     csvReader=csv.DictReader(csvFile)
#     for row in csvReader:
#         for i in data:
#             print(i)
#             for j in range(0,len(i)-1):
#                 if j==0 and row['origin']==i[j] and row['destination']==i[j+1]:
#                     print(row)
#                 if j>=0 and row['origin']==i[j] and row['destination']==i[j+1]:
#                     if row['flight_no'] not in list:
#                         print(row)


class grapher:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
   def edges(self):
      return self.findedges()
# Add the new edge
   def AddEdge(self, edge):
      edge = set(edge)
      (vrtx1, vrtx2) = tuple(edge)
      if vrtx1 in self.gdict:
         self.gdict[vrtx1].append(vrtx2)
      else:
         self.gdict[vrtx1] = [vrtx2]
# List the edge names
   def findedges(self):
      edgename = []
      for vrtx in self.gdict:
        for nxtvrtx in self.gdict[vrtx]:
            if {nxtvrtx, vrtx} not in edgename:
               edgename.append({vrtx, nxtvrtx})
        return edgename

# def generate_edges(graph):
#   edges = []

#   # for each node in graph
#   for node in graph:
#     print(node)
#       # for each neighbour node of a single node
#     for neighbour in graph[node]:
#         #print(neighbour)
#         # if edge exists then append
#         edges.append((node, neighbour))
#   return edges
    

gr=grapher(graph)
edges=gr.findedges()
print(edges)
for i in edges:
  print(add_edge(graph,'WIW','ECV',i))
  
