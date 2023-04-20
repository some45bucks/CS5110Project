class Producer:
    curr_funds = 0
    campaign_goal = 0
    total_ad_spending = 0
    genre = None
    id = 0

    def __init__(self, id, funds, goal, genre):
        self.id = id
        self.curr_funds = funds
        self.campaign_goal = goal
        self.genre = genre
        self.contributors = dict()
        
    #some sort of market measure
    #update on advertise
    def advertise(self):
        if self.campaign_goal <= self.curr_funds:
            spendAmount = 0
        else:
            spendAmount = self.curr_funds *.05
        self.curr_funds -= spendAmount
        self.total_ad_spending += spendAmount
        return spendAmount
    
    def addContribution(self, contributor, contribution):
        if not self.contributors.keys().__contains__(contributor):
            self.contributors[contributor] = 0
        # Add to this contributor's total contribution
        self.contributors[contributor] += contribution
        self.curr_funds += contribution

    def getContributions(self, contributor):
        if not self.contributors.__contains__(contributor):
            return 0
        return self.contributors[contributor]

    def getId(self):
        return f"Producer_{self.id}"
