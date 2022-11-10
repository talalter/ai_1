from Vertex import Vertex


class Graph:

    def __init__(self, config_):
        self.num_of_vertices, self.vertices, self.edges = self.parse_config(config_)
        self.graph = self.build_dict_graph(self.vertices, self.edges)
        self.list_of_only_vertices = [vertex for vertex in self.graph.keys()]
        self.brokens = [False for vertex in self.vertices]
        self.peoples = [vertex[1] for vertex in self.vertices]

    def parse_config(self, config_):
        num_vertex = 0
        all_vertices = []
        all_edges = []
        for line in config_.split('\n'):
            if len(line) > 0:
                first_letter = line[1]
                if first_letter == 'N':
                    num_vertex = int(line[3:])
                elif first_letter == 'V':
                    info_on_vertex = line[1:].split()
                    if len(info_on_vertex) == 1:
                        vertex_name = int(info_on_vertex[0][1:]) - 1
                        amount_of_people = 0  # maybe 0 or False
                        vertex_is_brittle = False
                        all_vertices.append((vertex_name, amount_of_people, vertex_is_brittle))
                    elif len(info_on_vertex) == 2:
                        vertex_name = int(info_on_vertex[0][1:]) - 1
                        if 'P' in info_on_vertex[1]:
                            amount_of_people = info_on_vertex[1][1:]
                            vertex_is_brittle = False
                        else:
                            amount_of_people = 0  # maybe 0 or False
                            vertex_is_brittle = True
                        all_vertices.append((vertex_name, amount_of_people, vertex_is_brittle))
                    else:
                        vertex_name = int(info_on_vertex[0][1:]) - 1
                        amount_of_people = info_on_vertex[1][1:]
                        vertex_is_brittle = True
                        all_vertices.append((vertex_name, amount_of_people, vertex_is_brittle))
                else:
                    info_on_vertex = line[1:].split()
                    all_edges.append(tuple(info_on_vertex))
        return num_vertex, all_vertices, all_edges

    def build_dict_graph(self, vertices_list, edges_list):
        dict_graph = dict()
        all_vertices = []
        for vertex in vertices_list:
            vertex_id = vertex[0]
            vertex_to_add = Vertex(vertex_id, vertex[1], vertex[2])
            all_vertices.append(vertex_to_add)
            dict_graph[vertex_to_add] = []
        for edge in edges_list:
            for vertex in all_vertices:
                if vertex.id_ == int(edge[1]) - 1:
                    for vertex_j in all_vertices:
                        if (vertex_j.id_ == int(edge[2]) - 1):
                            dict_graph[vertex].append((vertex_j, edge[3]))
                elif vertex.id_ == int(edge[2]) - 1:
                    for vertex_j in all_vertices:
                        if (vertex_j.id_ == int(edge[1]) - 1):
                            dict_graph[vertex].append((vertex_j, edge[3]))
        return dict_graph

    def __str__(self):
        res = ""
        for vertex in self.graph:
            for neighbourhood in self.graph[vertex]:
                res += str(vertex.id_) + f"---{str(neighbourhood[1])}-->"
                res += str(neighbourhood[0]) + "  "
            res += '\n'
        return res
