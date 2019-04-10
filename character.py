class Stats:

    __slots__ = ['strength', 'dexterity', 'wisdom', 'intelligence', 'charisma', 'constitution']

    def __init__(self, strength, dexterity, wisdom, intelligence, charisma, constitution):
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.constitution = constitution


class Character:

    __slots__ = ['player', 'name', 'job', 'race', 'alignment', 'stats', 'level', 'experience']

    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        self.player = player
        self.name = name
        self.job = job
        self.level = level
        self.race = race
        self.alignment = alignment
        self.experience = experience
        self.stats = stats


class Barbarian(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Bard(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Cleric(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Druid(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Fighter(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Monk(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Paladin(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Ranger(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Rogue(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Sorcerer(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)


class Warlock(Character):
    def __init__(self, patron, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)
        self.patron = patron


class Wizard(Character):
    def __init__(self, player, name, job, race, alignment, stats: Stats, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, stats=Stats, level=level, experience=experience)

