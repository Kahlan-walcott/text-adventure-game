"""
Kahlan Walcott
The escape game follows, you, an adventurer, who was abruptly brought to
an old forgotten castle while you were sleeping. 
You now have to travel throughout the castle to find the key 
and bring it back to the starting location.
04/26/2025
"""


class Item:
    """The class keeps track of the items names, descriptions, weight, 
    and its ability to be eaten or not."""
    def __init__(self, name='', desc='', weight=0, edible=False):
        self.name = name
        self. description = desc
        self.weight = weight
        self.edible = edible

    def __str__(self):
        """Returns the description of the item as a string."""
        return self.description

    def is_edible(self):
        """Determines if the item is edible or not."""
        if self.edible:
            return True
        else:
            return False

    def get_weight(self):
        """Returns the wight of the item."""
        return self.weight

    def get_name(self):
        """Returns the items name."""
        return self.name

    def get_description(self):
        """Returns that description of the items."""
        return self.description

    def set_weight(self, wt):
        """Sets the wight of an item to the given weight."""
        self.weight = wt
        return wt

    def set_name(self, name):
        """ Sets the name of an item to the given name."""
        self.name = name
        return name

    def set_description(self, desc):
        """Sets the description of an item to the given description."""
        self.description = desc
        return desc

    def set_edible(self, edible):
        """Sets the edibility of the item to the given edibility."""
        self.edible = edible
        return edible
