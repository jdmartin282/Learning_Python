import random
import json
import Character

random.seed()


def class_list(cl_type):
    jobs = ['Barbarian', 'Bard', 'Cleric',
            'Druid', 'Fighter', 'Monk',
            'Paladin', 'Ranger', 'Rogue',
            'Sorcerer',
            ]

    for job in jobs:
        if cl_type.title() == job:
            return False

    print('Not an acceptable class!  Enter class or type Exit to quit.')
    return True


def main_menu():
    loop_check = False

    menu = ['1. Create new character',
            '2. Update existing character',
            '3. Exit program',
            ]

    while not loop_check:
        for choice in menu:
            print(choice)
        choice = int(input('Enter choice: '))

        if choice == 1:
            create_character()
            loop_check = True

        elif choice == 2:
            open_character()
            loop_check = True

        elif choice == 3:
            loop_check = True
            print('c')

        else:
            print('Invalid selection')


def create_character():
    creation = False

    '''
    new_char = []
    name = 'Not declared'
    ch_class = 'Not declared'
    level = 'Not declared'
    player = 'Not declared'
    race = 'Not declared'
    alignment = 'Not declared'
    experience = 'Not declared'
    '''

#    new_character = Character()

    creation_menu = ['1. Name', '2. Class', '3. Level',
                     '4. Player', '5. Race', '6. Alignment',
                     '7. Experience', '8. Save Character',
                     ]

    while not creation:
        for item in creation_menu:
            print(item)
        set_info = int(input('Select menu item number: '))

        if set_info == 1:
            pk_name = input('Enter character name: ')
            pk_name = 'Name: ' + pk_name
#            new_character.ch_name = pk_name
        elif set_info == 2:
            valid_cl = True
            while valid_cl:
                pk_class = input('Enter character class: ')
                valid_cl = class_list(pk_class)
#                new_character.ch_class = pk_class
        elif set_info == 3:
            pk_level = input('Enter character level: ')
            pk_level = 'Level: ' + pk_level
#            new_character.ch_level = pk_level
        elif set_info == 4:
            pk_owner = input('Enter player\'s name: ')
            pk_owner = 'player: ' + pk_owner
#            new_character.ch_owner = pk_owner
        elif set_info == 5:
            pk_race = input('Enter character race: ')
            pk_race = 'Race: ' + pk_race
#            new_character.ch_race = pk_race
        elif set_info == 6:
            pk_alignment = input('Enter character\'s alignment: ')
            pk_alignment = 'Alignment: ' + pk_alignment
#            new_character.ch_alignment = pk_alignment
        elif set_info == 7:
            pk_experience_ttl = input('Enter total experience: ')
            pk_experience_ttl = 'Experience: ' + pk_experience_ttl
#            new_character.ch_experience_ttl = pk_experience_ttl

# broken, please fix me
'''
        elif set_info == 8:
            new_char = [name, ch_class, level, player, race, alignment, experience]
            for obj in new_char:
                print(obj)
#            with open(name, 'w') as new:
#                json.dump(new_char, new)
#            creation = True
        else:
            print('Not valid menu option!')
'''


def open_character():
    open_name = input('Enter pre-existing character name: ')

    with open(open_name, 'r') as exists:
        character = json.load(exists)

    print(character)


main_menu()



'''
with open('Illiya_Valira.json', 'r') as character_info:
    character_info = character_info.read()

for info in character_info:
    print(info)

# D6
for i in range(10):
print(random.randrange(1, 7))
'''
