class StoryNode:
  """
  This class contains the text display in each event, and the choices
  the player get to make.
  """
  def __init__(self, event, options):
    self.event = event
    self.options = options

  
node1 = StoryNode(
  """
  As you enter the dungeon a [dark green]musty smell[/ dark green], and a [darkgrey]dark semi lit[/ darkgrey] corridor greet you.
  You can tell time isn't a friend of what could have once being a fortress.
  """,
[("Rush through the corridor",node1_a),("Analyze the corridor",node1_b)])

node1_a = StoryNode(
  """
  [yellow bold]"A trap!?"[/ yello bold] you said, as you ran. But your speed was greater than the collapsing 
  floor. Now you stand at the entrance of a grand room, several artifacts of old left behind.
  In front of you the only visible door, but it is so... [black]dark[/ black].
  """,
[("Search around the room.",node1),("Head towards the door.",node)])

node1_b = StoryNode(
  """
  As you carefully look around the floor drops. You fall several meters into a underground 
  water body, [red bold]taking 1 damage[/ red bold]. You can see the edge and hear the noises
  of creatures nearby.
  """,
[("Hide in the shadows.",node1),("Hold your breath!",node1)])
