import random
#import json
from character import *

random.seed()


class Main:

    def __init__(self):
########################################################################################################################
# Dictionaries and lists to call and test against
########################################################################################################################
        # Dictionary to call against for predetermined job
        self.classes = {'Barbarian': Barbarian,
                        'Bard': Bard,
                        'Cleric': Cleric,
                        'Druid': Druid,
                        'Fighter': Fighter,
                        'Monk': Monk,
                        'Paladin': Paladin,
                        'Ranger': Ranger,
                        'Rogue': Rogue,
                        'Sorcerer': Sorcerer,
                        'Warlock': Warlock,
                        'Wizard': Wizard,
                        }

        # Dictionary to call functions for individual classes
        self.createClasses = {'Barbarian': self.create_barbarian,
                              'Bard': self.create_bard,
                              'Cleric': self.create_cleric,
                              'Druid': self.create_druid,
                              'Fighter': self.create_fighter,
                              'Monk': self.create_monk,
                              # 'Paladin': self.create_paladin,
                              # 'Ranger': self.create_ranger,
                              # 'Rogue': self.create_rogue,
                              # 'Sorcerer': self.create_sorcerer,
                              # 'Warlock': self.create_warlock,
                              # 'Wizard': self.create_wizard,
                              }

        # List to test against for valid jobs
        self.jobList = ['Barbarian',
                        'Bard',
                        'Cleric',
                        'Druid',
                        'Fighter',
                        'Monk',
                        'Paladin',
                        'Ranger',
                        'Rogue',
                        'Sorcerer',
                        'Warlock',
                        'Wizard',
                        ]

        # List to test against for valid races
        self.raceList = ['Dwarf',
                         'Elf',
                         'Halfling',
                         'Human',
                         'Dragonborn',
                         'Gnome',
                         'Half-Elf',
                         'Half-Orc',
                         'Tiefling',
                         ]

        # List to test against for valid alignments
        self.alignmentList = ['Lawful Good',
                              'Neutral Good',
                              'Chaotic Good',
                              'Lawful Neutral',
                              'True Neutral',
                              'Chaotic Neutral',
                              'Lawful Evil',
                              'Neutral Evil',
                              'Chaotic Evil',
                              ]

########################################################################################################################
# Functions to set class specific attributes
########################################################################################################################

    def create_barbarian(self, player, name, job, race, alignment, stats, level, experience):
        path = 'Path' # Function to call circle and provided stats/info
        return self.classes['Barbarian'](path, player, name, job, race, alignment,
                                     stats, level, experience)

    def create_bard(self, player, name, job, race, alignment, stats, level, experience):
        college = 'College' # Function to call circle and provided stats/info
        return self.classes['Bard'](college, player, name, job, race, alignment,
                                     stats, level, experience)

    def create_cleric(self, player, name, job, race, alignment, stats, level, experience):
        domain = 'Domain' # Function to call circle and provided stats/info
        return self.classes['Cleric'](domain, player, name, job, race, alignment,
                                     stats, level, experience)

    def create_druid(self, player, name, job, race, alignment, stats, level, experience):
        circle = 'Land' # Function to call circle and provided stats/info
        return self.classes['Druid'](circle, player, name, job, race, alignment,
                                     stats, level, experience)

    def create_fighter(self, player, name, job, race, alignment, stats, level, experience):
        fightingStyle = 'Fighting Style' # Function to call circle and provided stats/info
        return self.classes['Fighter'](fightingStyle, player, name, job, race, alignment,
                                     stats, level, experience)

    def create_monk(self, player, name, job, race, alignment, stats, level, experience):
        martialArts = 'Martial Arts' # Function to call circle and provided stats/info
        return self.classes['Monk'](martialArts, player, name, job, race, alignment,
                                     stats, level, experience)

########################################################################################################################
# Test loops for correct spelling and actual jobs, races, and alignments
########################################################################################################################
    # Function to check if the chosen job is valid from predetermined list
    def job_check(self):
        for j in self.jobList:
            print(j)
        job = input('Enter character class: ')

        if job.title() in self.jobList:
            return job.title()
        else:
            print('\nPlease select from this list:')
            return self.job_check()

    # Function to check if the chosen race is valid from predetermined list
    def race_check(self):
        for r in self.raceList:
            print(r)
        race = input('Enter character class: ')

        if race.title() in self.raceList:
            return race.title()
        else:
            print('\nPlease select from this list:')
            return self.race_check()

    # Function to check if the chosen alignment is valid from predetermined list
    def alignment_check(self):
        for a in self.alignmentList:
            print(a)
        alignment = input('Enter character alignment: ')

        if alignment.title() in self.alignmentList:
            return alignment.title()
        else:
            print('\nPlease select from this list:')
            return self.alignment_check()

