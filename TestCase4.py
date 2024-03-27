from Exhibition import Exhibition
from Exhibition import ExhibitionLocation
from SpecialEvent import SpecialEvent
from Tour import Tour
from Visitor import Visitor
from Visitor import VisitorType
from SpecialEvent import Purpose
from Ticket import Ticket

visitor1 = Visitor("Nada Mohd",19, VisitorType.ST,True)
visitor2 = Visitor("Dalal", 52, VisitorType.A, False)
visitor3 = Visitor("Maryam",26, VisitorType.A, False )
exhibition1 = Exhibition("UAE Heritage", "3 hours", ExhibitionLocation.EH)
special_event1 = SpecialEvent("Jazz Night", "4 hours", ExhibitionLocation.OS, Purpose.M)
tour1 = Tour("Heritage Tour", "May 3, 2024", "Salim")

ticket1 = Ticket(visitor1, exhibition1)
ticket2 = Ticket(visitor1, special_event1)
ticket3 = Ticket(visitor2, tour1)
ticket4 = Ticket(visitor3, special_event1)

visitor1.display_visitor_receipt()
print("------------------------------------------------------")
visitor2.display_visitor_receipt()
print("------------------------------------------------------")
visitor3.display_visitor_receipt()
print("------------------------------------------------------")