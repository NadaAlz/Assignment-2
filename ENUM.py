from enum import Enum

class VisitorType(Enum):  # A class to give Enum values to the self.vis_type attribute
    """Class to represent Visitor Type as ENUM values"""
    A = "Adult"
    C = "Child"
    S = "Senior"
    T = "Teacher"
    ST = "Student"

class ExhibitionLocation(Enum):  # A class to give Enum values to the self._exhLoc and self.location attribute
    """Class to represent Exhibition Location as ENUM values"""
    PG = "Permanent Galleries"
    EH = "Exhibition Halls"
    OS = "Outdoor Spaces"


class ArtType(Enum):  # A class to give Enum values to the self._art_type attribute
    """Class to represent Art Type as ENUM values"""

    A = "Artwork"
    B = "Artifact"
    C = "Exhibition"

class Purpose(Enum):  # A class to give Enum values to the self.purpose attribute
    """Class to represent Purpose as ENUM values"""

    F = "Fundraising"
    M = "Musical concert"
    L = "Light show"


