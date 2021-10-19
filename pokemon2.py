import os #This was required to make VLC player import work. IDK why
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import time,sys,vlc  #Imports a module to add a pause, a module to make typing look realistic, and vlc music player



#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#defines the slow typing speed for realistic typing
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

#Grabbing objects
pokeball = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication



#The story is broken into sections, starting with "intro"
def intro():
  sprint ("Welcome trainer, to the Motostoke Pokémon Center! My name is Ellie. What is your name? ")
  myName = input()
  sprint ("It is good to meet you, " + myName + ". I see you don\'t have a pokemon of your own yet!")
  time.sleep(1)
  sprint ("How would you feel about helping me out with a job and I\'ll give you one of my basic pokemon?")
  time.sleep(1.5)
  print ("""  A. Sounds good!
  B. I'm way too busy to help you.
  C. Take a nap""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_yes()
  elif choice in answer_B:
    sprint ("\nHow rude. You are hereby banned from this Pokémon Center! "
    "\n\nGame over!")
    time.sleep(3)
    intro()
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_yes(): 
  sprint ("\nThat's great to hear. I need you to go outside and look for a man in a black coat. "
          "Once you've found him, ask him when the \"delivery\" will get here. Make sure no one hears you ask, this is a private matter! ")
  time.sleep(1)
  print ("""  A. Too tired. Need nap.
  B. Go outside and look for the man.
  C. Exit and try to find a Pokémon on your own! """)
  choice = input(">>> ")
  if choice in answer_A:
    option_nap()
  elif choice in answer_B:
    sprint ("\nYou exit the Pokémon Center and look around. You see a man 30 feet away standing by a fountain.")
  elif choice in answer_C:
    option_selfhelp()
  else:
    print (required)
    option_rock()

def option_selfhelp():
  sprint ("\nYou walk outside and don't even notice the man in the black coat, just down the road. "
          "Straight ahead you see the sparkling river, to the left the road leads to the outskirts of Motostoke, and to the right the Galar mine. "
          "While glancing around, your eyes are drawn towards something sparkling in the midday sun, it's an object stuck in the mud down on the riverbank. "
          "Not able to help yourself, you walk towards it. You see it is a shiny Pokéball on the ground! Do you pick it up? Y/N?")
  choice = input(">>> ")
  if choice in yes:
    pokeball = 1 #adds a Pokéball
  else:
    pokeball = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. go to Motostoke outskirts.
  B. Head to the Galar Mine.
  C. Rest by the river""")
  choice = input(">>> ")
  if choice in answer_A:
    sprint ("\nHolding your new prized Pokéball in your hand, you head towards the outskirts of town.")
  elif choice in answer_B:
   if sword > 0:
    sprint ("\nYou've always been a big fan of mines, even if they aren't yours. You head west to the Galar Mine.")
   else: #If the user didn't grab the sword
     sprint ("\n")
  elif choice in answer_C:
    sprint ("The soft, rustling grass is so inviting. It has been a stressful day."
            "\"Yeah, why not? you deserve this!\" You think to yourself as you plop "
            "down, quickly falling asleep in the warm sun.")
    option_run()
  else:
    print (required)
    option_cave()

def option_nap():
  sprint ("You lie down in the corner of the room and allow your eylids to slowly slide over your eyeballs. You drift into a peaceful sleep.")
  time.sleep(2)
  sprint ("Snore...............Snore.................Snore")
  time.sleep(2)
  sprint ("You awake to the smiling face of Ellie")
  time.sleep(1)
  sprint ("\"Good morning sunshine. How was your nap?\", she says sweetly.")
  print ("""  A. Great!
  B. Meh.
  C. Terrible!!!""")
  choice = input(">>> ")
  if choice in answer_A:
    sprint ("\"Oh that's great to hear. Now do you think you can go find the man in the black coat? He doesn't like to be kept waiting.")
  elif choice in answer_B:
    sprint ("\"Well you probably just need some energy, here try some of my famous Sour Whipped-Cream Curry. It's Copperajah class you know!\"")
  elif choice in answer_C:
    option_terrible()
  else:
    print (required)
    option_run()
    
def option_terrible():
  sprint ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the orc to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  sprint ("You hear its heavy footsteps and ready yourself for "
  "the impending orc.")
  time.sleep(2)
  if flower > 0:
    sprint ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the orc. It does! The orc was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     sprint ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")
intro()

p = vlc.MediaPlayer("file:///C:/Users/Larkenor\Music/PokemonThemeSong.mp3")

p.play()
