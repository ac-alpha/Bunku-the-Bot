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

def put_time_table(bot_handler: Any):
    bot_handler.storage.put("timetable", tt)

help_content = "lorem ipsum dolor sit amet"

tt = " ~MIN106L~CSN221L~CSN291L~ ~ ~ ~MIN106T~ECN203T~HSS01T#HSS01L~MIN106L~ECN203L~CSN291L~ ~ ~CSN291P~CSN291P~MIN106P~MIN106P# ~ECN203L~CSN221L~ ~ ~ ~ ~CSN261P~CSN261P~CSN261P#"+\
        "HSS01L~MIN106L~ECN203L~CSN221L~CSN291L~ ~CSN221T~ ~ ~ # ~ ~ ~ ~ ~ ~ ~ ~ ~ # ~ ~ ~ ~ ~ ~ ~ ~ ~ # ~ ~ ~ ~ ~ ~ ~ ~ ~ "

def get_bot_converter_response(message: Dict[str, str], bot_handler: Any) -> str:
    content = message['content']

    
    if message['content'] == '' or message['content'] == 'help':
        return help_content
    
    words = content.lower().split()

    msg_response="Blank"
    if(len(words)==1):
        if(words[0].strip()=="left"):
            currTime = 9
            if(8<=currTime<=17):
                currDay = 0
                dayText=bot_handler.storage.get("timetable").split("~")[currDay]
                dayTimeTableList = dayText.split("~");
                currSubCode = dayTimeTableList[currTime-8].strip()
                if(currSubCode==""):
                    msg_response="No classes now. Type \"@bunku help\""
                else:
                    msg_response="Leave for "+currSubCode+" recorded\n"
            else:
                msg_response="No classes now. Type \"@bunku help\"" 
        elif (words[0].strip()=="updateTT"):  
            msg_response="Updated timetable successfully"          
            put_time_table(bot_handler)
            
    return msg_response

handler_class = BunkuHandler
