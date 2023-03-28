import sys
from simulation import Simulation 
from graph import Graph



if __name__ == "__main__":
    graph = Graph(5 , 5, .4)
    simulation = Simulation(graph)
    done = False
    while not done:
        done = simulation.runTimeStep()
    