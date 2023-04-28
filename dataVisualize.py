import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from genre import Genre
import numpy as np

class Visualizer:
    
    colorMap = ['red','green','blue','yellow','purple','orange']
       
    def __init__(self, producers,steps,tests):
        self.steps = steps
        self.tests = tests
        self.producer_data = {}
        self.marketPrefs = {}

        self.averageCompleted = 0
        self.testsCompleted = 0
        
        self.averageStrat = 0
        self.averageStratGoal = 0
        self.averageTimeToGoal = 0
        self.averageMoneyMade = 0
        self.averageMoneyMadeGoal = 0
        self.averageGoal = 0
        self.averageGoalGoal = 0
        self.averageSpentProducer = 0
        self.averageSpentProducerGoal = 0
        self.averageSpentConsumer = 0
        
        for g in Genre:
            self.marketPrefs[g] = np.zeros(steps)

        for producer in producers:
            self.producer_data[producer.id] = {'current_funds': np.zeros(steps),'g':producer.genre,'s':producer.strategy,'reached':False}

    def update(self, producers, marketPrefs, step):
        for g in Genre:
            self.marketPrefs[g][step] += marketPrefs[g.value]
        for producer in producers:
            self.producer_data[producer.id]['current_funds'][step] += producer.curr_funds
            if producer.campaign_goal <= producer.curr_funds and not 'goal' in self.producer_data[producer.id]:
                self.producer_data[producer.id]['reached'] = True
                self.producer_data[producer.id]['goal'] = [producer.campaign_goal for i in range(len(self.producer_data[producer.id]['current_funds']))]
    
    def updateData(self,producers,consumers):
        goalStep = 0
        
        for producer in producers:
            if producer.goalComplete != -1:
                goalStep += 1
        
        if goalStep > 0:
            self.testsCompleted += 1
        
        for producer in producers:

            if producer.goalComplete != -1 and goalStep > 0:
                self.averageStratGoal += producer.strategy/goalStep
                self.averageTimeToGoal += producer.goalComplete/goalStep
                self.averageGoalGoal += producer.campaign_goal/goalStep
                self.averageMoneyMadeGoal += producer.curr_funds/goalStep
                self.averageSpentProducerGoal += producer.total_ad_spending/goalStep
                self.averageCompleted += 1/goalStep
            
            self.averageStrat += producer.strategy/len(producers)
            self.averageGoal += producer.campaign_goal/len(producers)    
            self.averageMoneyMade += producer.curr_funds/len(producers)
            self.averageSpentProducer += producer.total_ad_spending/len(producers)
        
        for consumer in consumers:
            self.averageSpentConsumer += consumer.spent/len(consumers)
               
    def visualize(self):
        if self.tests == 1:
            plt.figure()
            for genre_id, data in self.marketPrefs.items():
                plt.plot(data/self.tests,label=f"{genre_id.name}",color=self.colorMap[genre_id.value])
            plt.title('Consumer Prefrences Over Time')
            plt.xlabel('Time')
            plt.ylabel('Prefrence')
            plt.legend()
            
            plt.figure()
            for producer_id, data in self.producer_data.items():
                plt.plot(data['current_funds'],color=self.colorMap[data['g'].value])
            plt.title('Producer Money Over Time')
            plt.xlabel('Time')
            plt.ylabel('Money')
            
            plt.figure()
            for producer_id, data in self.producer_data.items():
                plt.plot(data['current_funds'],color=self.colorMap[data['reached']])
                if data['reached']:
                    plt.plot(data['goal'], color = 'blue', linestyle='dashed')
            plt.title('Producer Goal Reaching')
            plt.xlabel('Time')
            plt.ylabel('Money')
            plt.legend([Line2D([0], [0], color='red',),Line2D([0], [0], color='green',),Line2D([0], [0], color='blue',linestyle='dashed')], ['Failed','Completed','Goal'])
                
            plt.figure()
            for producer_id, data in self.producer_data.items():
                plt.plot(data['current_funds'],color=(0, 0, data['s']))
            plt.title('Producer Strategy')
            plt.xlabel('Time')
            plt.ylabel('Money')
            plt.legend([Line2D([0], [0], color='black'),Line2D([0], [0], color='blue')], ['Strategy A','Strategy B'])

        plt.figure()
        totp = np.zeros(self.steps)
        for genre_id, data in self.marketPrefs.items():
            totp += data/self.tests
        plt.plot(totp/len(self.marketPrefs.items()),color='grey')
        plt.title('Average Consumer Prefrences Over Time')
        plt.xlabel('Time')
        plt.ylim(-1, 1)
        plt.ylabel('Prefrence')
        
        plt.figure()
        tot = np.zeros(self.steps)
        for producer_id, data in self.producer_data.items():
            tot += data['current_funds']/self.tests
        plt.plot(tot/len(self.producer_data.items()),color='grey')
        plt.title('Average Producer Over Time')
        plt.xlabel('Time')
        plt.ylabel('Money')

        if self.testsCompleted > 0:
            print("Goal Completing Producers")
            print(f" Percentage Completed Goal: {(self.averageCompleted/self.testsCompleted)/len(self.producer_data.items())}")
            print(f" Average Strategy (0:A, 1:B): {self.averageStratGoal/self.testsCompleted}")
            print(f" Average Time to Goal: {self.averageTimeToGoal/self.testsCompleted}")
            print(f" Average Goal amount: {self.averageGoalGoal/self.testsCompleted}")
            print(f" Average Money Made: {self.averageMoneyMadeGoal/self.testsCompleted}")
            print(f" Average Money Spent: {self.averageSpentProducerGoal/self.testsCompleted}")
            print("")
        print("All Producers")
        print(f" Average Strategy (0:A, 1:B): {self.averageStrat/self.tests}")
        print(f" Average Goal amount: {self.averageGoal/self.tests}")
        print(f" Average Money Made: {self.averageMoneyMade/self.tests}")
        print(f" Average Money Spent: {self.averageSpentProducer/self.tests}")
        print("")
        print("Consumers")
        print(f" Average Money Spent: {self.averageSpentConsumer/self.tests}")
        print(f" Average Start Prefs: {[self.marketPrefs[g][0]/self.tests for g in Genre]}")
        print(f" Average End Prefs: {[self.marketPrefs[g][-1]/self.tests for g in Genre]}")
        
        plt.show()