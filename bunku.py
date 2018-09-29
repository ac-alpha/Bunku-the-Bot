# See readme.md for instructions on running this code.

import copy
import importlib
from math import log10, floor
import datetime
import re
import graphql

from typing import Any, Dict, List

class BunkuHandler(object):
    '''
    '''
    

    def usage(self) -> str:
        return "Hey there! I am Bunku. I am here to help you out this semester and many more.\n\
Type the following and make me help you:\n\
@Bunku startrecording : to start recording your leaves\n\
@Bunku left <course-code> class : to record a leave for particular course code\n\
@Bunku <course-code> class cancelled : to report about a course class cancelled\n\
@Bunku extra class <course-code> : to report about an extra class\n\
@Bunku attendancerecord : to show your attendance record"

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        bot_response = get_bot_converter_response(message, bot_handler)
        bot_handler.send_reply(message, bot_response)

help_content = "Hey there! I am Bunku. I am here to help you out this semester and many more.\n\
Type the following and make me help you:\n\
@Bunku startrecording : to start recording your leaves\n\
@Bunku left <course-code> class : to record a leave for particular course code\n\
@Bunku <course-code> class cancelled : to report about a course class cancelled\n\
@Bunku extra class <course-code> : to report about an extra class\n\
@Bunku attendancerecord : to show your attendance record"

def get_bot_converter_response(message: Dict[str, str], bot_handler: Any) -> str:
    content = message['content']
    original_sender = message['sender_email']

    msg_response="**"+original_sender+"** "
    
    if message['content'] == '' or message['content'] == 'help':
        return help_content

    if message['content'] == 'startrecording':
        graphql.startRecording(original_sender)
        msg_response += "Started recording your attendance"
    elif message['content'] == 'attendancerecord':
        msg_response+="\n---Stats---\n"
        for course in graphql.getLeaveStats(original_sender):
            msg_response+=course+"\t:\t"
            daystillnow = daysTillNow(course)
            leavestillnow = graphql.getLeaveStats(original_sender)[course]
            daysattendedtillnow = daystillnow-leavestillnow
            msg_response+=str(daysattendedtillnow)+"/"+str(daystillnow)
            perc = int((daysattendedtillnow/float(daystillnow)) * 10000)/100.0
            msg_response+="\t"+str(perc)+"%\n"
        msg_response+="-----------"
    
    words = content.lower().split()
    if(len(words)==3):
        courses = list(graphql.getLeaveStats.keys())
        if(words[0].lower().strip()=="left" and words[2].lower().strip(=="class")):
            courseCode = words[1].lower()
            if courseCode in courses:
                graphql.updateLeave(original_sender,courseCode)
                msg_response+="Leave for "+courseCode+" recorded successfully. Try \"@Bunku attendancerecord\" for leave stats"
            else:
                msg_response+="Sorry! I don't know which course is that. Try \"@Bunku help\""
        elif(words[1].lower().strip()=="class" and words[2].lower().strip()=="cancelled"):
            courseCode = words[0].lower().strip()
            if courseCode in courses:
                graphql.cancelClass(courseCode)
                msg_response+="Class of "+courseCode+" has been cancelled."
            else:
                msg_response+="Sorry! I don't know which course is that. Try \"@Bunku help\""
        elif(words[0].lower().strip()=="extra" and words[1].lower().strip()=="class"):
            courseCode = words[2].lower().strip()
            if courseCode in courses:
                graphql.extraClass(courseCode)
                msg_response+="Extra Class of "+courseCode+" has been recorded."
            else:
                msg_response+="Sorry! I don't know which course is that. Try \"@Bunku help\""
        else:
            msg_response+="Sorry! I don't know how to respond to that. Try \"@Bunku help\""
    else:
        msg_response+="Sorry! I don't know how to respond to that. Try \"@Bunku help\""
                
    return msg_response


def daysTillNow(courseCode):
    startDate = graphql.getDaysInfo()["startsession"]    #workingdays["startsession"]
    hrsEachDay=[]
    tt=graphql.getTimeTable()
    for entry in tt:
        temp=0
        for time in entry:
            if entry[time]==courseCode.lower():
                temp+=1
        hrsEachDay.append(temp)
    fromdate = datetime.date(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
    todate = datetime.date.today()
    daygenerator = (fromdate + datetime.timedelta(x + 1) for x in range((todate - fromdate).days))
    weekdays=[0,0,0,0,0]
    for day in daygenerator:
        if (day.weekday() < 5):
            weekdays[day.weekday()]=weekdays[day.weekday()]+1
    totalClassesTillNow=0
    for i in range(5):
        totalClassesTillNow+=hrsEachDay[i]*weekdays[i]
    return totalClassesTillNow

        
handler_class = BunkuHandler


