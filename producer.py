class Producer:
    curr_funds = 0
    campaign_goal = 0
    total_ad_spending = 0
    genre = None
    id = 0
    contributors = []

    def __init__(self, id, funds, goal, genre):
        self.id = id
        self.curr_funds = funds
        self.campaign_goal = goal
        self.genre = genre

    def advertise(self):
        spendAmount = self.curr_funds * .1
        
        self.curr_funds -= spendAmount
        
        self.total_ad_spending += spendAmount
        
        return spendAmount
        
        
