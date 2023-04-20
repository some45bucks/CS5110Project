import random


class Consumer:
    curr_funds = 0
    risk_tolerance = 0.0001
    id = 0
    # TODO: Add true preferences of producers
    
    #hidden values

    # No awareness on initialization, can change if we want consumers to start with some pre-knowledge
    def __init__(self, id, funds, preferences, risk_tolerance, true_prefs):
        self.id = id
        self.curr_funds = funds
        self.prefs = preferences
        self.risk_tolerance = risk_tolerance
        self.neighbors = {}
        self.producers = {}
        self.prefs = preferences
        self.true = true_prefs

    def _speculativeValue(self, genre, campaign_goal, curr_campaign_funds):
        percentageDone = curr_campaign_funds/campaign_goal
        genrePrefrence = self.prefs[genre]

        return ((percentageDone+1)/self.risk_tolerance)*genrePrefrence

    # Nice wrapper for _speculativeValue()
    def speculativeValue(self, producer):
        if not self.prefs.contains(producer):
            return 0  # No value for projects this consumer is unaware of
        val = self._speculativeValue(producer.genre, producer.campaign_goal, producer.curr_funds)
        return val

    def modifyPreference(self, genre, modifier):
        self.prefs[genre] = modifier            

    def buy(self, producer):
        contrib = self.speculativeValue(producer)
        if (self.speculativeValue(producer) - producer.getContributions(self))/100 > .6:
            # If we have already contributed, only contribute again if the speculative value is
            # significantly greater (>60%) than the total previous contributions
            if contrib <= self.curr_funds:
                # Ensure we have enough funds to contribute fully
                producer.addContribution(contrib)
                self.curr_funds -= contrib
        
    def getId(self):
        return f"Consumer_{self.id}"
