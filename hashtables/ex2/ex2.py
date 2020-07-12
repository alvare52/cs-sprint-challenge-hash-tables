#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    
def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # tickets = list of Tickets
    # length = length of tickets list

    ticketsDictionary = {}
    route = [None] * length

    # fill dict with tickets
    for ticket in tickets:
        # print(ticket.source, ticket.destination)
        ticketsDictionary[ticket.source] = ticket.destination
        # first one should be source = "NONE", last is "NONE" for destination
        if ticket.source == "NONE":
            route[0] = ticket.destination
    
    i = 1
    # stop when the route list's last item is not None
    while route[length - 1] == None:
        route[i] = ticketsDictionary[route[i-1]]
        i += 1
        
    # print(ticketsDictionary)

    return route

# print("\n--START--")
# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# expected = ["PDX", "DCA", "NONE"]
# print(reconstruct_trip(tickets, 3))
