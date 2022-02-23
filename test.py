import csv
from collections import defaultdict
import json

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
    
# print(json.dumps(graph,sort_keys=False,indent=2))
# for k,v in graph.items():  
#   print(k,'\n',v)
print(graph)
with open('graphdata.json', 'w') as outfile:
            json.dump(graph,outfile)

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

# print(json.dumps(find_all_paths(graph, 'WIW', 'ECV'),indent=3,sort_keys=False))
f=[]
with open(filepath) as csvFile:
    csvReader=csv.DictReader(csvFile)
      # flights['flights']=[]
    for i in data:  
      for row in csvReader:
          flights=defaultdict(list)      
          for j in range(0,len(i)):
            if (j+1)<len(i) and (i[j]==row['origin'] or row['destination']==i[j+1]):
              # print(row)
              flights['flights'].append(row)
              f.append(flights)
              
# print(f)

print(json.dumps(f,sort_keys=False,indent=2))
# for i in f:
#   # print(i)
#   # print(f,'\n')
#   for k,v in i.items():
#     print(k,'\n','\t\t',v)

#print(find_path(graph, 'ZRW', 'BPZ'))
# print(len(data))
# with open('testreult.json', 'w') as outfile:
#             json.dump(data, outfile)


            

              
            
      