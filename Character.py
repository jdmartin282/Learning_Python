class Character:

    __slots__ = ['player', 'name', 'job', 'level', 'race', 'alignment', 'experience']

    def __init__(self, player, name, job, race, alignment, level=1, experience=0):
        self.player = player
        self.name = name
        self.job = job
        self.level = level
        self.race = race
        self.alignment = alignment
        self.experience = experience


class Warlock(Character):
    def __init__(self, patron, player, name, job, race, alignment, level=1, experience=0):
        super().__init__(player, name, job, race, alignment, level=level, experience=experience)
        self.patron = patron


if __name__ == '__main__':
    x = Character('Hatchi', 'Gremlock', 'Warlock', 'Tiefling', 'Chaotic Neutral')
    choice = input(f'Select Attribute to Edit: {x.__slots__}\n')
    if choice in x.__slots__:
        print(f'{choice}: {x.__getattribute__(choice)}')
        value = input(f'What would you like the new value for {choice} to be? ')
        print(f'{choice}: {value}')
        confirm = input('Are you sure you would like to save these changes? (Y/N): ')
        if confirm.upper() == 'Y':
            x.__setattr__(choice, value)
            print('Changes Saved')
            print(f'{choice}: {x.__getattribute__(choice)}')
