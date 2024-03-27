from Visitor import Visitor
from Visitor import VisitorType
from Exhibition import Exhibition
from SpecialEvent import SpecialEvent
from Tour import Tour
import random


class Ticket:
    """Class to represent a ticket"""

    # Constructor
    def __init__(self, visitor, event):  # It takes a visitor and an event as attributes

        # This checks if the visitor exists
        if not isinstance(visitor, Visitor):
            raise ValueError("The visitor does not exist.The ticket can not be generated")

        # This checks if the event exists
        if not isinstance(event, (Exhibition, Tour, SpecialEvent)):
            raise ValueError("The event does not exist. The ticket can not be generated")

        # The attributes are protected
        self.visitor = visitor
        self.event = event
        self.booking_method = self.booking_method()

        # This checks the type of visitor and gives the corresponding price
        if visitor.vis_type == VisitorType.A:
            ticket_price = 63

        elif visitor.vis_type in [VisitorType.C, VisitorType.S, VisitorType.T, VisitorType.ST]:
            ticket_price = 0

        else:
            ticket_price = event.special_price

        self.price = ticket_price

        # This automatically adds the ticket to the visitor ticket's list
        self.visitor.add_ticket(self)

    # Function to assign the booking method for a ticket
    def booking_method(self):
        return random.choice(["Online", "In Person"])

    # Function to display the ticket's details
    def display_ticket_details(self):
        print("Louvre Museum Ticket")
        print("")
        print("Visitor Information")
        print("Name:", self.visitor.get_vis_name())
        print("Age:", self.visitor.get_age())
        print("Visitor Type:", self.visitor.get_vis_type())
        print("Group Visit:", "Yes" if self.visitor.get_group() else "No")
        print("\nEvent Information")

        # Checks if the event is exhibition and prints its details
        if isinstance(self.event, Exhibition):
            print("Exhibition Name:", self.event.get_event_name())
            print("Duration:", self.event.get_duration())
            print("Location:", self.event.get_location())

        # Checks if the event is tour and prints its details
        elif isinstance(self.event, Tour):
            print("Tour Name:", self.event.get_event_name())
            print("Date:", self.event.get_date())
            print("Guide:", self.event.get_guide())
            print("Capacity:", self.event.get_capacity())

        # Checks if the event is special event and prints its details
        elif isinstance(self.event, SpecialEvent):
            print("Special Event Name:", self.event.get_event_name())
            print("Duration:", self.event.get_duration())
            print("Location:", self.event.get_location())
            print("Purpose:", self.event.get_purpose())

    # Function to display a ticket receipt
    def display_ticket_receipt(self):
        print("Visitor Information")
        print("Name:", self.visitor.get_vis_name())
        print("Age:", self.visitor.get_age())
        print("Visitor Type:", self.visitor.get_vis_type())
        print("Group Visit:", "Yes" if self.visitor.get_group() else "No")

        # Checks if the event is exhibition and prints its details
        if isinstance(self.event, Exhibition):
            print("Exhibition Name:", self.event.get_event_name())
            print("Price", self.price)

        # Checks if the event is tour and prints its details
        elif isinstance(self.event, Tour):
            print("Tour Name:", self.event.get_event_name())
            print("Price", self.price)


        # Checks if the event is special event and prints its details
        elif isinstance(self.event, SpecialEvent):
            print("Specil Event Name:", self.event.get_event_name())
            print("Price", self.price)

        # This checks if the visitor is a part of group and applies 50% discount
        if self.visitor.get_group():
            self.price = self.price * 0.5
            print("Group 50% discount:", self.price)

        # This applies the 5% vat to the total prices and prints it
        self.price += self.price * 0.05
        print("Total Price with 5% Vat:", self.price)

    # Function to get the price
    def get_price(self):
        return self.price

        # Function to get the event

    def get_event(self):
        return self.event

