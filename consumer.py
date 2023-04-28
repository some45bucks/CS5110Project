class Consumer:
    curr_funds = 0
    risk_tolerance = 0.0001
    id = 0

    # No awareness on initialization, can change if we want consumers to start with some pre-knowledge
    def __init__(self, id, funds, preferences, risk_tolerance):
        self.id = id
        self.curr_funds = funds
        self.spent = 0
        self.prefs = preferences
        self.risk_tolerance = risk_tolerance
        self.neighbors = {}
        self.producers = {}

    def _speculativeValue(self, genre, campaign_goal, curr_campaign_funds, awareness):
        percentageDone = curr_campaign_funds/campaign_goal
        genrePrefrence = self.prefs[genre]

        return ((percentageDone+1)/self.risk_tolerance)*genrePrefrence*awareness

    # Nice wrapper for _speculativeValue()
    def speculativeValue(self, producer):
        if producer.id not in self.producers:
            return 0  # No value for projects this consumer is unaware of
        val = self._speculativeValue(producer.genre, producer.campaign_goal, producer.curr_funds, self.producers[producer.id])
        return val

    def modifyPreference(self, genre, modifier):
        self.prefs[genre] = modifier            

    def buy(self, producer):
        contrib = self.speculativeValue(producer)
        contribSoFar = producer.getContributions(self)
        if contrib <= 0:
            return  # Don't buy if not a positive value
        
        diff = contrib - contribSoFar
        if diff > 0:
            if diff <= self.curr_funds:
                # Ensure we have enough funds to contribute fully
                producer.addContribution(self,diff)
                self.curr_funds -= diff
                self.spent += diff
        
    def getId(self):
        return f"Consumer_{self.id}"