# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
"""
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
"""
from data_handling_functions import add_ticket, status_update, display_ticket

ticket_number = 2
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
} 

while True:
    print("===MENU===")
    print("1. open new service ticket.")
    print("2. Update Status of ticket.")
    print("3. Display all tickets.")
    print("4. Quit.")
    
    user_input = int(input("Enter numeric selection: "))
    if user_input == 1:
        add_ticket()       
    elif user_input == 2:
        status_update()
    elif user_input == 3:
        display_ticket()
    else:
        print("Thank you for using the Customer Service Database.\nGoodbye")
        break
        
