from re import I
#promene
Player = "X"
end = False
pozice = int
pozice = 0
indx = pozice - 1
plocha = ["-","-","-",
          "-","-","-",
          "-","-","-"]
P1 = plocha





print ("Welcome to Tic Tac Toe \n========================================\n GAME RULES:\n Each player can place one mark (or stone)\n per turn on the 3x3 grid. The WINNER is\n who succeeds in placing three of their\n marks in a:\n * horizontal,\n * vertical or\n * diagonal row")
print ("+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n")
while end == False:
#stridani hracu
  if Player == "O":
    Player = "X"
  else:
    Player = "O"

  print("========================================")
  print ("Hráč " + Player + " zvolte pozici")
  print("========================================")
  pozice = int(input())
  indx = pozice - 1
#kontrola
  if 0>int(pozice):
    while 0>int(pozice):
      print("zvolte číslo mezi 1-9: ")
      pozice = int(input())

  elif 9<int(pozice):
    while 9<int(pozice):
      print("zvolte číslo mezi 1-9: ")
      pozice = int(input())
  elif plocha[indx] != "-":
    while plocha[indx] != "-":
      print("toto pole je obsazeno, zvolte prazdnou pozici: ")
      pozice = int(input())
      indx = pozice - 1
  else:
     plocha[indx] = Player
     print ("+---+---+---+\n | "+ plocha[6] +" | " + plocha[7] + " | " + plocha[8] + " |\n+---+---+---+\n| " + plocha[3] + " | " + plocha[4] + " | " + plocha[5] + " |\n+---+---+---+\n| " + plocha[0] +" | " + plocha[1] + " | " + plocha[2] + " |\n+---+---+---+\n")
     if plocha[0] == Player:
        if plocha[1] == Player:
          if plocha[2] == Player:
             end = True
             WIN = Player
        elif plocha[3] == Player:
          if plocha[6] == Player:
            end = True
            WIN = Player
        elif plocha[4] == Player:
          if plocha[8] == Player:
            end = True
            WIN = Player
     elif plocha[3] == Player:
        if plocha[4] == Player:
           if plocha[5] == Player:
             end = True
             WIN = Player
     elif plocha[6] == Player:
        if plocha[7] == Player:
          if plocha[8] == Player:
            end = True
            WIN = Player
     elif plocha[1] == Player:
       if plocha[4] == Player:
         if plocha[7] == Player:
            end = True
            WIN = Player
     elif plocha[2] == Player:
         if plocha[5] == Player:
          if plocha[8] == Player:
            end = True
            WIN = Player
         elif plocha[4] == Player:
           if plocha[6] == Player:
            end = True
            WIN = Player
else:
  print ("hrac "+ WIN + " vyhral")



