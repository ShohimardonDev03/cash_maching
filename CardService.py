
from CardDb import CardDb;
from Card import Card;
cardDb=CardDb();
class CardService :
 
    
 def getCardByPanAndPin(self,pan,pin):
   
  card =cardDb.getCardByPan(pan);
   
  if card != None and card.pin== pin:
       
       return card;
  else: 
    return None;   

 def getCard(self):
   return cardDb.getCard() 