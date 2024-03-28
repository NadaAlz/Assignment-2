from Event import Event
from ENUM import ExhibitionLocation


class Exhibition(Event):
    """Class to represent an Exhibition as a Child of Event Class"""

    # Constructor
    def __init__(self, event_name='', duration='',location=ExhibitionLocation.PG):  # We have an attribute that is initialized from the parent class, and we initialized 2 more attributes in this class. This means that an exhibition has 3 attributes, howeover, an event still has 1 attribute only.
        # This calls the constructor of the parent class (Event), and initializes the attributes of an event
        Event.__init__(self, event_name)

        # We initialized the new instance values that are in the exhibition class. There is no need to initialize the other attributes as we called the parent class constructor
        self._duration = duration
        self._location = location

    # Setter functions to set the attributes of an exhibition
    def set_duration(self, duration):
        self._duration = duration

    def set_location(self, location):
        self._location = location

    # Getter functions to set the attributes of an exhibition
    def get_duration(self):
        return self._duration

    def get_location(self):
        return self._location.value

    # Function to display a new opening exhibition
    def display_new_exh(self):
        print("Opening New Exhibition")
        print("Exhibition name:", self.get_event_name())
        print("Duration:", self.get_duration())
        print("Location:", self.get_location())

