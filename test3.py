import csv
from collections import defaultdict
import json


# add nodes
def addNode(graph, nodeToAdd):
    if nodeToAdd not in graph:
        graph[nodeToAdd]=set()

    return graph

# add connections:
def addConnection(graph, origin, destination):
    print(origin,destination)
    addNode(graph, origin)
    addNode(graph, destination)

    graph[origin].add(str(destination))

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
graph=defaultdict(set)
filepath='example/example0.csv'
with open(filepath) as csvFile:
    csvReader=csv.DictReader(csvFile)
    for row in csvReader:
        #graph=addNode(graph,row['origin'])
        graph=addConnection(graph, row['origin'],row['destination'])

print("Nodes:", graph)

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
for i in data:
    print(i)

list=[]
with open(filepath) as csvFile:
    csvReader=csv.DictReader(csvFile)
    for row in csvReader:
        for i in data:
            print(i)
            for j in range(0,len(i)-1):
                if j==0 and row['origin']==i[j] and row['destination']==i[j+1]:
                    print(row)
                if j>=0 and row['origin']==i[j] and row['destination']==i[j+1]:
                    if row['flight_no'] not in list:
                        print(row)
