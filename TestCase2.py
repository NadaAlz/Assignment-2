"""Test Case to open a new exhibition or event at the museum"""

from Exhibition import Exhibition
from Exhibition import ExhibitionLocation
from SpecialEvent import SpecialEvent
from SpecialEvent import Purpose
exhibition1 = Exhibition("UAE Heritage", "3 months", ExhibitionLocation.EH)
exhibition1.display_new_exh()
print("")
special_event1 = SpecialEvent("Jazz Night", "4 hours", ExhibitionLocation.OS, Purpose.M)
special_event1.display_new_event()