from Event import Event
import random


class Tour(Event):
    """Class to represent a Tour as a Child of Event Class"""

    # Constructor
    def __init__(self, event_name='', date='', guide=''):  # We have an attribute that is initialized from the parent class, and we initialized 3 more attributes in this class. This means that a tour has 4 attributes, howeover, an event still has 1 attribute only.

        # This calls the constructor of the parent class (Event), and initializes the attributes of an event
        Event.__init__(self, event_name)

        # We initialized the new instance values that are in the tour class. There is no need to initialize the other attributes as we called the parent class constructor
        self._date = date
        self._guide = guide
        self._capacity = self.group_capacity()

        # Setter functions to set the attributes of a tour

    def set_date(self, date):
        self._date = date

    def set_guide(self, guide):
        self._guide = guide

    # Getter functions to set the attributes of a tour
    def get_date(self):
        return self._date

    def get_guide(self):
        return self._guide

        # Function to assign a random capacity for a tour

    def group_capacity(self):
        return random.choice([15, 41])

    def get_capacity(self):
        return self._capacity

    # Function to display a new tour
    def display_new_tour(self):
        pass