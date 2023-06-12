from Card import Card;
class CardDb:
    
 list=[Card("2003","2003",50_000,"Shohimardon","Abdurashitov",False)];
 
    
 def getCardByPan(self,pan):
  for card in self.list :
   if card.pan== pan:
        return card;

  return None ;  

 def getCard(self):
      return  self.getCardByPan("2003");       

       
       
   