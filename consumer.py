import random

class Consumer:
    curr_funds = 0
    prefs = {}
    risk_tolerance = 0.0001
    id = 0
    neighbors = {}
    producers = {}

    # No awareness on initialization, can change if we want consumers to start with some pre-knowledge
    def __init__(self,id, funds, preferences, risk_tolerance):
        self.id = id
        self.curr_funds = funds
        self.prefs = preferences
        self.risk_tolerance = risk_tolerance

    def speculativeValue(self, genre, campaign_goal, curr_campaign_funds):
        percentageDone = curr_campaign_funds/campaign_goal
        genrePrefrence = self.prefs[genre]

        return ((percentageDone+1)/self.risk_tolerance)*genrePrefrence

    # Nice wrapper for other speculativeValue()
    def speculativeValue(self, producer):
        val = self.speculativeValue(producer.genre, producer.campaign_goal, producer.current_funds)
        return val

    def modifyPreference(self, genre, modifier):
        self.prefs[genre] += modifier            

    def buy(self, producer):
        # TODO: check if already contributed
        contrib = self.speculativeValue(producer)
        producer.addContribution(contrib)
        self.curr_funds -= contrib
        
    def getId(self):
        return f"Consumer_{self.id}"
