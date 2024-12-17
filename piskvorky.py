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
IsX = True




print ("Welcome to Tic Tac Toe \n========================================\n GAME RULES:\n Each player can place one mark (or stone)\n per turn on the 3x3 grid. The WINNER is\n who succeeds in placing three of their\n marks in a:\n * horizontal,\n * vertical or\n * diagonal row")
print ("+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+\n")
while end == False:
  if IsX == True:
    IsX = False
    print("========================================")
    print ("Hráč X zvolte pozici")
    print("========================================")
    pozice = int(input())
    indx = pozice - 1
    if plocha[indx] != "-":
      while plocha[indx] != "-":
        print("toto pole je obsazeno, zvolte prazdnou pozici: ")
        pozice = int(input())
        indx = pozice - 1
    else:
      plocha[indx] = "X"
      print ("+---+---+---+\n | "+ plocha[0] +" | " + plocha[1] + " | " + plocha[2] + " |\n+---+---+---+\n| " + plocha[3] + " | " + plocha[4] + " | " + plocha[5] + " |\n+---+---+---+\n| " + plocha[6] +" | " + plocha[7] + " | " + plocha[8] + " |\n+---+---+---+\n")
      if plocha[0] == "X":
        if plocha[1] == "X":
          if plocha[2] == "X":
            end = True
            WIN = "X"
        elif plocha[3] == "X":
          if plocha[6] == "X":
            end = True
            WIN = "X"
        elif plocha[4] == "X":
          if plocha[8] == "X":
            end = True
            WIN = "X"
      elif plocha[3] == "X":
        if plocha[4] == "X":
          if plocha[5] == "X":
            end = True
            WIN = "X"
      elif plocha[6] == "X":
        if plocha[7] == "X":
          if plocha[8] == "X":
            end = True
            WIN = "X"
      elif plocha[1] == "X":
        if plocha[4] == "X":
          if plocha[7] == "X":
            end = True
            WIN = "X"
      elif plocha[2] == "X":
        if plocha[5] == "X":
          if plocha[8] == "X":
            end = True
            WIN = "X"
        elif plocha[4] == "X":
          if plocha[6] == "X":
            end = True
            WIN = "X"
#HRAC O
    print(IsX)
  elif IsX == False:
    IsX = True
    print("========================================")
    print ("Hráč O zvolte pozici")
    print("========================================")
    pozice = int(input())
    indx = pozice - 1
    if plocha[indx] != "-":
      while plocha[indx] != "-":
        print("toto pole je obsazeno, zvolte prazdnou pozici: ")
        pozice = int(input())
        indx = pozice - 1
    else:
      plocha[indx] = "O"
      print ("+---+---+---+\n | "+ plocha[0] +" | " + plocha[1] + " | " + plocha[2] + " |\n+---+---+---+\n| " + plocha[3] + " | " + plocha[4] + " | " + plocha[5] + " |\n+---+---+---+\n| " + plocha[6] +" | " + plocha[7] + " | " + plocha[8] + " |\n+---+---+---+\n")
      if plocha[0] == "O":
        if plocha[1] == "O":
          if plocha[2] == "O":
            end = True
            WIN = "O"
        elif plocha[3] == "O":
          if plocha[6] == "O":
              end = True
              WIN = "O"
        elif plocha[4] == "O":
          if plocha[8] == "O":
            end = True
            WIN = "O"
      elif plocha[3] == "O":
       if plocha[4] == "O":
        if plocha[5] == "O":
           end = True
           WIN = "O"
      elif plocha[6] == "O":
        if plocha[7] == "O":
         if plocha[8] == "O":
           end = True
           WIN = "O"
      elif plocha[1] == "O":
       if plocha[4] == "O":
          if plocha[7] == "O":
           end = True
           WIN = "O"
      elif plocha[2] == "O":
        if plocha[5] == "O":
          if plocha[8] == "O":
            end = True
            WIN = "O"
        elif plocha[4] == "O":
          if plocha[6] == "O":
            end = True
            WIN = "O"

else:
  print ("hrac "+ WIN + " vyhral")





            end = True
            WIN = "O"

else:
  print ("hrac "+ WIN + " vyhral")

