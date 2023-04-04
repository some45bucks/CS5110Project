from simulation import Simulation 
from graph import Graph
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a simulation.')
    parser.add_argument('-n', type=int, default=5, help='consumers')
    parser.add_argument('-m', type=int, default=5, help='producers')
    parser.add_argument('-p', type=float, default=0.4, help='probability of an edge existing')
    parser.add_argument('-sim', type=str, default='default', help='simulation type')
    args = parser.parse_args()

    graph = Graph(args.n, args.m, args.p)

    if args.sim == 'default':
        simulation = Simulation(graph)
    elif args.sim == 'custom':
        #other code
        pass
    else:
        raise ValueError('Invalid simulation type')

    done = False
    while not done:
        done = simulation.runTimeStep()
    