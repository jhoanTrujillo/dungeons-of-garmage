class StoryNode:
  """
  This class contains the text display in each event, and the choices
  the player get to make.
  """
  def __init__(self, text, options, is_damage=False, is_healing=False, is_ending=False):
    self.text = text
    self.options = options
    self.is_damage = is_damage
    self.is_healing = is_healing
    self.is_ending = is_ending

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
test_ending = StoryNode(
  "\nEnd of test.",
   [
      ("Leave dungeon", None)
    ],
    is_ending = True
  )

### Events/story nodes
caves_a = StoryNode(
  """
  End of path
  """,
   [
      ("Ending", test_ending)
    ]
  )

caves = StoryNode(
  """The floor under your feet opens up, and you fall into a pitch black pit. *Spalsh* you fall harshly into a body of water.\n
  As you resurface you hear creatures in the distances and see a torch approaching. What do you do?
  """,
   [
      ("Hide in the shadows", caves_a),
      ("Hold my breath", caves_a)
    ],
    is_damage=True
  )

treasure_room = StoryNode(
  """As the gate cracks open, a musty smell and a dimly lit corridor greet your senses. 
After a moment walking in the corridor you start hearing a unfamiliar noise. 
what would you do?\n""",
   [
      ("Run!", test_ending),
      ("Listen carefully", caves)
    ]
  )

#Initial node
corridor = StoryNode(
  """As the gate cracks open, a musty smell and a dimly lit corridor greet your senses.
After a moment walking in the corridor you start hearing a unfamiliar noise. 
What would you do?""",
   [
      ("Run!", treasure_room),
      ("Listen carefully", caves)
    ]
  )