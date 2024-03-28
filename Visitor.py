from ENUM import VisitorType #Import the Enum Library
from Exhibition import Exhibition
from SpecialEvent import SpecialEvent
from Tour import Tour



class Visitor:
    """Class to represent a Visitor"""

    # Constructor
    def __init__(self, vis_name='', age=0, vis_type=VisitorType.C,group=True):  # We gave attributes for each art, and specified the type of values, we have string, integer, bool, and ENUM.
        # The attributes are public
        self.vis_name = vis_name
        self.age = age
        self.vis_type = vis_type
        self.group = group
        # list of tickets that a visitor has
        self.tickets = []

    # Setter functions to set the attributes of a visitor

    def set_vis_name(self, vis_name):
        self.vis_name = vis_name

    def set_age(self, age):
        self.age = age

    def set_vis_type(self, vis_type):
        self.vis_type = vis_type

    def set_group(self, group):
        self.group = group

    # Getter functions to set the attributes of an art
    def get_vis_name(self):
        return self.vis_name

    def get_age(self):
        return self.age

    def get_vis_type(self):
        return self.vis_type.value

    def get_group(self):
        return self.group

    # Function to add the ticket to the visitor's tickets' list
    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    # Function to get the tickets
    def get_tickets(self):
        return self.tickets

    # Function to display all tickets that a visitor has
    def display_visitor_tickets(self):
        ticket_count = 0
        for ticket in self.get_tickets():
            ticket_count += 1  # This calculates the number of tickets the visitor has
            print("Ticket Number", ticket_count)
            ticket.display_ticket_details()  # This will display each ticket information, and this function is created in the Ticket Class
            print("")
            print("")

    # Functin to display all tickets' receipts for a visitor
    def display_visitor_receipt(self):
        # It shows the visitor's information
        print("Visitor Information")
        print("Name:", self.get_vis_name())
        print("Age:", self.get_age())
        print("Visitor Type:", self.get_vis_type())
        print("Group Visit:", "Yes" if self.get_group() else "No")

        total_price = 0  # Initialize the price to 0
        for ticket in self.get_tickets():  # This goes through each ticket

            # This checks if the event is exhibition, then it prints the exhibition details and adds the price
            if isinstance(ticket.event, Exhibition):
                print("Exhibition Name:", ticket.event.get_event_name())
                print("Price:", ticket.price)
                total_price += ticket.price

                # This checks if the event is tour, then it prints the tour details and adds the price
            elif isinstance(ticket.event, Tour):
                print("Tour Name:", ticket.event.get_event_name())
                print("Price:", ticket.price)
                total_price += ticket.price


            # This checks if the event is special event, then it prints the special event details and adds the price
            elif isinstance(ticket.event, SpecialEvent):
                print("Specil Event Name:", ticket.event.get_event_name())
                print("Price:", ticket.price)
                total_price += ticket.price

            # This checks if the visitor came with a group, then it applies 50% discount to the total price
            if self.get_group():
                total_price = total_price * 0.5
                print("Group 50% discount:", total_price)

        # Finally, this applies the 5% vat to the total price and prints the final total in the receipt
        total_price += total_price * 0.05
        print("Total Price with 5% Vat:", total_price)