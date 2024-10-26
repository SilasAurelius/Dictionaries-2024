# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
"""
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
"""
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
    print("4. Display all tickets by status.")
    print("5. Quit")
    
    user_input = int(input("Enter numeric selection: "))
    if user_input == 1:
        new_customer = input("Enter customer name: ").title()
        new_issue = input("Enter issue: ").lower()
        new_status = input("Enter status (open/closed): ").lower()
        ticket_number += 1
        service_tickets[f"Ticket{ticket_number}"] = {"Customer": new_customer, "Issue": new_issue, "Status": new_status}
        print(service_tickets)
    elif user_input == 2:
        update_ticket = input("Enter ticket number i.e. 'Ticket000' etc.: ")
        update_status = input("Enter status (open/closed): ").lower()
        if update_ticket and new_customer not in ticket_number:
            print("Ticket number and/or customer name not found.")
        else:
            updated_service_ticket = {f"Ticket{ticket_number}": {"Customer": {new_customer}, "Issue": {new_issue}, "Status": {update_status}}} 
            service_tickets.update(update_status)
    elif user_input == 3:
        for display in service_tickets:
            print(f"\n{display}")
    elif user_input == 4:
        print(service_tickets.sort())
    else:
        print("Thank you for using the Customer Service Database.\nGoodbye")
        break
        
