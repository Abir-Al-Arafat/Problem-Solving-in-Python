# define a 'Graph' class and implement the following
# a constructor to initialize an empty dictionary/graph
# method named 'add_vertex' to add a vertex/key
# method named 'add_edge' to add an edge to the vertex/key
# method named 'remove_edge' to remove an edge from the vertex/key
# method named 'remove_vertex' to remove vertex/key

class Graph:
    def __init__(self):
        # initializing a dictionary to keep the adjacency list
        self.adj_list = {}

    # method to add a vertex/key
    def add_vertex(self, value):
        # checking if the vertex/key already exists
        if value not in self.adj_list.keys():
            self.adj_list[value] = []
            return True
        return False

    # method to print all the vertices and adjacency list
    def print_graph(self):
        # printing the graph
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")

    # method to add an edge to the vertex/key
    def add_edge(self, vertex1, vertex2):
        # checking if the vertices exist
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            # adding vertex2 in the adj list of vertex1
            self.adj_list[vertex1].append(vertex2)
            # adding vertex1 in the adj list of vertex2
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    # method to remove an edge of a vertex/key
    def remove_edge(self, vertex1, vertex2):
        # checking if the vertices exist
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            # removing edge of vertex1
            self.adj_list[vertex1].remove(vertex2)
            # removing edge of vertex2
            self.adj_list[vertex2].remove(vertex1)
            return True
        return False

    # method to remove vertex/key
    def remove_vertex(self, vertex):
        # checking if the vertex exists
        if vertex in self.adj_list.keys():
            # running for loop to get the list of edges associated with the vertices
            for edge in self.adj_list[vertex]:
                # removing the edges
                self.adj_list[edge].remove(vertex)
            # removing the vertex
            self.adj_list.pop(vertex)
            return True
        return False


graph = Graph()

print("Adding Vertices")

print(graph.add_vertex('A'))
print(graph.add_vertex('B'))
print(graph.add_vertex('C'))
print(graph.add_vertex('D'))

graph.print_graph()

print("Adding Edges")
print(graph.add_edge('A', 'B'))
print(graph.add_edge('A', 'C'))
print(graph.add_edge('A', 'D'))
print(graph.add_edge('B', 'D'))
print(graph.add_edge('C', 'D'))

graph.print_graph()

# print("Removing Edges")

# graph.remove_edge('A', 'B')
# graph.print_graph()

print("Removing Vertex")
print(graph.remove_vertex('D'))
graph.print_graph()
