import pickle
from Character import Character


class Main:

    # Didn't want to use properties "class" and "classList" instead we are calling them "jobs"
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
               'Warlock',
               'Wizard']

    def createCharacter(self):
        player = input(r"Enter Player's name: ")
        name = input('Enter character name: ')
        job = self.getJob()
        race = input('Enter character race: ')
        alignment = input(r"Enter character's alignment: ")
        level = int(input('Enter character level: '))
        experience = int(input('Enter total experience: '))
        return Character(player, name, job, race, alignment, level=level, experience=experience)

    # We are going to use __slots__ of `Character` to get our list of editable properties
    def editCharacter(self, character: Character):
        choice = input(f'Select Attribute to Edit: {character.__slots__}\n')
        if choice in character.__slots__:
            print(f'{choice}: {character.__getattribute__(choice)}')
            value = input(f'What would you like the new value for {choice} to be?\n')
            print(f'{choice}: {value}')
            confirm = input('Are you sure you would like to save these changes? (Y/N)\n')
            if confirm.upper() == 'Y':
                character.__setattr__(choice, value)
                print(f'{choice}: {character.__getattribute__(choice)}')
                print('Changes Saved')
        move_on = input('Would you like to make additional changes? (Y/N)\n')  # Adding Recursion for addition changes
        if move_on.upper() == 'Y':
            self.editCharacter(character)
        return character

    # We want to be able to save the Characters we create
    def saveCharacter(self, character: Character):
        with open(rf'database\{character.name}.p', 'wb') as dataFile:
            pickle.dump(character, dataFile)

    # We want to be able to load our Characters that we have created
    def loadCharacter(self, characterName):
        with open(rf'database\{characterName}.p', 'rb') as dataFile:
            return pickle.load(dataFile)

    # We are going to add some recursion to validate we get a proper class from our list
    def getJob(self):
        job = input('Enter Character Class: ')
        if self.validateJob(job.title()):
            return job
        else:
            jobListPrintout = ', '.join(self.jobList)
            print(rf'"{job.title()}" is not a valid class. Please enter a valid class from the list: {jobListPrintout}')
            self.getJob()  # This is the recursion call

    def validateJob(self, job):
        if job not in self.jobList:
            return False
        else:
            return True


if __name__ == '__main__':
    x = Main()
    y = Character('Hatchi', 'Gremlock', 'Warlock', 'Tiefling', 'Chaotic Neutral')
    z = x.editCharacter(y)
    x.saveCharacter(z)
    a1 = x.loadCharacter(z.name)
    print('debugline')
