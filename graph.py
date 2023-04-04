import networkx as nx
import random
from consumer import Consumer
from producer import Producer

class Graph:
    def __init__(self, num_producers, num_consumers, connectivity_prob):
        self.graph = nx.Graph()
        self.num_producers = num_producers
        self.num_consumers = num_consumers
        self.connectivity_prob = connectivity_prob
        self.producers = []
        self.consumers = []
        
        # Add producer nodes
        for i in range(num_producers):
            newProducer = Producer(0,0,0,0)
            self.graph.add_node(newProducer)
            self.producers.append(newProducer)
            
        # Add consumer nodes
        for i in range(num_consumers):
            newConsumer = Consumer(0,[],0)
            self.graph.add_node(newConsumer)
            self.consumers.append(newConsumer)
            
        # Connect every consumer to every producer with a weight between 0
        for consumer in range(num_consumers):
            for producer in range(num_producers):
                weight = 0
                self.graph.add_edge(f"Consumer_{consumer}", f"Producer_{producer}", weight=weight)
                     
        # Connect consumers to other consumers with a probability of connectivity_prob with a weight of 0
        for i in range(num_consumers):
            for j in range(i+1, num_consumers):
                if random.random() < connectivity_prob:
                    weight = 0
                    self.graph.add_edge(f"Consumer_{i}", f"Consumer_{j}", weight)


    # Takes two nodes and updates the edge weight if there is one
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

    def consumerAwareness(self,consumer):
        awareness = []

        return awareness