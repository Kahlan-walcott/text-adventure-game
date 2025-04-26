"""
Kahlan Walcott
The escape game follows, you, an adventurer, who was abruptly brought to an old forgotten castle while you were
sleeping. you now have to travel throughout the castle to find the key and bring it back to the starting location.

I certify that this code is mine, and mine alone, in accordance with GVSU academic honesty policy.
12/07/2023
"""

from Item import Item
from Location import Location


class Game:
    """This class keeps trak of the items in a location and when they have been picked up, dropped, or eaten. It also
    allows the game to be played by a user or an auto win feature."""
    def __init__(self):
        self.lis_item = []
        self.create_world()
        self.current_loc = self.bedroom  # start_loc
        self.int_message = ''
        self.set_welcome_message()
        self.first = None
        self.second = None

    def get_message(self):
        """Returns the initial message"""
        return self.int_message

    def get_current_location(self):
        """Returns the current location"""
        return self.current_loc

    def create_world(self):
        """Keeps track of all the attributes of the items, locations, and neighbors in the castle."""
        # items
        self.sword = Item('sword', 'a old and well used sword that has a green emerald on it.', 8, False)
        self.key = Item('key', 'a shiny and silver key.', 2, False)
        self.sandwich = Item('sandwich', 'a soggy ham and cheese sandwich.', 1, True)
        self.book = Item('book', 'a tiny and leather-bound book with faded gold lettering.', 55, False)

        # locations
        self.maids_chamber = Location('in a near perfectly clean maids chamber.', None)
        self.kitchen = Location('in a messy kitchen with half of the pans hanging and clean and the others not.', None)
        self.bathroom = Location('in a sparkling bathroom.', self.sandwich)
        self.attic = Location('in a dark and dusty attic that has only been used of storage.', None)
        self.bedroom = Location('in a bright bedroom that is clean and seemingly unused.', None)
        self.ballroom = Location('in a massive ballroom.', self.key)
        self.library = Location('in a vast musty library.', self.book)
        self.war_room = Location('in an dimly lit war room with one weapon that has a spotlight on it.', self.sword)

        # neighbors
        self.maids_chamber.add_neighbor('north', self.bathroom)
        self.kitchen.add_neighbor('north', self.ballroom)
        # Bathroom
        self.bathroom.add_neighbor('east', self.bedroom)
        self.bathroom.add_neighbor('south', self.maids_chamber)
        # Attic
        self.attic.add_neighbor('south', self.bathroom)

        # Bedroom
        self.bedroom.add_neighbor('north', self.attic)
        self.bedroom.add_neighbor('west', self.bathroom)
        self.bedroom.add_neighbor('south', self.library)
        # Ballroom
        self.ballroom.add_neighbor('down', self.kitchen)
        self.ballroom.add_neighbor('east', self.library)
        self.ballroom.add_neighbor('south', self.war_room)
        # Library
        self.library.add_neighbor('west', self.ballroom)
        self.library.add_neighbor('south', self.war_room)
        self.library.add_neighbor('north', self.bedroom)
        # War room
        self.war_room.add_neighbor('north', self.library)
        self.war_room.add_neighbor('up', self.ballroom)

    def go(self, dirs):
        """Keeps track of the current location and replaces it with where the user moves next"""
        next_loc = self.current_loc.get_neighbor(dirs)
        if next_loc is None:
            # executes when there is no neighbor in the given direction.
            self.int_message = 'You can\'t move in this direction.'
        else:
            # replaces the current location with the next one and updates the message with the current location
            self.current_loc = next_loc
            self.int_message = self.current_loc.__str__()

    def set_welcome_message(self):
        """Sets the initial message to the description and goal of the game and the commands that can be used."""
        self.int_message = ('You, an adventurer, were tired after your journey, so you found a tree to take a nap by. '
                            'When you awoke you are no longer in the forest, but you are in a \nbedroom of an '
                            'old forgotten castle that you must find your way out of.'
                            '\n'
                            '\nCommands: \nauto: will give you the answer to the game'
                            '\ncommands: will give you the following list'
                            '\ngo direction: allows you to move to different rooms \n'
                            'help: gives helpful hints \npickup item: allows you to pickup an item \n'
                            'drop item: you can drop an item in your inventory \n'
                            'look: allows you to find out where you are \n'
                            'list: allows you to see what items are in your inventory \n'
                            'eat item: allows you to eat an edible item \nswing: allows you to swing the sword \n'
                            'lay: allows you to lay in the bed\n')

    def parse_command(self):
        """Gets input from the user and splits it into two words"""
        words = input('Enter>>> ').split()
        first = words[0].lower()
        if len(words) > 1:  # executes when the user enters more than one word
            second = words[1].lower()
        else:  # sets the second word to none since the user didn't put a second word
            second = None
        return first, second

    def start(self):
        """Controls the entire game and what to do for the valid or invalid inputs from the user"""
        print(self.get_message())
        first, second = self.parse_command()
        self.first = first
        self.second = second
        while first != 'quit':  # runs only while the user does not enter quit
            if self.game_over() is True:
                break
            elif first == 'commands':
                print('Commands: \nauto: will give you the answer to the game'
                            '\ncommands: will give you the following list'
                            '\ngo direction: allows you to move to different rooms \n'
                            'help: gives helpful hints \npickup item: allows you to pickup an item \n'
                            'drop item: you can drop an item in your inventory \n'
                            'look: allows you to find out where you are \n'
                            'list: allows you to see what items are in your inventory \n'
                            'eat item: allows you to eat an edible item \nswing: allows you to swing the sword \n'
                            'lay: allows you to lay in the bed\n')
            elif first == 'auto':
                Game().auto_win()
                break
            elif first == 'go' and second == 'north' or second == 'south' or second == 'east' or second == 'west' or second == 'up' or second == 'down':  # executes when the user enters go and a valid direction and prints the updated message for the location
                self.go(second)
                print(self.int_message)

            elif first == 'help':
                # allows the user to type help to get the hint for the location they are in
                self.help()
                print(self.int_message)
            elif first == 'pickup':
                # allows the user to type pickup to pick
                # up the item in the location and get a message of what they are holding.
                self.pickup()
                print(self.int_message)

            elif first == 'swing' and second == 'sword':
                # only runs when the second word is sword.
                # When the second word is sword the user gets
                # a message that they have swung the sword
                self.swing_sword()
                print(self.swing_sword())
            elif first == 'swing' and second != 'sword':
                # only runs when the second word is not sword.
                # When the second word is not sword it prints the message
                # that the thing the user is trying to swing is not swingable
                print(f'You can\'t swing a {second}')
            elif first == 'lay':
                # allows the user to type lay and prints out the message of if the user can lay down in that location
                self.lay_in_bed()

            elif first == 'drop' and second == 'sandwich' or second == 'key' or second == 'sword':
                # executes drop and a valid item that they would like to drop and prints
                # the message that they dropped the item
                print(self.drop(second))
            elif first == 'look':  # allows the user to type look to get a description what room they are currently in
                self.look()
                print('You are ' + self.int_message)
            elif first == 'list':  # allows the user to type list to get a message of what is in their inventory
                print(self.list())
            elif first == 'eat':  # allows the user to type eat to get a message of if that item is edible or not
                print(self.eat(second))

            elif first == 'quit':
                # allows the user to type quit to end the game and prints out that they chose to end the game
                print('You chose to end the game.')
                break
            else:  # accounts for all the invalid inputs and displays the commands that can be typed
                print('That is not a valid command. \nTry typing: \ngo north, west, east, south, up, or down - to go to'
                      ' another room in that direction \nlook - to see where you are \npickup - to pick up an item if '
                      'there is one in the room you are currently in \ndrop - sandwich, key, sword, or book - to drop that'
                      ' specific item \neat - sandwich, key, sword, or book - to try to eat that specific item '
                      '\nlist - to see what is in your inventory \nhelp - to get hints and directions \nauto - if you'
                      ' are lost this will give you the answer')

            first, second = self.parse_command()
            self.first = first
            self.second = second

    def look(self):
        """Updates the message with the current locations description and then returns it"""
        self.int_message = self.current_loc.get_description()
        return {self.int_message}

    def help(self):
        """Accounts for any hints the user may need while playing the game"""
        if self.current_loc == self.maids_chamber:  # updates that message to what the user can do in the maids chamber and where to go next
            self.int_message = ('There is nothing for you here. Go to another room.'
                                '\nDirections:'
                                '\nNorth: Bathroom')
        elif self.current_loc == self.kitchen:
            # updates the message to what the user can do in the kitchen and where to go next
            self.int_message = ('There is nothing for you here. Go to another room.'
                                '\nDirections:'
                                '\nNorth: Ballroom')
        elif self.current_loc == self.bathroom:  # updates the message to what the user can do in the bathroom and where to go next
            self.int_message = ('Go pick up the sandwich and go to another room.'
                                '\nDirections:'
                                '\nSouth: Maids Chamber'
                                '\nEast: Bedroom')
        elif self.current_loc == self.attic:  # updated the message to what the user can do in the attic and where to go next
            self.int_message = ('There is nothing for you here. Go to another room.'
                                '\nDirections:'
                                '\nSouth: Bathroom')

        elif self.current_loc == self.bedroom:  # updates the message to what the user can do in the bedroom and where to go next
            self.int_message = ('There is nothing for you here. Go to another room.'
                                '\nDirections:'
                                '\nNorth: Attic'
                                '\nSouth: Library'
                                '\nWest: Bathroom')

        elif self.current_loc == self.ballroom:  # updates the message to what the user can do in the ballroom and where to go next
            self.int_message = ('Go pick up the key and bring it to the bedroom.'
                                '\nDirections:'
                                '\nSouth: War Room'
                                '\nEast: Library'
                                '\nDown: Kitchen')
        elif self.current_loc == self.library:  # updates the message to what the user can do in the library and where to go next
            self.int_message = ('Go pickup the book and go to another room.'
                                '\nDirections:'
                                '\nNorth: Bedroom'
                                '\nSouth: War Room')
        elif self.current_loc == self.war_room:  # updates the message to what the user can do in the war room and where to go next
            self.int_message = ('Go pick up the sword and go to another room. If you have gone to all of the rooms and '
                                'have the key in your inventory go back to the bedroom and lay in the \nbed.'
                                '\nDirections'
                                '\nNorth: Library'
                                '\nUp: Ballroom')
        return self.int_message

    def list(self):
        """Returns a string of what is in the users inventory"""
        statement = f'You are holding: \n'
        for item in self.lis_item:
            statement += f'{item.get_description()}\n'
        return statement

    def pickup(self):
        """Keeps track of if an item is in the location the user is in and returns the appropriate message"""
        if self.current_loc.has_item():
            # runs if the current location has an item and returns the items name that the user picked up
            self.int_message = f'You are holding a {self.current_loc.get_item().get_name()}'
            temp = self.current_loc.get_item()
            if temp.get_weight() >= 50:  # checks the items weight, if it is over 50 it is too heavy to pick up
                self.int_message = f'The {self.current_loc.get_item().get_name()} is too heavy to pick up!'
            else:  # adds the item to the list and removes it from the location
                self.lis_item.append(temp)
                self.current_loc.set_item(None)
        else:  # returns the message that there is nothing in the room to pick up
            self.int_message = 'There is nothing to pick up.'
        return self.int_message

    def drop(self, name):
        """Allows the user to drop an item in the room they are in"""
        i = self.search_pouch(name)
        if i is not None:  # runs if the item the user wants to drop is in the list
            self.current_loc.set_item(i)
            self.lis_item.remove(i)
            return f'You have successfully dropped {i.get_name()} on the floor'
        else:  # tells the user that the item that are trying to drop is not in their inventory
            return f'You are not holding a {name}'

    def search_pouch(self, name):
        """Checks the list for the item to user is trying to do something with"""
        for i in self.lis_item:
            if i.get_name().lower() == name:  # runs if the thing in the list matches what the user wants
                return i
        return None

    def eat(self, name):
        """Checks the edibility of an item in the users inventory"""
        item = self.search_pouch(name)
        if item is not None:  # runs if there is item in the list that matches what the user wants
            if item.is_edible():  # checks if the item is edible, if it is it's removed and the message is updated to tell the user that they ate something
                self.lis_item.remove(item)
                self.int_message = f'You ate a yummy piece of {item.get_name()}'
            else:  # returns that the item the user is trying to eat is not edible
                self.int_message = f'{item.get_name()} is not edible'
        else:  # returns that the item the user is trying to eat is not in their inventory
            self.int_message = f'You are not holding {name}'
        return self.int_message

    def game_over(self):
        """Controls weather the user won the game or not yet"""
        if self.key in self.lis_item and self.current_loc == self.bedroom and self.lay_in_bed() is True:
            # runs only if the key is in the list and the users current location is the bedroom and prints the message that the user won the game
            self.int_message = 'You escaped the castle! Run far, far away.'
            print(self.int_message)
            return True
        else:  # the game is still going
            return False

    def swing_sword(self):
        """Allows the user to swing the sword"""
        if self.sword in self.lis_item:  # runs only if the sword is in the list and returns that the user swung the sword
            return 'You have swung the sword.'
        return 'You not swung the sword.'

    def lay_in_bed(self):
        """Allows the user to lay in the bed"""
        if self.current_loc == self.bedroom and self.first == 'lay':
            # runs only when the current location is the bedroom and returns that the user is laying on the bed
            print('You are laying in the bed.')
            return True
        else:  # if the user tries to lay down anywhere else the message that there is nothing to lay on is returned
            # print('There is nothing for you to lay on')
            return False

    def auto_win(self):
        """Allows someone who has access to this code to see how to win the game without interacting with it"""
        g = Game()
        print(g.get_message())
        print(g.look())
        print(g.help())
        g.go('south')
        print(g.get_message())
        print(g.help())
        print(g.pickup())
        g.go('south')
        print(g.get_message())
        print(g.help())
        print(g.pickup())
        print(g.list())
        g.go('up')
        print(g.get_message())
        print(g.help())
        print(g.pickup())
        g.go('east')
        print(g.get_message())
        print(g.help())
        g.go('north')
        print(g.get_message())
        g.lay_in_bed()
        g.first = 'lay'
        if g.game_over():
            g.get_message()


if __name__ == '__main__':
    g = Game()
    # g.auto_win()
    g.start()
