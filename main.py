from simulation import Simulation 
from graph import Graph
import argparse
from dataVisualize import Visualizer 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a simulation.')
    parser.add_argument('-n', type=int, default=10, help='producers')
    parser.add_argument('-m', type=int, default=100, help='consumers')
    parser.add_argument('-p', type=float, default=0.4, help='probability of an edge existing')
    parser.add_argument('-s', type=str, default='30', help='number of steps')
    args = parser.parse_args()
    
    tests = 500
    
    for i in range(tests):
        graph = Graph(args.n, args.m, args.p)
        if i == 0:
            vis = Visualizer(graph.producers,int(args.s),tests)
        simulation = Simulation(graph,int(args.s))
        simulation.addProGoals(200)
        simulation.addConFunds(100)

        done = False
        while not done:
            done,producers,market,step = simulation.runTimeStep()
            vis.update(producers,market,step)

        vis.updateData(graph.producers,graph.consumers)
    vis.visualize()