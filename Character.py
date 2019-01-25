class Stats:

    __slots__ = ['constitution', 'charisma', 'dexterity', 'intelligence', 'strength', 'wisdom']

    def __init__(self, constitution, charisma, dexterity, intelligence, strength, wisdom):
        self.constitution = constitution
        self.charisma = charisma
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.strength = strength
        self.wisdom = wisdom


class Skills:

    __slots__ = ['acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 'history', 'insight',
                 'intimidation', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion',
                 'religion', 'sleight_of_hand', 'stealth', 'survival']

    def __init__(self, acrobatics, animal_handling, arcana, athletics, deception, history, insight, intimidation,
                 investigation, medicine, nature, perception, performance, persuasion, religion, sleight_of_hand,
                 stealth, survival):
        self.acrobatics = acrobatics
        self.animal_handling = animal_handling
        self.arcana = arcana
        self.athletics = athletics
        self.deception = deception
        self.history = history
        self.insight = insight
        self.intimidation = intimidation
        self.investigation = investigation
        self.medicine = medicine
        self.nature = nature
        self.perception = perception
        self.performance = performance
        self.persuasion = persuasion
        self.religion = religion
        self.sleight_of_hand = sleight_of_hand
        self.stealth = stealth
        self.survival = survival


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
