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
  sprint ("Welcome trainer, to the Pokémon Center! My name is Ellie. What is your name? ")
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
  sprint ("\nThat's great to hear. I need you to go outside and look for a man in a black coat. Once you've found him, ask him when the \"delivery\" will get here. Make sure no one hears you ask, this is a private matter! ")
  time.sleep(1)
  print ("""  A. Too tired. Need nap.
  B. Go outside and look for the man
  C. Try to steal all the Pokémon at the center """)
  choice = input(">>> ")
  if choice in answer_A:
    option_nap()
  elif choice in answer_B:
    sprint ("\nYou exit the Pokémon Center and look around. You see a man 30 feet away standing by a fountain.")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  sprint ("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    sprint ("\nReally? You're going to hide in the dark? I think "
    "orcs can see very well in the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    sprint ("\nYou laid in wait. The shimmering sword attracted "
    "the orc, which thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly. As the orc "
    "reached out to grab the sword, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: #If the user didn't grab the sword
     sprint ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    sprint ("As the orc enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the orc turns "
    "around and sees you running.")
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
  sprint ("Good morning . How was your nap?")
  print ("""  A. Great!
  B. Meh.
  C. Terrible!!!""")
  choice = input(">>> ")
  if choice in answer_A:
    sprint ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    sprint ("\nYou're no match for an orc. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
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
