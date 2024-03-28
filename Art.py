from ENUM import ArtType
from ENUM import ExhibitionLocation



class Art:
    """Class to represent an art"""

    # Constructor
    def __init__(self, art_title='', art_type=ArtType.A, artist='', date_oc='', histSign='',
                 exhLoc=ExhibitionLocation.PG):  # We gave attributes for each art, and specified the type of values, we have string and Enum
        # Each attribute is protected by using one underscore "_"
        self._art_title = art_title
        self._art_type = art_type
        self._artist = artist
        self._date_oc = date_oc
        self._histSign = histSign
        self._exhLoc = exhLoc

    # Setter functions to set the attributes of an art
    def set_art_title(self, art_title):
        self._art_title = art_title

    def set_art_type(self, art_type):
        self._art_type = art_type

    def set_artist(self, artist):
        self._artist = artist

    def set_date_oc(self, date_oc):
        self._date_oc = date_oc

    def set_histSign(self, histSign):
        self._histSig = histSign

    def set_exhLoc(self, exhLoc):
        self._exhLoc = exhLoc

    # Setter functions to get the attributes of an art
    def get_art_title(self):
        return self._art_title

    def get_art_type(self):
        return self._art_type.value

    def get_artist(self):
        return self._artist

    def get_date_oc(self):
        return self._date_oc

    def get_histSign(self):
        return self._histSign

    def get_exhLoc(self):
        return self._exhLoc.value

        # Function to display an art object attributes

    def display_art(self):
        print("Art Title:", self.get_art_title())
        print("Art Type:", self.get_art_type())
        print("Artist:", self.get_artist())
        print("Date of Creation:", self.get_date_oc())
        print("Historical Significance:", self.get_histSign())
        print("Exhibition Location:", self.get_exhLoc())
