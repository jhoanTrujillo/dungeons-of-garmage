class Event:
  """
  This is a class to construct event nodes which are contain the 
  content of the story, the options presented, and the type of event.

  categoryf only need to be added when the event has consequences. It can take the strings:
  battle, heal, damage, ending.

  The types of events that a class can be are:    

  damage: damages the player by 1
  heal: heals the character by 1
  battle: triggers the battle function in the utility.py. The requirement should be an string
  with the name of an enemy from the enemies dic in characters.py.
  reward: Just like the battle category, you should provide an string with the name of the 
  item you would like to append to the player items.
  alternative: in addition you should provide an array with two objects, and string and another
  array that follows the same format as other choices.
  """
  def __init__(self):
    self.text = ""
    self.options = []
    self.category = ""
    self.requirement = ""
  
  def add_values(self, text, options,category="", requirement=""):
    #Always provide text to display the players.
    self.text = text
    #Needs at least an empty array.
    self.options = options
    self.category = category
    self.requirement = requirement
    
  def add_option(self, option , next_node):
      """
      Allows to add option to any node. 
      WARNING: Not tested yet, and might be remove
      """
      self.options.append((option, next_node)) 

#####################################
####   Story nodes declaration   ####
#####################################

#defining all the events as empty class
intro = Event()
#Dungeon Path
treasure_room = Event()
#mimic ending is part of this path
library = Event()
armory = Event()
skeleton_fight = Event()
pythonmancer = Event()

#Underground path
cave = Event()
hold_breath = Event()
hide_in_shadows = Event()
interact_with_dwellers = Event()
sneak_from_dwellers = Event()
hostile_towards_dwellers = Event()
undertown = Event()

#temple (last event for both path)
temple = Event()
heretic_slayer = Event()
cosplayer = Event()
trickster = Event()
the_pythonmancer = Event()

#Boss scenes
the_hand = Event()
the_hand_weaken = Event()

#Endings
mimic_ending = Event()
dead_by_battle = Event()
lamb = Event()
priest_of_hold = Event()
vanquisher = Event()
the_coward = Event()


#Intro add_values.
intro.add_values(
  """The unwelcoming smell of dust, and mould is in the air of a dimly.
As you make your way throught the hallway you start to hear a unfamiliar noise.
What would you do?
  """,
  [
    ("Run forward!", treasure_room),
    ("Analyse the sound", cave)
  ]
)

### Underground path
cave.add_values(
  """You fell down a dark abyss. Eventually landing in a body of water.
As you emerge you can hear creatures in the distance and the darkness gives way
to the dim light of torches approaching.""",
  [
    ("hold your breath", hold_breath),
    ("Hide into the shadows", hide_in_shadows)
  ],
  "damage"
)

hold_breath.add_values(
  """As you hold your breath you start to heal, Thanks to the magic of the spring.
Of course, breathing is still an issue, so as you re-surface.
small fluffy cave dwellers look at you in awe. 
""",
  [
    ("*yell* I'm that who reigns in the depths", interact_with_dwellers),
    ("Leave water, and punch a dweller", hostile_towards_dwellers)
  ],
  "heal"
)

hide_in_shadows.add_values(
  """You leave the water and hide in the shadows, and between rocks.
You notice small fluffy creatures with little torches approaching the body of water,
they look at each other and shrug.""",
  [
    ("Sneak around from the creatures", sneak_from_dwellers),
    ("Show yourself, ...Hello?.", interact_with_dwellers)
  ]
)

interact_with_dwellers.add_values(
   """The creatures laugh, and start mimicking you. Some of them are facinanted,
the others are talking between each other and then, what seems to be the leader
points towards the path behind them.
""",
  [
    ("Follow the fluffy dwellers", None ),
    ("Show yourself, ...Hello?.", interact_with_dwellers)
  ]
)

undertown.add_values(
   """After some rest in the Dwellers village, you are ready to go.
As you stand infront of a stone staircase which split into two ways. leading back to the dungeon. 
the dwellers hand you a sword. Too big for the little creatures, but perfect for your journey ahead.
What do you do?
""",
  [
    ("Take the right path", None),
    ("Take the left path", None)
  ], 
  "reward", 
  "Excalibur"
)

#Inner dungeon path
treasure_room.add_values(
  """You run as fast as you can and listen to the sound of collapsing floor behind you.
Finally, you reach with only one treasure chest and a door not far behind it.""",
  [
    ("Head for the door", library),
    ("Open the chest", mimic_ending)
  ]
)

mimic_ending.add_values(
  """You open the chest, thinking on all the richest you will find.
Then you take a moment and notice a [red]fleshy interior[/ red] and teeth around the lid,
As you try to close the door [red]a giant tongue surrounds you draggin you inside[/ red].""",
[],
"ending" 
)

library.add_values(
  """As you open the door, you look at old dusty tomes, 
sitting in shelves that reach the roof. Then the door locks behind you! 
And there isn't much around other than books.""",
  [
    ("Search for an exit", armory),
    ("Look at the book.", pythonmancer)
  ]
)

