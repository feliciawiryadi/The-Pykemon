import os, random, time

# INTRO ---------------------------------------------
def intro():
  global level, filename
  print("Welcome to Pykemon.\n\n\nIn this simple game, you are going to \nbattle against 4 pykemons.\n\n1. Squirtle (water)\n2. Bulbasaur (nature)\n3. Charmander (fire)\n4. Pikachu (electric)")
  input("\nPress ENTER to continue")
  os.system("clear")
  print("The rules are simple, each round you are going to \nfight against a random pykemon out of the four. \n\nThis games follows elemental reactions \nthat happen in real life, such as :\n\nWater beats fire\nNature beats electric\nFire beats nature\nElectric beats water")
  input("\nPress ENTER to continue")
  os.system("clear")

  print("1. New data \n2. Load data")
  newload = input("Enter number 1 / 2 : ")
  while newload != "1" and newload != "2":
    print("\nPlease enter numbers 1/2 only.")
    newload = input("Enter number : ")

  os.system("clear")
  if newload == "1":
    print("What's your name?")
    name = input("Insert name :")
    filename = name+".txt"
    try :
      f = open(filename, "x")
      level = 1
    except:
      print("Hmm.. it seems like you have played under that name...")
      print("\nOverwrite? \ncareful, overwriting this data means \nyou will lose all progress.")
      cont = input("(y/n) ")
      while cont != "y" and cont != "n":
        print("\nPlease only input letter 'y' or 'n'.")
        cont = input("Enter letter : ")

      if cont == "y":
        f = open(filename, "w")
        level = 1
      elif cont == "n":
        f = open(filename, "r")
        level = int(f.read())
  elif newload == "2":
    name = input("Insert name : ")
    filename = name+".txt"
    try:
      f = open(filename, "r")
      level = int(f.read())
    except:
      input("Name not found. \nPress ENTER to create new file.")
      f = open(filename, "w")
      level = 1
  f.close()
  print("You are level", level)
  f = open(filename, "w")
  f.write(str(level))
  f.close()
  input("Press ENTER to continue.")
  os.system("clear")

# LOADING SCREEN ------------------------------------
def loading():
  print("Damage criteria : \n1. Attacking using the same element as pykemon, \n   base damage = 10 \n2. Attacking using pykemon's elemental counter, \n   base damage (critical) = 50\n3. Other attacks, base damage = 20-30\n\nAll damages scale up according to your level, \nexample : critical hit (50 damage) \nlevel 1 : 50 dmg\nlevel 2 : 100 dmg \nlevel 3 : 150 dmg \net cetera.\n")
  for i in range(5):
    time.sleep(1)
    print("Loading...")
  input("Press ENTER to continue")
  os.system("clear")
  print("Remember : \nWater beats fire\nNature beats electric\nFire beats nature\nElectric beats water\n")
  
  print("Preparing the arena...")
  time.sleep(2)
  input("Press ENTER to begin the battle.")
  os.system("clear")

def randoming():
  global enemy, index, element, temp1
  enemies = ["Squirtle", "Bulbasaur", "Charmander", "Pikachu"]
  elements = ["water", "nature", "fire", "electric"]

  index = random.randint(0,3)
  while temp1 == index:
    index = random.randint(0,3)
  enemy = enemies[index]
  element = elements[index]

# BATTLE --------------------------------------------
def battle():
  global attacks, move, damage, enemy, myHP, enemyHP
  print("You are fighting against a", enemy, "(", element, ")")

  attacks = ["Water gun", "Poison Ivy", "Dynamite", "Tazer"]
  print("\nAttacks : \n1. Water gun \n2. Poison Ivy \n3. Dynamite \n4. Electric Tazer")
  print("\nYour HP is", myHP, "\n"+enemy+"'s HP is", enemyHP)

  move = input("\n(Please enter numbers only.)\nYour move : ")
  while move != "1" and move != "2" and move != "3" and move != "4":
    print("\nPlease enter numbers 1-4 only.")
    move = input("Your move : ")
  os.system("clear")
  damagecount()

