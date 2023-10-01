class Event:
  """
  This is a class to construct event nodes which are contain the 
  content of the story, the options presented, and the type of event.

  type_off only need to be added when the event has consequences. It can take the strings:
  battle, healing, damage, ending.
  """
  def __init__(self, text, options=[], type_of="", enemy_name=""):
    self.text = text
    self.options = options
    self.type_of = type_of
    self.enemy_name = enemy_name
    
  def add_option(self, option, next_node):
      """
      Allows to add option to any node. 
      WARNING: Not tested yet, and might be remove
      """
      self.options.append((option, next_node)) 

################################
####     Story nodes        ####
################################

### Endings
mimic_ending = Event(
  """You open the chest, thinking on all the richest you will find.
Then you take a moment and notice a [red]fleshy interior[/ red] and teeth around the lid,
As you try to close the door [red]a giant tongue surrounds you draggin you inside[/ red].""",
"ending"
)

dead_by_battle = Event(
   """You fought with all your might, but might alone won't save a lost soul.
[red3]You fell in combat like hundreds of other adventurers seeking greatness[/ red3].""",
"ending"
)

### Underground path
cave_b = Event(
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

cave_a = Event(
  """You fall into a body of water! sadly, it was painful.
As you come out of the water you can hear a noise coming from creatures in the cave.
The torches are getting closer. 
What would you do?""",
   [
      ("hold your breath", None),
      ("Hide into the shadows", None)
    ]
  )

cave = Event(
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

#Inner dungeon path


skeleton_fight = Event(
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

skeleton = Event(
"""After looking around for a bit you found another room. It looks like an armory.
All the equipment is rusted, and a well seems to be in the middle of the room.
Some skeletons are in the floor. But it seems like one of them is starting to move!""",
   [
      ("Fight the skeleton", skeleton_fight),
      ("Jump down the well", cave)
    ]
  )

library = Event(
  """As you open the door, you look at old dusty tomes, 
sitting in shelves that reach the roof. Then the door locks behind you! 
And there isn't much around other than books.""",
   [
      ("Search for an exit", skeleton),
      ("Look at the book.", None)
    ]
  )

treasure_room = Event(
  """You run as fast as you can and listen to the sound of collapsing floor behind you.
Finally, you reach with only one treasure chest and a door not far behind it.""",
   [
      ("Head for the door", library),
      ("Open the chest", mimic_ending)
    ]
  )


#Intro event.
intro = Event(
  """As the gate cracks open, a musty smell and a dimly lit corridor greet your senses.
After a moment walking in the corridor you start hearing a unfamiliar noise. 
What would you do?""",
   [
      ("Run, as fast as possible!", treasure_room),
      ("Locate the sound's location", cave)
    ]
  )