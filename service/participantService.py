from classes.participant import Participant
import datetime
import csv

PATICIPANTS_FILE_PATH = 'files/participants.csv'
# move this sometime into events class
EVENTS = ['333','222','444','555','666','777','333bf','333fm','333oh','333ft','minx','pyram','clock','skewb','sq1','444bf','555bf','333mbf']


class participantService(object):
    _instance = None
    _initialized = False
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(participantService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not participantService._initialized :
            participantService._initialized = True
            self.allParticiapants = self.loadAllParticipants()



    def getEvents(self, participantDic):
        ev = []
        for i in EVENTS:
            ev.append(participantDic[i] == '1')
        return ev

    def getParticipant(self, nm):
        return self.allParticiapants[nm]

    def getAllParticipants(self):
        return self.allParticiapants

    def loadParticipantObj(self, participantDic):
            name = participantDic['Name']
            country = participantDic['Country']
            wcaId = participantDic['WCA ID']
            dob = datetime.datetime.strptime(participantDic['Birth Date'], '%Y-%m-%d')
            gender = participantDic['Gender']
            email = participantDic['Email']
            events = self.getEvents(participantDic)
            p = Participant(name, country, wcaId, dob, gender, email, events)
            return p

    def loadAllParticipants(self):
        print 'loading Participants'
        participants =  list(csv.DictReader(open(PATICIPANTS_FILE_PATH)))
        participantDic = {}
        for participant in participants:
            p = self.loadParticipantObj(participant)
            participantDic[p.getName()] = p

        return participantDic