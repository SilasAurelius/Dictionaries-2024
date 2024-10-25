# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
"""
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
"""
ticket_number = 002.0
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_new_serive_ticket(service_tickets):
    new_customer = input("Enter customer name: ")
    new_issue = input("Enter issue: ")
    new_status = input("Enter status (open/closed): ")
    
    
    

while True:
    print("===MENU===")
    print("1. open new service ticket.")
    print("2. Update Status of ticket.")
    print("3. Display all tickets.")
    print("4. Display all tickets by status.")
    
    user_input = int(input("Enter numeric selection: "))
    if user_input == 1:
        add_new_serive_ticket()
        ticket_number += 1
        service_tickets[(f"Ticket{ticket_number}")][new]
    pass
