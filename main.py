from Card import Card;
from CardService import CardService;
from Util import Util;
import os


cardService=CardService();

def   clearConsole():
 os.system("clear");
    
def checkCard(pin, pan):
    
 
 
  card=cardService.getCardByPanAndPin(pan,pin);
  
  if(card == None):
     clearConsole()
     Util.print_error ("Card pan or pin invalid!\n\n");
     main();    
    
  else:
   cardInside()
   
   
   # User menu
def sms_section(card):
 Util.print_success("Sms section");
 b=False;
 if card.sms_notification :
     b=True
 
    
 text="";
 if b:
  text="o'richirishni xoxlaysizmi"
 else:
  text="yoqishni xoxlaysizmi"

 print("Carta sms xabarnomasi {text}".format(text=text))
 Util.print_error("1 - Xa \t\t0 - Yo'q")
 
 if(input("-> ")=="1"):
    card.sms_notification=not bool(card.sms_notification);
   
    
 else:
    cardInside();
 

def card_balance():
 Util.print_success("Card balance");
 
 card =cardService.getCard();

 
 print(Util.COLOR_GREEN+card.firstName+" "+ card.firstName)
 Util.print_error("You have : "+str(card.cash)+" $")
 print("Back - 0")
 input("->")   

def card_info():
    card =cardService.getCard();
    Util.print_success("Card info") 
    print("------------------------------")
    Util.print_success("First name : "+card.firstName)
    Util.print_success("Last  name : "+card.lastName)
    Util.print_success("Card balanace : "+str(card.cash))
    Util.print_success("Card number : "+str(card.pan))
    
    print("Back - 0")
    input("->")   

def cash(card):
 Util.print_success("Cash")
 
 print("Your balanace ({balance})".format(balance=card.cash))
 
 print ("1 - 20 000 \t\t 2 - 40 000")
 print ("3 - 80 000 \t\t 4 - 100 000")
 print ("5 - 200 000 \t\t 6 - 300 000")
 print ("7 - 400 000 \t\t 8 - 500 000")
 print("* - Qo'lda kiritish")
 print("0 - back")
 select = input("-> ")
 
 if select == "1":
     get_cash(20_000,card);
 elif select == "2":
     get_cash(40_000,card);
 elif select == "3":
     get_cash(80_000,card);
 elif select == "4":
     get_cash(100_000,card);
 elif select == "5":
     get_cash(200_000,card);
 elif select == "6":
     get_cash(300_000,card);
 elif select == "7":
     get_cash(400_000,card);
 elif select == "8":
     get_cash(500_000,card);
 elif select == "*":
     get_cash(0,card);
 else:
     cardInside();
    
 
 
def get_cash(amount,card):
     
     
     if amount != 0:
         input("Check chiqarishini hohlaysimi ? \n 1 - Xa \t\t 2 - Yo'q\n -> ")
         if(card.cash < amount):
           print("Mablag' yetarli.Iltimos boshqa mablag' kiriting")
           
           cash(card);
         else:    
           card.cash=card.cash-amount;
           cardInside();
     else:
         get_cash(input("Iltimos miqdorini kiriting"),card);
    
     
     
 
def change_pin(card):
    Util.print_success("Change pin")
    print("Enter old password")
    old_p=input("-> ");
    if(cardService.getCardByPanAndPin("2003",old_p) == None):
        clearConsole();
        Util.print_error("Parol mos kelmadi")
        change_pin(card);
        return;
    
    new_p=input("Yangi parol kiriting\n-> ")
    conform_p=input("Tastiqlash parol kiriting\n-> ")
    if  (new_p  != conform_p):
        clearConsole();
        Util.print_error("Parol mos kelmadi")
        change_pin(card);
        return;
    
    card.pin=new_p;
    print("Succesfully changes password\n0 - Back")       
    input("-> ")
    
# / User menu 
  
  
def cardInside():
    clearConsole()
    Util.print_success("1 - Sms xabarnoma \t\t 2 - Karta balansi")
    Util.print_success("3 - Pin o'zgartirish \t\t 4 - Naqt pul olish")
    Util.print_success("5 - Karta ma'lumotlari \t\t")
    Util.print_success("0 - Kartani chiqarish")
    select = input("Select: ")
    clearConsole();
    card =cardService.getCard();

    if select == "1":
     sms_section(card);    
    elif select == "2":
     card_balance()    
    elif select == "3":
        change_pin(card)
    elif select == "4":
        cash(card)
    elif select == "5":
        card_info()
    
       
 
    elif select == "0":
        Util.print_error("Bye bye")
        return;
    else:
        print("Value is not 1, 2, or 3");
        clearConsole()
        cardInside()
    cardInside();
  
  
      

  





def main():
     tmp_card_number="";
     tmp_card_pin=""
     print (Util.COLOR_GREEN+"Welcome to Cashing machine")
     tmp_card_number=input(Util.COLOR_YELLOW+"Please input card number : ");
     tmp_card_pin=input(Util.COLOR_YELLOW+"Please input password : ")
    
     checkCard(tmp_card_pin,tmp_card_number)
     


# Main
main();    

# Main




