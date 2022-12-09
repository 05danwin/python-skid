import os
import time

class Spelare:
  def __init__(self, hp, dmg, rustning, mynt):
    self.hp = hp
    self.dmg = dmg
    self.rustning =  rustning
    self.mynt = mynt

class Monster:
  def __init__(self, namn, hp, dmg, rustning, svaghet, utseende):
    self.namn = namn
    self.hp = hp
    self.dmg = dmg
    self.rustning = rustning
    self.svaghet = svaghet
    self.utseende = utseende

# class Vapen:
#   def __init__(self, namn, dmg):
#     self.namn = namn
#     self.dmg = dmg


def strid(monster, spelare, namn): #DETTA ÄR STRIDSFUNKTIONEN SOM ANVÄNDER 
  print("tryck enter för att fortsätta...")
  while spelare.hp > 0 and monster.hp > 0:
    while True:
      input()
      rensa()
      print(f'''    
    \n A wild {monster.namn} appears!
    {monster.utseende}
    ''')
      print("-----------------------------\n1 SLÅSS --- 2 FLY --- 3 PRATA\n-----------------------------")
      print(f"{monster.namn} har {monster.hp} HP och {monster.dmg} DMG\n")
      print(f"{namn} har {spelare.hp} HP och {spelare.dmg} DMG")
      print()
      svar = input("Vad vill du göra? ")
      if svar == "1":
          print(f"\nTILLGÄNGLIGA VAPEN:\n 1 SVÄRDET")
          vapenval = input("\nVilket vapen väljer du? ")
          if vapenval == "1":
            print("Du valde svärdet och gör 5 dmg\n")
            monster.hp -= spelare.dmg
            print(f"{monster.namn} slår tillbaka och gör {monster.dmg} skada\n")
            spelare.hp -= monster.dmg
            if monster.hp <= 0:
              print(f"\n1 SLAKTA {monster.namn} --- 2 SKONA {monster.namn}")
              svar = int(input("Vad vill du göra?"))
              if svar == "1":
                print(r'''
               _--------_
             /            \
            |   .-.  .-.   |
            | )(__/  \__)( |
            |/     /\     \|
            (_     ^^     _)
             \__IIIIIIII__/
              | \IIIIII/ |
              \          /
               \________/
              ''')
                print(f"{monster.namn} ÄR DÖD\n")
                input()
                rensa()
                return 
            elif spelare.hp <= 0:
              print(f"{namn} ÄR DÖD")
              print("1 JA --- 2 NEJ\n")
              omstart = input("Vill du börja om?")
              if omstart == "1":
                monster.hp = 20
                spelare.hp = 25
                strid(monster,spelare,namn)
              elif omstart == "2":
                break
              else:
                print("Välj ett giltigt nummer")
            
          else:
            print("Välj ett giltigt nummer")
      elif svar == "2": 
        print(f"Din barmhärtighet uppskattas av {monster.namn}")
        return 
      elif svar == "2":
        spelare.dmg -= 1
        print(f"\nDu flyr och din omodighet minskar din dmg med 1. Din nya dmg är {spelare.dmg}")
        input()
        rensa()
        return
      elif svar == "3":
        if monster.namn == "Leif" and monster.hp > 10:
          print("Leif vill inte prata just nu, testa att mucka upp honom lite först")
          break
        elif monster.namn == "Leif" and monster.hp <= 10: 
          print("Leif är rädd och erbjuder pengar för att få lämnas i fred. Han har 10 guldmynt till sitt namn\n")
          print("1 JA --- 2 NEJ\n")
          svar = input("Accepterar du hans erbjudande?")
          if svar == "1":
            print("Leif springer kvickt bort och lämnar dig med 10 guldmynt")
            spelare.mynt += 10
            print(f"Du har nu {spelare.mynt} guldmynt")
          elif svar == "2":
            print("snorre")
      else:
            print("Välj ett giltigt nummer")

