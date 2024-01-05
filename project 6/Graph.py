class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2].append(vertex1)
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
        if vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2].remove(vertex1)
    
    def remove_vertex(self, vertex):
        while self.adjacency_list[vertex]:
            adjacent_vertex = self.adjacency_list[vertex].pop()
            self.remove_edge(vertex, adjacent_vertex)
        del self.adjacency_list[vertex]

    def bfs(self, start_vertex):
        visited = []
        queue = [start_vertex]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.append(current_vertex)
                queue.extend([v for v in self.adjacency_list[current_vertex] if v not in visited])
        
        return ' '.join(visited)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = []
        if start_vertex not in visited:
            visited.append(start_vertex)
            for neighbour in self.adjacency_list[start_vertex]:
                self.dfs(neighbour, visited)

        return ' '.join(visited)


# g = Graph()
# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')
# g.add_vertex('E')
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('C', 'D')
# g.add_edge('B', 'D')
# g.add_edge('B', 'E')
# g.add_edge('C', 'E')

# # نمایش لیست همجواری
# print("Adjacency List:")
# print(g.adjacency_list)

# # نمایش نتایج به صورت رشته از BFS و DFS
# print("\nBFS:")
# print(g.bfs('A'))

# print("\nDFS:")
# print(g.dfs('A'))