import networkx as nx
import random

class Graph:
    def __init__(self, num_producers, num_consumers, connectivity_prob):
        self.graph = nx.Graph()
        self.num_producers = num_producers
        self.num_consumers = num_consumers
        self.connectivity_prob = connectivity_prob
        
        # Add producer nodes
        for i in range(num_producers):
            self.graph.add_node(f"Producer_{i}")
            
        # Add consumer nodes
        for i in range(num_consumers):
            self.graph.add_node(f"Consumer_{i}")
            
        # Connect every consumer to every producer with a random whole number weight between 0 and 10
        for consumer in range(num_consumers):
            for producer in range(num_producers):
                weight = random.randint(0, 10)
                self.graph.add_edge(f"Consumer_{consumer}", f"Producer_{producer}", weight=weight)
                     
        # Connect consumers to other consumers with a probability of connectivity_prob
        for i in range(num_consumers):
            for j in range(i+1, num_consumers):
                if random.random() < connectivity_prob:
                    self.graph.add_edge(f"Consumer_{i}", f"Consumer_{j}")


    def update_edge_weight(self, node1, node2, weight):
        """
        Updates the weight of the edge between node1 and node2 to the given weight.
        """
        if self.graph.has_edge(node1, node2):
            self.graph[node1][node2]['weight'] = weight
        else:
            print(f"Edge ({node1}, {node2}) does not exist in the graph.")
    

    
    def print_graph(self):
        """
        Prints all the edges and their weights in the graph.
        """
        for edge in self.graph.edges():
            weight = self.graph.get_edge_data(edge[0], edge[1]).get('weight', None)
            if weight is None:
                print(f"{edge[0]} -- {edge[1]}")
            else:
                print(f"{edge[0]} -- {edge[1]} : {weight}")

