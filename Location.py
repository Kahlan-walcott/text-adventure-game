"""
Kahlan Walcott
The escape game follows, you, an adventurer, who was abruptly brought to
an old forgotten castle while you were sleeping. You now have to travel
throughout the castle to find the key and bring it back to the starting location.
04/26/2025
"""


class Location:
    """This class keeps track of the locations and their descriptions 
    including neighbors and what items are in them."""
    def __init__(self, decs='', item=None):
        self.description = decs
        self.item = item
        self.neighbors = {}

    def get_item(self):
        """Returns the item that is in location."""
        return self.item

    def get_description(self):
        """Returns the description of the location."""
        return self.description

    def set_item(self, item):
        """Sets the item to the given item"""
        self.item = item
        return item

    def has_item(self):
        """Determines if the location has an item."""
        if self.item is not None:
            return True
        else:
            return False

    def add_neighbor(self, dirs, loc):
        """Adds a neighbor to the neighbors' dictionary."""
        self.neighbors[dirs] = loc

    def get_neighbor(self, direct):
        """Returns the neighbor in a given direction."""
        return self.neighbors.get(direct, None)

    def remove_item(self):
        """Removes an item for the location. When none is returned there
        is no item in the location but when an item is in a room
        the item is assigned to a temporary variable and the item is se
        to none removing the item from a room."""
        if self.item is None:
            return None
        else:
            temp = self.item
            self.item = None
            return temp

    def __str__(self):
        """Returns a string of the description and what the user sees i
        the location. It also returns a string of what location the user
        is in."""
        if self.item is not None:  # when there is an item
            first_str = f'You are {self.get_description()} \n' + f'You see {self.item}'
            return first_str
        else: 
            return f'You are {self.description}'
