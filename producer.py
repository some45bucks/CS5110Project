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
        self.contributors = []
        
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
    
    
    def addContribution(self,contrib):
        # TODO: add awareness of the contributing consumer maybe?
        self.curr_funds += contrib
    
    def getId(self):
        return f"Producer_{self.id}"
