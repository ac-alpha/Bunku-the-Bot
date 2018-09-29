# See readme.md for instructions on running this code.

import copy
import importlib
from math import log10, floor
import datetime
import re

from typing import Any, Dict, List

def is_float(value: Any) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

# Rounds the number 'x' to 'digits' significant digits.
# A normal 'round()' would round the number to an absolute amount of
# fractional decimals, e.g. 0.00045 would become 0.0
# 'round_to()' rounds only the digits that are not 0.
# 0.00045 would then become 0.0005.

def round_to(x: float, digits: int) -> float:
    return round(x, digits-int(floor(log10(abs(x)))))

class BunkuHandler(object):
    '''
    This plugin allows users to make conversions between various units,
    e.g. Celsius to Fahrenheit, or kilobytes to gigabytes.
    It looks for messages of the format
    '@mention-bot <number> <unit_from> <unit_to>'
    The message '@mention-bot help' posts a short description of how to use
    the plugin, along with a list of all supported units.
    '''
    

    def usage(self) -> str:
        return '''
               Lorem ipsum dolor sit amet
               '''

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


tt=[{"t8_9":"","t9_10":"min106","t10_11":"csn221","t11_12":"csn291","t12_1":"","t2_3":"","t3_4":"min106","t4_5":"ecn203","t5_6":"hss01"},\
{"t8_9":"hss01","t9_10":"min106","t10_11":"ecn203","t11_12":"csn291","t12_1":"","t2_3":"","t3_4":"csn291","t4_5":"min106","t5_6":""},\
{"t8_9":"","t9_10":"ecn203","t10_11":"csn221","t11_12":"","t12_1":"","t2_3":"","t3_4":"csn261","t4_5":"","t5_6":""},\
{"t8_9":"hss01","t9_10":"min106","t10_11":"ecn203","t11_12":"csn221","t12_1":"csn291","t2_3":"csn221","t3_4":"","t4_5":"","t5_6":""},\
{"t8_9":"","t9_10":"","t10_11":"","t11_12":"","t12_1":"","t2_3":"","t3_4":"","t4_5":"","t5_6":""}]
leaverecord = {"min106":3,"csn221":2,"csn291":2,"csn261":3,"ecn203":1,"hss01":0}
workingdays = {"startsession":"2018-07-23","endsession":"2018-11-10","min106":40,"csn221":40,"csn291":20,"csn261":20,"ecn203":40,"hss01":30}

def get_bot_converter_response(message: Dict[str, str], bot_handler: Any) -> str:
    content = message['content']
    original_sender = message['sender_email']

    msg_response="**"+original_sender+"** "
    
    if message['content'] == '' or message['content'] == 'help':
        return help_content

    if message['content'] == 'startrecording':
        startrecording(original_sender)
        msg_response += "Started recording your attendance"
    elif message['content'] == 'attendancerecord':
        msg_response+="\n---Stats---\n"
        for course in leaverecord:
            msg_response+=course+"\t:\t"
            daystillnow = daysTillNow(course)
            leavestillnow = leaverecord[course]
            daysattendedtillnow = daystillnow-leavestillnow
            msg_response+=str(daysattendedtillnow)+"/"+str(daystillnow)
            perc = int((daysattendedtillnow/float(daystillnow)) * 10000)/100.0
            msg_response+="\t"+str(perc)+"%\n"
        msg_response+="-----------"
    
    words = content.lower().split()

    
    if(len(words)==1):

        if(words[0].strip()=="left"):
            currTime = datetime.datetime.now().time().hour
            if(8<=currTime<=17):
                currDay = datetime.datetime.today().weekday();
                dayText=tt[currDay]
                dayTimeTableList = dayText.split("~");
                currSubCode = dayTimeTableList[currTime-8].strip()
                if(currSubCode==""):
                    msg_response="No classes now. Type \"@bunku help\""
                else:
                    msg_response="Leave for "+currSubCode+" recorded\n"
                    bot_handler.storage.put("leaves",currSubCode+"-1")
            else:
                msg_response="No classes now. Type \"@bunku help\"" 

        elif(words[0].strip()=="startdate"):
            startDate=bot_handler.storage.get("startDate")
            msg_response= startDate+" is the start date of the session."

        elif(words[0].strip()=="enddate"):
            endDate=bot_handler.storage.get("endDate")
            msg_response = endDate+" is the start date of the session."
        
        elif(words[0].strip()=="startrecording"):
            bot_handler.storage.put("leaveRecord",convertRecordToString(leaverecord))
            msg_response += "Started recording the leaves now... Happy bunking!"
        
        elif(words[0].strip()=="rawrecords"):
            rawrecord = bot_handler.storage.get("leaveRecord")
            msg_response += rawrecord


    elif(len(words)==2):

        if(words[0]=="startsession"):
            date=words[1].strip()
            if(len(date)==10 and date[0].isdigit() and date[1].isdigit() and date[3].isdigit() and date[4].isdigit() and date[6].isdigit() and date[7].isdigit() and\
                date[8].isdigit() and date[9].isdigit() ):
                bot_handler.storage.put("startDate",date)
                msg_response=date+" is set as start date."
            else:
                msg_response = "Enter date in required format"

        elif(words[0]=="endsession"):
            date=words[1].strip()
            if(len(date)==10 and date[0].isdigit() and date[1].isdigit() and date[3].isdigit() and date[4].isdigit() and date[6].isdigit() and date[7].isdigit() and\
                date[8].isdigit() and date[9].isdigit() ):
                bot_handler.storage.put("endDate",date)
                msg_response=date+" is set as end date."
            else:
                msg_response = "Enter date in required format"
        else:
            msg_response="I don't know how to respond to that. Type \"@bunku help\""
                
    return msg_response

def convertRecordToString(leaverecord):
    recordString=""
    for course in leaverecord:
        for elem in course:
            recordString+=str(elem)+"~"
        recordString+="\b$"
    recordString+="\b"
    return recordString

def convertStringToRecord(recordString):
    recordString=recordString[:len(recordString)-1]
    recordList=recordString.split("$")
    temp=[]
    for record in recordList:
        record=record.strip().split("~")
        record[1]=int(record[1])
        record[2]=int(record[2])
        record[3]=int(record[3])
        temp.append(record)
    return temp

def startrecording(email):
    pass

def daysTillNow(courseCode):
    startDate = workingdays["startsession"]
    hrsEachDay=[]
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


