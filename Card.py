
from dataclasses import dataclass
@dataclass
class Card:
    pan:str;
    pin:str;
    cash:int;
    firstName:str;
    lastName:str;
    sms_notification:bool;
 
 