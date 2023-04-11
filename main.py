from simulation import Simulation 
from graph import Graph
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a simulation.')
    parser.add_argument('-n', type=int, default=10, help='producers')
    parser.add_argument('-m', type=int, default=100, help='consumers')
    parser.add_argument('-p', type=float, default=0.1, help='probability of an edge existing')
    parser.add_argument('-s', type=str, default='50', help='number of steps')
    args = parser.parse_args()

    graph = Graph(args.n, args.m, args.p)

    simulation = Simulation(graph,int(args.s))
    

    done = False
    while not done:
        done = simulation.runTimeStep()
    