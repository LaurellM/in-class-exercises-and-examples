musician = {
    "name": "Andrew Bird",
    "instrument": ["violin", "whistle"],
    "record label": "Merge",
    }
# as we reach thr limitations of dictionaries to represesent data,
# we can move to classes
# Classes generally represent the nouns in code (people, places, things)

class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f'{self.name}: {self.instrument}'

# When I create an object thats an element of a class,
# it's called an instance
# Let's create a musician class and store that instance 
# in a variable  

snoop = Musician("Snoop Dogg", "MC")
print(snoop)

jewel = Musician("Jewel", "guitar")
print(jewel)
# create 3 new more musician instances
andy = Musician("Andy Dwyer", "guitar")
print(andy)

duke = Musician("Duke Silver", "saxaphone")

elsa = Musician("Elsa", "vocals")

# 2 examples of instances

class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        return self.name

    @property
    def show_members(self):
        print(f'The members of {mouse_rat.name} are: ', [f"{member}" for member in mouse_rat.members])


mouse_rat = Band("Mouse Rat")
print(f'The members of {mouse_rat.name} are {mouse_rat.members}')

mouse_rat.members.extend([snoop, jewel])
print(f'The members of {mouse_rat.name} are: ', [f"{member}" for member in mouse_rat.members])
# add new mwmbers to the band
new_members = [andy, duke, elsa]
# print out new band members
mouse_rat.members.extend(new_members)
mouse_rat.show_members
# get values of attributes for new members
more_info_tuples = [("Laurell", "harmonica"), ("Vanessa", "drums"), ("Samuel", "piano")]

# new_members = []
# create a musiciam instance foir each new member and add them to the new_members
for member_tuple in more_info_tuples:
    name, instrument = member_tuple 
    new_member = Musician(member_tuple[0], member_tuple[1])
    new_members.append(new_member)

mouse_rat.show_members