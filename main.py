import random
import json
from character import Character

random.seed()


class Main:

    # Function to check if user input was an actual class
    jobList = ['Barbarian',
               'Bard',
               'Cleric',
               'Druid',
               'Fighter',
               'Monk',
               'Paladin',
               'Ranger',
               'Rogue',
               'Sorcerer',
               ]

    def job_check(self):
        job = input('Enter character class: ')
        if job.title() in self.jobList:
            return job.title()
        else:
            print('Please select from this list:')
            for j in self.jobList:
                print(j)
            return self.job_check()

    # Function to create a new character
    def create_character(self):
        owner = input('Enter player\'s name: ')
        name = input('Enter character name: ')
        job = self.job_check()
        level = int(input('Enter character level: '))
        race = input('Enter character race: ')
        alignment = input('Enter character\'s alignment: ')
        experience = int(input('Enter total experience: '))

        new_character = Character(owner, name, job, race, alignment, stats=None, level=level, experience=experience)

        # Test for correct attributes
        test_list = [owner, name, job, level, race, alignment, experience]
        for t in test_list:
            print(t)

        return new_character

    # Function to edit a pre-existing character
    def edit_character(self, character):
        creation = False
        edit_character = character

        edit_menu = ['1. Owner',
                     '2. Name',
                     '3. Class',
                     '4. Level',
                     '5. Race',
                     '6. Alignment',
                     '7. Experience',
                     #'8. Save Changes',
                     '0. Exit',
                     ]

        while not creation:
            for item in edit_menu:
                print(item)
            set_info = int(input('Select menu item number: '))

            if set_info == 1:
                owner = input('Enter new player\'s name: ')
                edit_character.owner = owner

                print(edit_character.owner)

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

                print(edit_character.alignment)

            elif set_info == 7:
                experience = input('Enter new experience total: ')
                edit_character.experience = experience

                print(edit_character.experience)

            elif set_info == 0:
                creation = True
            else:
                print('Invalid menu option!')

        return edit_character


if __name__ == '__main__':
    x = Main()
    my_character = x.create_character()
    my_character = x.edit_character(my_character)


'''
# Function to display options and call requisite functions
def main_menu():
    loop_check = False
    current_char = 'null'

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
            current_char = self.create_character()
            loop_check = True

# Calls function to edit current character if one is loaded
        elif choice == 2:
            if not current_char:
                current_char = edit_existing_character(current_char)
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

