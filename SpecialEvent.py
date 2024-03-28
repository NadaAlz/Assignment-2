from Event import Event
from enum import Enum

class ExhibitionLocation(Enum):  # A class to give Enum values to the self._exhLoc and self.location attribute
    """Class to represent Exhibition Location as ENUM values"""
    PG = "Permanent Galleries"
    EH = "Exhibition Halls"
    OS = "Outdoor Spaces"


class Purpose(Enum):  # A class to give Enum values to the self.purpose attribute
    """Class to represent Purpose as ENUM values"""

    F = "Fundraising"
    M = "Musical concert"
    L = "Light show"


class SpecialEvent(Event):
    """Class to represent a Special Event as a Child of Event Class"""

    # Constructor
    def __init__(self, event_name='', duration='', location=ExhibitionLocation.PG,purpose=Purpose.M):  # We have an attribute that is initialized from the parent class, and we initialized 3 more attributes in this class. This means that a special event has 4 attributes, howeover, an event still has 1 attribute only.
        # This calls the constructor of the parent class (Event), and initializes the attributes of an event
        Event.__init__(self, event_name)

        # We initialized the new instance values that are in the special event class. There is no need to initialize the other attributes as we called the parent class constructor
        self._duration = duration
        self._location = location

        # For the special event, we gave special prices for different purposes
        if purpose == Purpose.F:
            special_price = 80

        elif purpose == Purpose.M:
            special_price = 60

        else:
            special_price = 100

        self._purpose = purpose
        self._special_price = special_price

        # Setter functions to set the attributes of a special event

    def set_duration(self, duration):
        self._duration = duration

    def set_location(self, location):
        self._location = location

    def set_purpose(self, purpose):
        self._purpose = purpose

    # Getter functions to set the attributes of a special event
    def get_purpose(self):
        return self._purpose.value

    def get_duration(self):
        return self._duration

    def get_location(self):
        return self._location.value

    # Function to display a new opening special event
    def display_new_event(self):
        print("Hosting New Special Event")
        print("Event name:", self.get_event_name())
        print("Duration:", self.get_duration())
        print("Location:", self.get_location())

