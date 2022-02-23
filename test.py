import csv
from collections import defaultdict
import json



def generate_edges(graph):
  edges = []

  # for each node in graph
  for node in graph:
    print(node)
      # for each neighbour node of a single node
    for neighbour in graph[node]:
        #print(neighbour)
        # if edge exists then append
        edges.append((node, neighbour))
  return edges

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

graph=defaultdict(list)

filepath='example/example0.csv'
with open(filepath) as csvFile:
    csvReader=csv.DictReader(csvFile)
    for row in csvReader:
      #  print(row)
        # graph[str(row['origin'])].add(row['destination'])
        if row['destination'] not in graph[row['origin']]:
            graph[row['origin']].append(row['destination'])
                                        #[
                                        # row['destination']
                                        #  ,row['flight_no']
                                        #  ,row['departure']
                                        #  ,row['arrival']
                                        #  ,row['base_price']
                                        #  ,row['bag_price']
                                        #  ,row['bags_allowed']
                                         #]
                                         # )



        
print(json.dumps(graph,sort_keys=False,indent=2))
# for k,v in graph.items():  
#   print(k,'\n',v)



with open('graphdata.json', 'w') as outfile:
    json.dump(graph,outfile)


# print(generate_edges(graph))


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

   
# Driver function call to print all 
# generated paths

#print(find_all_paths(graph, 'd', 'c'))
   
# Driver function call to print all 
# generated paths

data=find_all_paths(graph, 'WIW', 'ECV')
#data=find_all_paths(graph, 'ZRW', 'BPZ')
#data=find_all_paths(graph, 'ZRW', 'BPZ')

# print(data)
print(json.dumps(find_all_paths(graph, 'WIW', 'ECV'),indent=3,sort_keys=False))
f=[]
with open(filepath) as csvFile:
    csvReader=csv.DictReader(csvFile)
      # flights['flights']=[]
    for row in csvReader:    
        for i in data:   
          for j in range(0,len(i)):
              #flights=defaultdict(list) 
              if j-1<0 and (i[0]==row['origin'] and row['destination']==i[j+1]):
                # print(row)
                print(i[j],i[j+1])
              elif j<len(i)-1 and (i[j]==row['origin'] and row['destination']==i[j+1]):
                print(i)
                print(row)

                #flights['flights'].append(row)
                #f.append(flights)
          #print('flight')
# for i in data:
#   for j in range(0,len(i)):
#     if j-1<0:
#       print(i[0],i[j+1])
#     elif j<len(i)-1:
#       print(i[j],i[j+1])
#   print('done')
    # for k in range(1,len(i)):
    #   print(i[j],i[k])

# print(f)

# print(json.dumps(f,sort_keys=False,indent=2))
# for i in f:
#   # print(i)
#   # print(f,'\n')
#   for k,v in i.items():
#     print(k,'\n','\t\t',v)

#print(find_path(graph, 'ZRW', 'BPZ'))
# print(len(data))
# with open('testreult.json', 'w') as outfile:
#             json.dump(f, outfile)


            

              
            
      