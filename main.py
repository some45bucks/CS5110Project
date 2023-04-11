from simulation import Simulation 
from graph import Graph
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a simulation.')
    parser.add_argument('-n', type=int, default=5, help='consumers')
    parser.add_argument('-m', type=int, default=5, help='producers')
    parser.add_argument('-p', type=float, default=0.4, help='probability of an edge existing')
    parser.add_argument('-s', type=str, default='1000', help='number of steps')
    args = parser.parse_args()

    graph = Graph(args.n, args.m, args.p)

    simulation = Simulation(graph,args.s)
    

    done = False
    while not done:
        done = simulation.runTimeStep()
    