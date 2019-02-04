class Character:

    __slots__ = ['self', 'player', 'name', 'job', 'race', 'alignment', 'stats', 'level', 'experience']

    def __init__(self, player, name, job, race, alignment, level=1, experience=0):
        self.player = player
        self.name = name
        self.job = job
        self.level = level
        self.race = race
        self.alignment = alignment
        self.experience = experience
        self.stats = Stats()


class Stats:

    __slots__ = ['strength', 'dexterity', 'wisdom', 'intelligence', 'charisma', 'constitution']

    def __init__(self, strength, dexterity, wisdom, intelligence, charisma, constitution):
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.constitution = constitution
