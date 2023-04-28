from simulation import Simulation 
from graph import Graph
import argparse
from dataVisualize import Visualizer 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a simulation.')
    parser.add_argument('-n', type=int, default=20, help='producers')
    parser.add_argument('-m', type=int, default=400, help='consumers')
    parser.add_argument('-p', type=float, default=0.4, help='probability of an edge existing')
    parser.add_argument('-s', type=int, default=30, help='number of steps')
    parser.add_argument('-t', type=int, default=30, help='number of tests')
    parser.add_argument('-cm', type=int, default=100, help='number of tests')
    parser.add_argument('-pg', type=int, default=200, help='number of tests')
    args = parser.parse_args()
    
    tests = args.t
    
    for i in range(tests):
        graph = Graph(args.n, args.m, args.p)
        if i == 0:
            vis = Visualizer(graph.producers,args.s,tests)
        simulation = Simulation(graph,args.s)
        simulation.addProGoals(args.pg)
        simulation.addConFunds(args.cm)

        done = False
        while not done:
            done,producers,market,step = simulation.runTimeStep()
            vis.update(producers,market,step)

        vis.updateData(graph.producers,graph.consumers)
    vis.visualize()