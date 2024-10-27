def add_ticket():
    new_customer = input("Enter customer name: ").title()
    new_issue = input("Enter issue: ").lower()
    new_status = input("Enter status (open/closed): ").lower()
    ticket_number += 1
    service_tickets[f"Ticket00{ticket_number}"] = {"Customer": new_customer, "Issue": new_issue, "Status": new_status}
    print(service_tickets)
    
def status_update():
    update_ticket = input("Enter ticket number i.e. 'Ticket000' etc.: ")
    update_status = input("Enter status (open/closed): ").lower()
    if update_ticket not in service_tickets:
        print("Ticket number not found.")
    else:
        service_tickets[update_ticket]["Status"] = update_status
        print("Ticket updated successfully!")

def display_ticket():
    for ticket_id, data in service_tickets.items():
        print(f"\n{ticket_id} {data}")