def damagecount():
  global move, enemy, damage, enemyHP, myHP, level, filename, commentary
  commentary = []
  if enemy == "Squirtle":
    if move == "1":
      # water vs water
      damage = 10
      waterattacks()
    elif move == "2":
      # nature vs water
      damage = 30
      natureattacks()
    elif move == "3":
      # fire vs water
      damage = 20
      fireattacks()
    elif move == "4":
      # elec vs water
      damage = 50
      elecattacks()
  elif enemy == "Bulbasaur":
    if move == "1":
      # water vs nature
      damage = 30
      waterattacks()
    elif move == "2":
      # nature vs nature
      damage = 10
      natureattacks()
    elif move == "3":
      # fire vs nature
      damage = 50
      fireattacks()
    elif move == "4":
      # elec vs nature
      damage = 20
      elecattacks()
  elif enemy == "Charmander":
    if move == "1":
      # water vs fire
      damage = 50
      waterattacks()
    elif move == "2":
      # nature vs fire
      damage = 20
      natureattacks()
    elif move == "3":
      # fire vs fire
      damage = 10
      fireattacks()
    elif move == "4":
      # elec vs fire
      damage = 30
      elecattacks()
  elif enemy == "Pikachu":
    if move == "1":
      # water vs elec
      damage = 20
      waterattacks()
    elif move == "2":
      # nature vs elec
      damage = 50
      natureattacks()
    elif move == "3":
      # fire vs elec
      damage = 30
      fireattacks()
    elif move == "4":
      # elec vs elec
      damage = 10
      elecattacks()
  if damage == 10 :
    commentary.append("\nWEAK")
  elif damage == 20:
    commentary.append("\nSTRONG !")
  elif damage == 30:
    commentary.append("\nPOWERFUL !!")
  elif damage == 50:
    commentary.append("\nCRITICAL !!!")
  enemyHP -= level*damage
  myHP -= level*15
  if enemyHP < 0:
    enemyHP = 0
  if myHP < 0:
    myHP = 0

  print("You used", attacks[int(move)-1], "\n"+enemy, "used basic attack\n")
  for data in commentary:
    print(data)
    time.sleep(0.5)
  input("\nPress ENTER to continue")
  os.system("clear")

  print("Your attack dealt", level*damage, "damage to", enemy+".\nYou lost", level*15, "HP from", enemy+"'s attack. \n\nYour HP :", myHP, "\n"+enemy+"'s HP :", enemyHP)
  
  if myHP > 0 :
    f = open(filename, "w")
    f.write(str(level))
    f.close()
  else :
    print("\n....You died. May you rest in peace.", enemy, "lives for one more day.")
  input("Press ENTER to continue")
  os.system("clear")

# ELEMENTAL SOUND EFFECTS ---------------------------
def waterattacks():
  global commentary
  commentary = ["POW !","SPLASH !!", "WHOOOSH !!!"]

def natureattacks():
  global commentary
  commentary = ["POW !", "EARTH GRUMBLING..", "BOOM !!!"]

def fireattacks():
  global commentary
  commentary = ["POW !", "FIRE CRACKLING..", "FWOOSH !!!"]

def elecattacks():
  global commentary
  commentary = ["POW !", "POOF !!", "BZZZZZ !!!"]

# MAIN ----------------------------------------------
intro()
temp1 = 100
myHP = level*100
enemyHP = level*50
loading()
randoming()
while myHP > 0:
  if enemyHP <= 0:
    print("Oh wait!! \n"+enemy, "fainted.\n\nYou won the battle and levelled up! \n\nNow you have more HP and stronger attacks, \nbut so does your enemy. \n\nHP +100")
    input("\nPress ENTER to continue")
    os.system("clear")
    temp1 = index
    randoming()
    level += 1
    myHP += 100
    enemyHP = level*50
  battle()
os.system("clear")
print("That was fun! come again later!")