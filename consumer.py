class Consumer:
    curr_funds = 0
    prefs = []
    risk_tolerance = 0.0
    awareness = []
    neighbors = []

    # No awareness on initialization, can change if we want consumers to start with some pre-knowledge
    def __init__(self, funds, preferences, risk_tolerance, neighbors):
        self.curr_funds = funds
        self.prefs = preferences
        self.risk_tolerance = risk_tolerance
        self.neighbors = neighbors

    def speculativeValue(self, genre, campaign_goal, curr_campaign_funds):
        # TODO: calculate a speculative value for the given parameters
        pass

    # Nice wrapper for other speculativeValue()
    def speculativeValue(self, producer):
        val = self.speculativeValue(producer.genre, producer.campaign_goal, producer.current_funds)
        return val

    def modifyPreference(self, genre, modifier):
        # TODO: modify preference by the modifier amount
        pass

    def notifyNeighbors(self, producer):
        # TODO:
        pass

    def buy(self, producer):
        # TODO: check if already contributed
        contrib = self.speculativeValue(producer)
        producer.addContribution(contrib)
        self.curr_funds -= contrib
