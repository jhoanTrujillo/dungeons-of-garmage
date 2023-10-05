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
        self.items = []

    def calculate_battle_damage(self, enemy_defense):
        """
        calculates damage of a battle.
        """
        if self.attack > enemy_defense:
            return self.attack - enemy_defense
        else:
            return 1

    def take_damage(self, damage=1):
        """
        Decrease the health value of the class by one or more if the value
        heal is provided on the call.
        """
        self.health -= damage
        if self.health <= 0:
            self.is_dead = True
        return f"""[red]{self.name} took {damage}[/red]
        Current Health: {self.health}."""

    def restore_damage(self, heal=1):
        """
        Increases the health value of the class by one or more if the value
        heal is provided on the call.
        """
        self.health += heal
        return f"""[green bold]Some damage was restored.\n
        Current Health: { self.health }[/green bold]."""

    def do_damage(self, enemy):
        """
        do damage to an enemy class which uses the same character class.
        """
        damage = self.calculate_battle_damage(enemy.defense)
        enemy.health -= damage
        """
        Checks if the entity affected has less or 0 health,
        marks them as dead, and sets total as 0.
        """
        if enemy.health <= 0:
            enemy.health = 0
            enemy.is_dead = True
        return f"""[red bold]{enemy.name} took {damage} damage.
        Leaving it with {enemy.health} health.[/red bold]"""

    def add_item(self, item_name):
        # Append string with item name to the items array
        self.items.append(item_name)
        return f"[green]you gain { item_name }[/green]"

    def use_item(self, event_node):
        node_options = event_node
        # goes over the items in the player item list
        for item in self.items:
            # Checks for name of the item can be found in items array
            if item == node_options.requirement[0]:
                # Individually add both values in the array.
                node_options.add_option(node_options.requirement[-1][0],
                                        node_options.requirement[-1][-1])
                return f"An alternative route has open due to an item: {item}"

# Player declaration
player = Character("Player", 5, 5, 4)
# Enemy declaration
enemies = {
    "Skeleton": Character("Skeleton", 5, 5, 2),
    "Dweller": Character("Dweller", 4, 6, 2),
    "Priest": Character("Priest", 3, 3, 2),
    "The hand": Character("The Hand", 6, 6, 4),
    "The hand weaken": Character("The Hand", 3, 2, 2)
}