########################################################################################################################
# Functions to create and edit characters and stats
########################################################################################################################
    # Function to create a new character
    def create_character(self):

        player = input('Enter player\'s name: ').title()
        name = input('Enter character name: ').title()

        print('\nAvailable classes: ')
        job = self.job_check()
        level = int(input('Enter character level: '))
        race = self.race_check()
        alignment = self.alignment_check()
        experience = int(input('Enter total experience: '))
        stats = self.create_stats()

        new_character = self.createClasses[job](player, name, job, race, alignment,
                                                stats=stats, level=level, experience=experience)

        # Test for correct attributes
        # test_list = [player, name, job, level, race, alignment, experience]
        # for t in test_list:
        #     print(t)

        return new_character

    # Function to edit a pre-existing character
    def edit_character(self, character):
        creation = False
        edit_character = character

        edit_menu = ['1. Player',
                     '2. Name',
                     '3. Class',
                     '4. Level',
                     '5. Race',
                     '6. Alignment',
                     '7. Experience',
                     '0. Exit',
                     ]

        while not creation:
            for item in edit_menu:
                print(item)
            set_info = int(input('Select menu item number: '))

            if set_info == 1:
                player = input('Enter new player\'s name: ')
                edit_character.player = player

                print(edit_character.player)

            elif set_info == 2:
                name = input('Enter new character name: ')
                edit_character.name = name

                print(edit_character.name)

            elif set_info == 3:
                edit_character.job = self.job_check()

                print(edit_character.job)

            elif set_info == 4:
                level = input('Enter new character level: ')
                edit_character.level = level

                print(edit_character.level)

            elif set_info == 5:
                race = input('Enter new character race: ')
                edit_character.race = race

                print(edit_character.race)

            elif set_info == 6:
                alignment = input('Enter new character\'s alignment: ')
                edit_character.alignment = alignment

                print(f'Alignment changed to {edit_character.alignment}!\n')

            elif set_info == 7:
                experience = input('Enter new experience total: ')
                edit_character.experience = experience

                print(f'Experience changed to {edit_character.experience}!')

            elif set_info == 0:
                creation = True
            else:
                print('Invalid menu option!')

        return edit_character

    def create_stats(self):

        strength = int(input('Enter strength: '))
        dexterity = int(input('Enter dexterity: '))
        wisdom = int(input('Enter wisdom: '))
        intelligence = int(input('Enter intelligence: '))
        charisma = int(input('Enter charisma: '))
        constitution = int(input('Enter constitution: '))

        new_stats = Stats(strength=strength, dexterity=dexterity, wisdom=wisdom,
                          intelligence=intelligence, charisma=charisma, constitution=constitution)

        return new_stats


########################################################################################################################
# Main Test Area
########################################################################################################################


if __name__ == '__main__':
    x = Main()
    # my_character = x.create_character()
    my_stats = Stats(strength=12, dexterity=10, wisdom=9, intelligence=10, charisma=8, constitution=14)
    my_character = Druid(circle='Land', player='Jesse', name='Illiya', job='Druid', race='Half-Elf',
                         alignment='ChaoticNeutral', stats=my_stats, level=7, experience=8821)
    # print(my_character)
    # print(my_character.Druid.circle)
    # my_character = x.edit_character(my_character)
    # my_character.stats = x.create_stats()

    print(my_character.circle)
    print(my_character.stats.strength)
    print(my_character.stats.dexterity)
    print(my_character.stats.wisdom)
    print(my_character.stats.intelligence)
    print(my_character.stats.charisma)
    print(my_character.stats.constitution)

    # for i in my_character.__slots__:
    #     print(i)


########################################################################################################################
# Dead code needing updated/refactored
########################################################################################################################
'''
# Function to display options and call requisite functions
def main_menu(self):
    loop_check = False

    menu = ['1. Create new character',
            '2. Update existing character',
            '0. Exit program',
            ]

    while not loop_check:
        for choice in menu:
            print(choice)
        choice = int(input('Enter choice: '))

        # Calls function to create a new character
        if choice == 1:
            current_char = current_char.create_character()
            loop_check = True

        # Calls function to edit current character if one is loaded
        elif choice == 2:
            if not current_char:
                current_char = current_char.edit_character(current_char)
                loop_check = True
            else:
                print("No character currently opened!")
                loop_check = True

        elif choice == 0:
            loop_check = True
            print('c')

        else:
            print('Invalid selection')

    return current_char
'''

# broken, please fix me
'''
        elif set_info == 8:
            new_char = [name, ch_class, level, player, race, alignment, experience]
            for obj in new_char:
                print(obj)
            with open(name, 'w') as new:
                json.dump(new_char, new)
            creation = True
        else:
            print('Not valid menu option!')
'''

'''
def open_character():
    open_name = input('Enter pre-existing character name: ')

    with open(open_name, 'r') as exists:
        character = json.load(exists)

    print(character)
'''

'''
with open('Illiya_Valira.json', 'r') as character_info:
    character_info = character_info.read()

for info in character_info:
    print(info)

# D6
for i in range(10):
print(random.randrange(1, 7))
'''

