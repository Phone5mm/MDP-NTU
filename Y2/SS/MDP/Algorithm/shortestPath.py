#Calculate Distance
def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

#Add vertex to graph
def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

# Add edge between vertex v1 and v2 with weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e
        graph[index2][index1] = e

# Print the graph
def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j], \
        " edge weight: ", graph[i][j])


#Five obstacles and origin get from android
origin = [0,0]
A = [3,5]
B = [3,9]
C = [6,3]
D = [15,10]
E = [10,5] 
obstacle_list = [A,B,C,D,E]
visited_vertex = [0,0,0,0,0]
obstacle_distance = [distance(origin,A),distance(origin,B),distance(origin,C),distance(origin,D),distance(origin,E)]
first_vertex = obstacle_distance.index(min(obstacle_distance))
print(first_vertex)
# stores the vertices in the graph
vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []
# Add vertices to the graph
add_vertex(0)
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
# Add the edges between the vertices with the edge weights.
add_edge(0, 1, round(distance(A,B),2))
add_edge(0, 2, round(distance(A,C),2))
add_edge(0, 3, round(distance(A,D),2))
add_edge(0, 4, round(distance(A,E),2))
add_edge(1, 2, round(distance(B,C),2))
add_edge(1, 3, round(distance(B,D),2))
add_edge(1, 4, round(distance(B,E),2))
add_edge(2, 3, round(distance(C,D),2))
add_edge(2, 4, round(distance(C,E),2))
add_edge(3, 4, round(distance(D,E),2))

print("Internal representation: ", graph)

# Update the current vertex
current_vertex = first_vertex
shortest_path=[100,100,100,100,100]
for i in range(0, 5):
    shortest_path[i] = current_vertex
    minimum = 200
    min_index = 0
    visited_vertex[current_vertex] = 1
    for j in range (0, 5):
        if graph[current_vertex][j]<minimum and current_vertex!=j:
            if visited_vertex[j] == 0 :
                minimum = graph[current_vertex][j]
                min_index = j
    current_vertex = min_index
print(shortest_path)
        
