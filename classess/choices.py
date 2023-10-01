class Event:
  """
  This is a class to construct event nodes which are contain the 
  content of the story, the options presented, and the type of event.

  type_off only need to be added when the event has consequences. It can take the strings:
  battle, healing, damage, ending.
  """
  def __init__(self, text, options, type_of="", enemy_name=""):
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
As you try to close the door [red]a giant tongue surrounds you draggin you inside[/ red].
""",
   [],
    "ending"
  )

### Events/story nodes 
cave = Event(
  """You ignore the chest and decide to walk towards the door. The creaking of the door
gives way to a""",
   [
      ("Fight the skeletons", None),
      ("Jump down the well", None)
    ],
    "damage"
  )

library = Event("""As you enter a huge library full of duty old tomes. 
the door behind you seals shot! And there isn't much around other than books.
What would you do?
""",
   [
      ("Search for an exit", None),
      ("Look at the book.", None)
    ],
  )

post_armory_fight = Event(
  """You fought bravely, but after your fight you notice more skeletons rising.
You know endurance will take the best of you, if you keep it up. So you run back towards the library.
The small black door stands infront of you. What do you do?
""",
   [
      ("", None),
      ("Jump down the well", None)
    ],
    "battle",
    "Skeleton"
  )

old_armory = Event(
  """You ignore the chest and decide to walk towards the door. The creaking of the door
gives way to an old rusted armory with skeletons around. As you step in you see all a skeleton rise.
What would you do?""",
   [
      ("Fight the skeletons",post_armory_fight),
      ("Jump down the well", None)
    ]
  )

treasure_room = Event(
  """You run as fast as you can and listen to the sound of collapsing floor behind you.
Finally reaching a room with a big treasure chest and a huge door behind it.
What would you do?:""",
   [
      ("Open the door", old_armory),
      ("Check the treasure chest", mimic_ending)
    ]
  )


#First story event
intro = Event(
  """As the gate cracks open, a musty smell and a dimly lit corridor greet your senses.
After a moment walking in the corridor you start hearing a unfamiliar noise. 
What would you do?""",
   [
      ("Run, as fast as possible!", treasure_room),
      ("Locate the sound's location", cave)
    ]
  )