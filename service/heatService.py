from classes.heat import Heat
from service import participantService
import datetime
import csv

DAY1HEAT = 'files/day1Heats.csv'
DAY2HEAT = 'files/day2Heats.csv'
DAY3HEAT = 'files/day3Heats.csv'
DAY_HEAT_DATA ={
  1 :'files/heatDay1Data.csv'
}
day1 = datetime.datetime(2017,05,12)
days = {
    1 : datetime.datetime(2017,05,12),
    2 :datetime.datetime(2017,05,13),
    3 :datetime.datetime(2017,05,14)
}

ps = participantService.participantService()

class heatService(object):
    _instance = None
    _initialized = False
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(heatService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not heatService._initialized :
            heatService._initialized = True
            self.allHeats = self.loadAllHeats()
            self.setHeatsData()
            self.addOtherHeats()


    def loadAllHeats(self):
        print 'loading Heats'
        return {
            1 : self.loadHeats(list(csv.DictReader(open(DAY1HEAT))), 1),
            2 : self.loadHeats(list(csv.DictReader(open(DAY2HEAT))), 2),
            3 : self.loadHeats(list(csv.DictReader(open(DAY3HEAT))), 3)
        }


    def addOtherHeats(self):
        allHeats = self.getAllHeats()
        for heat in allHeats:
            if (heat.event not in ['333mbf', '333fmc']) and int(heat.round) > 1:
                allParticipants = ps.getAllParticipants()
                eventParticipants  = [participantObj for participantName, participantObj in allParticipants.iteritems() if participantObj.isParticipating(heat.event)]
                for participant in eventParticipants:
                    heat.addParticipant(participant)



    def getHeatForDay(self,dy):
        return self.allHeats[dy]

    def getAllHeats(self):
        allHeats = self.allHeats
        heats = []
        for i in allHeats:

            heats = heats + allHeats[i].values()

        return heats

    def loadHeats(self, heats, dy):
        heatDic = {}
        for heat in heats:
            event = heat['Event Name']
            round = heat['Round']
            heatNo = heat['Heat No']
            roomNo = heat['Room No']
            sH = int(heat['Start Hour'])
            sM = int(heat['Start Min'])
            eH = int(heat['End Hour'])
            eM = int(heat['End Min'])
            startTime = datetime.datetime.combine(days[dy], datetime.time(sH, sM))
            endTime = datetime.datetime.combine(days[dy], datetime.time(eH, eM))
            h = Heat(event, round, heatNo, roomNo, startTime, endTime)
            heatDic[h.getName()] = h
        return heatDic

    def parseHeatDataRow(self, row):
        dy = row['day']
        participant = ps.getParticipant(row['Name'])
        heatName = '-'.join(map(str, [row['event'], row['round'], row['heat']]))
        heatsForDay = self.getHeatForDay(int(dy))
        heatsForDay[heatName].addParticipant(participant)

    def setHeatsData(self):
        heatDayDataList = list(csv.DictReader(open(DAY_HEAT_DATA[1])))
        for row in heatDayDataList:
            if row['Name']: # hack to filter empty rows intentionally put to seperate events to increase readability
                self.parseHeatDataRow(row)
