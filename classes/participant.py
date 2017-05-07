
# move this sometime into events class
EVENTS = ['333','222','444','555','666','777','333bf','333fm','333oh','333ft','minx','pyram','clock','skewb','sq1','444bf','555bf','333mbf']

class Participant:
    def __init__(self, name, country,  wcaId, dob, gender, email, events):
        self.name = name
        self.country = country
        self.wcaId = wcaId
        self.dob = dob
        self.gender = gender
        self.email = email
        self.events = events
        self.heats = []


    def isParticipating(self, event):
        if event not in EVENTS:
            return False
        return self.events[EVENTS.index(event)]

    def addHeat(self, heat):
        self.heats.append(heat)

    def getHeats(self):
        return self.heats

    def getName(self):
        return self.name

    def getIternary(self):
        heats = self.heats
        heats.sort(key=lambda r: r.startTime)
        return heats

    def __repr__(self):
        return '<' + self.name + '>'