class Event:
    """Class to represent an Event"""

    # Constructor
    def __init__(self, event_name=''):  # An event has one attribute only and its type is string
        self._event_name = event_name

        # Setter function to set the event name

    def set_event_name(self, event_name):
        self._event_name = event_name

    # Getter function to set the event name
    def get_event_name(self):
        return self._event_name