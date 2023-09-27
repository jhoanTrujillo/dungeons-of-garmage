class Character:
  """
  Player class which will hold the health of the player
  and some other values that can be change during the game.
  """
  def __init__(self, name, health, attack, defense):
    self.name = name
    self.health = health
    self.attack = attack
    self.defense = defense
    self.is_dead = False
  
  def calculate_damage(self, enemy_defense):
    """
    calculates damage of a battle. 
    """
    return self.attack - enemy_defense

  def take_damage(self, damage=1):
    """
    Decrease the health value of the class by one or more if the value 
    heal is provided on the call.
    """
    self.health -= damage
    return f"[red bold]You took damage. Current Health: { self.health }[/red bold]."
  
  def restore_damage(self, heal=1):
    """
    Increases the health value of the class by one or more if the value 
    heal is provided on the call.
    """
    self.health += heal
    return f"[green bold]Some damage was restored. Current Health: { self.health }[/green bold]."

  def battle(self, enemy):
    """
    Makes the player and enemy take damage over time. 
    The calculation is based on each other's stat.
    Prints message if the user dies
    """
    #execute as long as the player has healt
    while self.health > 0:
      #calculates damage dealt to enemy
      damage_dealt = self.calculate_damage(enemy.defense)
      enemy.take_damage(damage_dealt)
      print(f"[yellow]You dealt {damage_dealt} damage[/ yellow]. To the {enemy.name}")

      #If enemy is alive calculate damage receive from enemy
      if enemy.health > 0:
          damage_received = enemy.calculate_damage(self.defense)
          self.take_damage(damage_received)
          print(f"[red]You took {damage_received} damage[/ red]. You have {self.health} health left")
      #If the enemy is dead it should return a message and break the loop
      else:
        return f"[green]You defeated the {enemy.name}.[/ Green]Current health: [pink]{self.health}[/pink]"
    #If the while loop can't be execute that means the player is dead. 
    self.is_dead = True
    return self.is_dead
    
      

#Player declaration
player = Character("Player", 5 ,5, 4)

#Enemy declaration
skeleton = Character("Skeleton", 4 , 5, 3)
