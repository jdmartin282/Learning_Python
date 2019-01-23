class Stats:

    __slots__ = ['constitution', 'charisma', 'dexterity', 'intelligence', 'strength', 'wisdom']

    def __init__(self, constitution, charisma, dexterity, intelligence, strength, wisdom):
        self.constitution = constitution
        self.charisma = charisma
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.strength = strength
        self.wisdom = wisdom


class Character:

    __slots__ = ['player', 'name', 'job', 'level', 'race', 'stats', 'alignment', 'experience']

    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        self.player = player
        self.name = name
        self.job = job
        self.level = level
        self.race = race
        self.stats = stats
        self.alignment = alignment
        self.experience = experience


class Warlock(Character):
    def __init__(self, patron, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=stats, level=level, experience=experience)
        self.patron = patron


if __name__ == '__main__':
    pass
