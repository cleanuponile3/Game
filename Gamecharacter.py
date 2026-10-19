class GameCharacter:
    """A class representing a game character with managed stats like health, mana, and level."""
    
    def __init__(self, name: str):
        # Initialize the character with a given name and default starting stats
        self._name = name
        self._health = 100  # Starts at maximum health
        self._mana = 50     # Starts at maximum mana
        self._level = 1     # Starts at level 1

    @property
    def name(self):
        """Read-only property to access the character's name."""
        return self._name

    @property
    def health(self):
        """Getter property to access the character's current health."""
        return self._health

    @health.setter
    def health(self, value):
        """Setter property to protect health bounds, preventing it from dropping below 0 or going above 100."""
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        """Getter property to access the character's current mana."""
        return self._mana

    @mana.setter
    def mana(self, value):
        """Setter property to protect mana bounds, preventing it from dropping below 0 or going above 50."""
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        """Getter property to access the character's current level."""
        return self._level

    def level_up(self):
        """Increases the character's level, refills health and mana, and announces the level up."""
        self._level += 1
        self.health = 100  # Uses the health setter
        self.mana = 50     # Uses the mana setter
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        """Returns a string representation of the character's current stats."""
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"cp