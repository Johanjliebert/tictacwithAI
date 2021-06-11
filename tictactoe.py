import random
import time
#board+start
print("""chcesz byc kółkiem czy krzyżykiem""")
ty="0"
while ty!="1" and ty!="2":
   print("jeśli chcesz krzyżyk to napisz 1 a jeśli kółko to 2")
   ty=input()
if ty=="1":
   ty="X"
   comp="O"
else:
   ty="O"
   comp="X"
poziom="0"
while poziom!="1" and poziom!="2":
   print("wybierz poziom- 1 czy 2")
   poziom=input()
game_going=True
x=[]
possible=[]
y=0
z=""
while y<9:
   y+=1
   x.append(str(y))
   possible.append(y)
if(ty=="O"):
   wynik={
      "X":-1,
      "O":1,
      "nikt nie":0
   }
else:
   wynik={
      "X":1,
      "O":-1,
      "nikt nie":0
   }

y=1

#display board

def board():
   print(
'  '+x[0]+""" |  """+x[1]+""" |  """+x[2]+""" 
____ ____ ____
  """+x[3]+""" |  """+x[4]+""" |  """+x[5]+"""
____ ____ ____
  """+x[6]+""" |  """+x[7]+""" |  """+x[8])
   print("")


#turn
def turn():
   print("twój ruch")
   valid=False
   while valid==False:
      try:
         z=int(input())
         if z not in possible:
            raise ValueError
         valid=True
      except:
         print("błąd, podaj właściwą wartość")
   x[z-1]=ty
   possible.remove(z)
   board()
   checkwin()
   time.sleep(1)
#check win

def checkwin():

#check middle
   diagonal1=x[0]==x[4]==x[8]
   diagonal2=x[6]==x[4]==x[2]
   row=x[3]==x[4]==x[5]
   column=x[1]==x[4]==x[7]
   if diagonal1 or diagonal2 or row or column==True:
      return x[4]

#left upper corner

   uprow=x[0]==x[1]==x[2]
   lefcol=x[0]==x[3]==x[6]
   downrow=x[6]==x[7]==x[8]
   rightcol=x[2]==x[5]==x[8]
   if uprow or lefcol == True:
      return x[0]
#right down corner
   elif downrow or rightcol==True:
      return x[8]
#check tie
   elif len(possible)==0:
      return "nikt nie"
   else:
      return 0
#computer respond!
#random
def random_respond():
   respond=random.choice(possible)
   x[respond-1]=comp
   possible.remove(respond)
   board()
   print("___________________________")
#best 
def best_respond(ilosc):
   best_score=2
   while ilosc>0:
      pos=possible[ilosc-1]
      possible.remove(pos)
      x[pos-1]=comp
      score=minimax(True)
      if score<best_score:
         best_score=score
         best_move=pos-1
      x[pos-1]=str(pos)
      possible.append(pos)
      ilosc-=1
   return best_move

def minimax(is_maximazing):
   result=checkwin()
   if result!=0:
      return wynik[result]
   if is_maximazing:
      bestScore=-2
      for _ in possible:
         moz=possible[0]
         x[moz-1]=ty
         possible.remove(moz)
         scor=minimax(False)
         possible.append(moz)
         x[moz-1]=str(moz)
         if(scor>bestScore):
            bestScore=scor
      return bestScore
   else:
      bestScore=2
      for _ in possible:
         moz=possible[0]
         x[moz-1]=comp
         possible.remove(moz)
         scor=minimax(True)
         possible.append(moz)
         x[moz-1]=str(moz)
         if(scor<bestScore):
            bestScore=scor
      return bestScore

#play game

board()
if ty=="X":
   time.sleep(1)
   random_respond()
while checkwin()==0:
   turn()
   if checkwin()==0:
      if poziom=="1":
         random_respond()
      elif poziom=="2":
         resp=best_respond(len(possible))
         x[resp]=comp
         possible.remove(resp+1)
         board()
         print("___________________________")
print(str(checkwin())+" wygrywa!")
end=input()
