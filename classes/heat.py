class Heat:
    def __init__(self, event, round, heatNo, roomNo, st, et):
        self.event = event
        self.round = round
        print 'round', round
        self.heatNo = heatNo
        self.roomNo = roomNo
        self.startTime = st
        self.endTime = et
        self.participants = []

    def getName(self):
        return '-'.join(map(str, [self.event, self.round, self.heatNo]))


    def addParticipant(self, participant):
        self.participants.append(participant)
        participant.addHeat(self)

    def getParticipants(self):
        return self.participants

    def __repr__(self):
        return '<' + self.event + ' Round ' + self.round +' Heat ' + self.heatNo +'>'
