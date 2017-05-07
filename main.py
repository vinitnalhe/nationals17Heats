# from service import heatService, participantService
# from classes.heat import Heat

from  service import heatService
from  service import participantService
from  service import verifyService
from  service import iternaryService
# heatsDay1Data = heatHelper.setHeatsData(1, heats['day1'])


h = heatService.heatService()
p = participantService.participantService()
v = verifyService.verifyService()
it = iternaryService.iternaryService()
v.verifyAllHeats()
v.verifyRegistration()
# for k, val in p.getAllParticipants().iteritems()[:1]:


allParticipants = p.getAllParticipants()
for participantName, participantObj in allParticipants.iteritems():
    it.writeIternaryToPdf(participantName, participantObj.getIternary())








