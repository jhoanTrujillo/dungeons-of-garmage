class Event:
  """
  This is a class to construct event nodes which are contain the 
  content of the story, the options presented, and the type of event.

  type_off only need to be added when the event has consequences. It can take the strings:
  battle, healing, damage, ending.
  """
  def __init__(self):
    self.text = ""
    self.options = []
    self.type_of = ""
    self.enemy_name = ""
  
  def add_values(self, text, options,type_of="", enemy_name=""):
    #Always provide text to display the players.
    self.text = text
    #Needs at least an empty array.
    self.options = options
    self.type_of = type_of
    self.enemy_name = enemy_name
    
  def add_option(self, option , next_node):
      """
      Allows to add option to any node. 
      WARNING: Not tested yet, and might be remove
      """
      self.options.append((option, next_node)) 

################################
####     Story nodes        ####
################################

#defining all the events as empty class
intro = Event()
#Dungeon Path
treasure_room = Event()

#mimic ending is part of this path
library = Event()
pythonmancer = Event()
armory = Event()
skeleton_fight = Event()

#Underground path
cave = Event()

hold_breath = Event()
hide_in_shadows = Event()

interact_with_dwellers = Event()
sneak_from_dwellers = Event()
hostile_towards_dwellers = Event()

#Endings
mimic_ending = Event()
dead_by_battle = Event()

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
  "healing"
)

hide_in_shadows.add_values(
  """You leave the water and hide in the shadows, and between rocks.
You notice small fluffy creatures with little torches approaching the body of water,
they look at each other and shrug.""",
  [
    ("Sneak about from the creatures", sneak_from_dwellers),
    ("Show yourself, ...Hello?.", interact_with_dwellers)
  ]
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
You find a book called pythonmancer and store it in your backpack.
""",
  [
    ("", ),
    ("",)
  ]
)

skeleton_fight.add_values(
  """You fought bravely! but after your fight you notice more skeletons start rising.
You know this fight will take the best of you at this pace.
What do you do?
""",
  [
    ("Run to the Library", None),
    ("Jump down the well", Cave)
  ],
  "battle",
  "Skeleton"
)

### Endings
dead_by_battle.add_values(
   """You fought with all your might, but might alone won't save a lost soul.
[red3]You fell in combat like hundreds of other adventurers seeking greatness[/ red3].""",
[],
"ending"
)