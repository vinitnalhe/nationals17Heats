
from service import participantService, heatService

ps = participantService.participantService()
hs = heatService.heatService()
EVENTS = ['333','222','444','555','666','777','333bf','333fm','333oh','333ft','minx','pyram','clock','skewb','sq1','444bf','555bf','333mbf']
class verifyService(object):

    def __init__(self):
        pass


    def verifyAllHeats(self):
        heats = hs.getAllHeats()
        events = {}
        for heat in heats:
            if heat.event not in events:
                events[heat.event] = []

            events[heat.event].append(heat)

        if len(events.keys())  == 20:
            print "20 Events inlcuding intro and Lunch"


    def verifyRegistration(self):
        participants = ps.getAllParticipants()
        for participantName, participant in participants.iteritems():
            for event in EVENTS:
                if participant.isParticipating(event):
                    fl = False
                    for h in participant.getHeats():
                        if h.event == event:
                            fl = True
                            break
                    if not fl:
                        print  event
