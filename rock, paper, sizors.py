import random

x = {
  0: "rock",
  1: "paper",
  2: "sizors"
}
while 1:
  cG = random.choice(list(x.keys()))
  print("0.rock")
  print("1.paper")
  print("2.sizors")

  pG = int(input())
  if pG not in range(0, 3):
    print("select number in range 0, 2")
  elif(pG == 0 and cG == 2):
    print("you win")
  elif(cG == 0 and pG == 2):
    print("you lost")
  elif(pG < cG):
    print("you lost")
  elif(pG > cG):
    print("you win")
  elif(pG == cG):
    print("its draw")
    break















