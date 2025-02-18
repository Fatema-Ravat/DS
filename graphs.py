class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True

        return False
    
    def add_edge(self,v1,v2):
        # create an edge between v1 and v2
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        # remove an edge between v1 and v2
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError: #error generated when the edge already does not exists
                pass
            return True
        return False
    
    def delete_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for temp_vertex in self.adj_list[vertex]:
                self.adj_list[temp_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex ,":" , self.adj_list[vertex])
    
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A","B")
g.print_graph()