def skid(spelare):
  print("------------------------------------------------\n1 FORTSÄTT RESAN --- 2 RYGGSÄCK --- 3 REGELBOKEN\n------------------------------------------------")
  svar = input("vad vill du göra?")
  if svar == "1": 
    print("1 SHOPPEN --- 2 LÄGRET --- 3 ")
    print("Var vill du gå?")
  elif svar == "2": 
    print(f"Ditt inventory: ")
  elif svar == "3":
    print("--- REGLER OCH INSTRUKTIONER ---")
    print("1. Klicka enter för att forstätta dialog/funktioner \n2. Var inte en noob \n3. Var inte snorre på spelet")

    input()
    rensa()
    
  else:
    print("Välj ett giltigt nummer")


def rensa():
  os.system('cls' if os.name == 'nt' else 'clear')














def main():
  rensa()
  input("NÅGON GÅNG I TIDEN, I EN GALAX LÅNGT LÅNGT BORTA...     tryck enter för att forsätta")
  rensa()
  input("DU KÄNNER EN SVAL BRIS OCH SOLENS STARKA LJUS PÅ ÖGONLOCKEN. PLÖTSLIGT HÖR DU EN RÖST TALA TILL DIG.")
  rensa()
  input('''DET ÄR JAG SOM ÄR JESUS

                        ((())()))()())
                     ((( (          ) ) )    
                    ( )); ----,---- ; ( (
                   ( )((| `o- |`o-  | ) )
                   ) ) )|     |_    |)( (
                   ( ( (|   _____,  |( (
                      ) )\_       _/ ) )
                    (  )  ( `-----' ) ( (
                   )( _____/      \_____ )
                   ( /                  \ )
                 (( /        ..,,,.,,,.  \)
                   /   ..,..(          ).,\.
             ,..,,/,,,.(                    ).,..
          ,.(                                   ),,.,..,                         
        ,,                                            .,)
       (                                              )
        ,.,.                                       ,.)
            (,,,..                           ,,..,)
                  (,..,,.            ,.,,,.,)   
                         (...,,,,.,.)
''')
  rensa()
  namn = input("\"VEM ÄR DU?\"\nSKRIV DITT NAMN --> ")
  rensa()
  input(f"\"HEJ {namn}, DU BEFINNER DIG JUST NU PÅ PLANETEN BORÅSUS.\"").upper() 
  rensa()
  input("FÖRBERED DIG PÅ DIN FÖRSTA STRID {namn}.")
  rensa()

  # ALLA MONSTER:
  leif = Monster("Leif", 20, 10, 0, "Vass", r''' 
          [\__/]  
         / +  + \
    ⁂--- \vWWWWv/---⁅
          \____/
          I    I
          ₼₼  ₼₼  
''')

  rolf = Monster("Rolf", 30, 15, 3, "Trubbig", r'''
         _◺⨽₩₩₩₩₩⨼◿_
        |           |
       /   ⩊⩊⩊ ⩊⩊⩊   \
      |     ⨸   ⨸     |
      |    ⋀_____⋀    |   
       \             /
       ₼₼₼₼———————₼₼₼₼  
''')

  rune = Monster("Bettan", 60, 20, 3, "Vass", r'''
               _..--+~ ----__
           _-=~      ( .     )
        _-~     _.--=.\\´''```
      _~      _-       \\_\
     =      _=          '--'
    '      =                             .
   :      :                              '=_. ___
  |       ;                                  '~--.~.
  ;       ;                                       } |
  =        \            __..-...__             ~~ ~~~~
   :        =_     _.-~~          ~~--.__
  \            -+-                    ~~ ~~~~ ~~~ ~ 
  ~~~~ ~~ ~        ~~ ~~ ~~ ~~~~~ ~~~ ~~~  ~~ ~~ ~
      ~  ~~~~~  ~~         ~    ~~  ~~ ~~~ ~
''')
  

  # ALLA SPELARE (BARA EN):
  spelare = Spelare(30, 5, 0)
  skid()
  strid(leif, spelare, namn)
  

main()