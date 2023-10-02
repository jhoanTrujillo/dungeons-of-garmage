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

#Endings
mimic_ending = Event()
dead_by_battle = Event()

#Intro add_values.
intro.add_values(
  """As the gate cracks open, a musty smell and a dimly lit corridor greet your senses.
After a moment walking in the corridor you start hearing a unfamiliar noise. 
What would you do?""",
  [
    ("Run, as fast as possible!", treasure_room),
    ("Locate the sound's location", cave)
  ]
)

### Underground path
cave.add_values(
  """You fall into a body of water! sadly, it was painful.
As you come out of the water you can hear a noise coming from creatures in the cave.
The torches are getting closer. 
What would you do?""",
  [
    ("hold your breath", None),
    ("Hide into the shadows", None)
  ],
  "damage"
)

hold_breath.add_values(
  """""",
  [
    ("hold your breath", None),
    ("Hide into the shadows", None)
  ],
  "healing"
)

hide_in_shadows.add_values(
  """""",
  [
    ("hold your breath", None),
    ("Hide into the shadows", None)
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
    ("Jump down the well", None)
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