armory.add_values(
"""After looking around for a bit you found another room. It looks like an armory.
All the equipment is rusted, and a well seems to be in the middle of the room.
Some skeletons are in the floor. But it seems like one of them is starting to move!""",
  [
    ("Fight the skeleton", skeleton_fight),
    ("Jump down the well", cave)
  ]
)

pythonmancer.add_values("""Between the hundreds of books, annexed in the walls of the library 
You find a book called 'Modern Guide To Pythonmancy', and put it in your bag. 
Then as you look around there is a small black door, and a big old wooden door.
""",
  [
    ("Go throught the wooden door", armory),
    ("Go throught the small black door", temple)
  ],
  "reward",
  "Modern Guide To Pythonmancy"
)

skeleton_fight.add_values(
  """You fought bravely! but after your fight you notice more skeletons start rising.
You know this fight will take the best of you at this pace.
What do you do?
""",
  [
    ("Run to the Library", temple),
    ("Jump down the well", cave)
  ],
  "battle",
  "Skeleton"
)

temple.add_values(
  """You run towards your next location, and locking the black door behind you.
This gives way to a temple of sort, and in there a group of cultist praying to an unknown god.
unnused robes are around you, but other then that the only exist is behind the priest.
What do you do?
""",
  [
    ("Stop this heresy!", heretic_slayer),
    ("Wear the robe and join the cultist", cosplayer)
  ]
)
#Wear the robe and join the cultist circle
cosplayer.add_values(
  """You wear the robes of a cultist and join their prayer. 
The priest mentions a sacrifice, and ask the congregation to gather around.
You do and the a symbol in the floor opens a void into the floor and a giant hand comes out.
The hand seems to be looking for something to grab.
""",
  [
    ("Push the cultist next to you, towards the hand", trickster),
    ("Give yourself to the hand. The hand loves you", lamb)
  ], 
  "alternative",
  [
    "Modern Guide To Pythonmancy",
    ("Cast your pythonmancer spell", the_pythonmancer)
  ]
)
#when the player uses the pythonmancy spell book on the cultist
the_pythonmancer.add_values(
     """You uses your power and just like that anacondas and pythons jump at the enemy.
The Hand is weakend, the cultist are unconsious, and the priest ran through the door behidn. 
The Hand feels, you and it is ready to take you on.
""",
  [
    ("Claim the glory!", the_hand_weaken),
    ("Take what you can and run away!", the_coward)
  ]
)

#Push the cultist next to you.
trickster.add_values(
  """\"What did you do? That was steve! we can\'t force our chocice on The Hand!\", said the priest, as he put his crown away,
  and started to run. [purple]The Hand[/purple] is out of control, throwing and hitting cultist around.
""",
  [
    ("I...Have to (fight The Hand)", the_hand),
    ("I...Have to (Sacrifice yourself)", lamb)
  ]
)

#After defeating the weaken hand using the pythonmancer book, the evil ending is unlock. 
#Not all easy endings are good.
the_hand_weaken.add_values("""You [red]slayed The hand[/ red], and wear the crown of thorns left behind by the priest.
  The calling is too strong, this is what you always wanted. Your mind is beginning to falter... 
  Would you accept the offer of The Hand? 
  """,
  [
    ("", ),
    ("", )
  ],
  "battle",
  "The hand weaken"
)

### Endings
dead_by_battle.add_values("""You fought with all your might, but might alone won't save a lost soul.
  [red3]You fell in combat like hundreds of other adventurers seeking greatness[/ red3].""",
  [],
  "ending"
)

lamb.add_values("""You give yourself to the command of [purple]The Hand[/ purple].
  [red3]You can feel the warm of its embrace, as you traverse the void.[/ red3] This is the end
  of your journey, but it feels right.""",
  [],
  "ending"
)

#Chaotic Ending 
the_coward.add_values(
   """You take all you can, all the gold, silver, and even copper. All in your bag.
   Nor [purple]The Hand[/purple] or the [purple]cultist[/purple] had enough time to see you go. 
   You are far from everything and between the crevices of the caves in the underground you see a light,
   a light back to Garmage. [pink]Congratulations, you get to live another day![/ pink]
""",
  [],
  "ending"
)

#Evil Ending
priest_of_hold.add_values("""With your crown of thorns, and your throne as [purple]The Hand[/purple], you are the new,
  undisputed [bold purple]master priest of The church of hold[/ bold purple]. May Garmage sleep well
  one last night, because your reign of evil starts here.
  """,
  [],
  "ending"
)

#Hero Ending
vanquisher.add_values( """With the power of [yellow]Excalibur[/ yellow] you break the hold of evil in your mind.
  and the light of the sword, incinarates all evil infront of you, from the [purple]cultist[/ purple], to [red]The Hand[red],
  They are all but burnt marks on the ground. You are [bold yellow]The Paladin of Light[/bold yellow], Bringing Garmage to a new age of peace.
  """,
  [],
  "ending"
)