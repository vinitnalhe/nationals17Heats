import pdfkit
class iternaryService(object):

    def __init__(self):
        pass


    def writeIternaryToPdf(self, participantName,  heats):
        fileName = 'iternaries/' + participantName + '.pdf'
        pdfkit.from_string(self.getHtmlString(participantName, heats), fileName)

    def getHtmlString(self, participantName, heats):
        template = open('files/iternary.html').read()
        template = template.replace('{{main}}', self.getHeatsHtml(heats))
        template = template.replace('{{name}}', participantName)

        return template


    def getHeatsHtml(self, heats):
        html = ''
        for heat in heats:
            html += self.getHeatHtml(heat)
        return html

    def getHeatHtml(self, heat):

        fields = [heat.startTime.strftime('%d-%m'), heat.event, heat.round, heat.heatNo,
                  heat.roomNo,heat.startTime.strftime("%H:%M") + '-' +heat.endTime.strftime("%H:%M") ]


        res = '<tr class = ' + self.getClassForTr(heat) +' >'
        for f in  fields:
            res += '<td>' + f+ '</td>'
        return  res + '</tr>'

    def getClassForTr(self, heat):
        if (heat.event not in ['333mbf', '333fmc']) and int(heat.round) > 1:
            return 'warning'
        return 'success'
