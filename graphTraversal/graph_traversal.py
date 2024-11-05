from collections import defaultdict

def reconstructItinerary(adj_list, curr, itinerary):
    itinerary.append(curr)
    if curr not in adj_list:
        return itinerary  # Base case: no outgoing flights

    # Prioritize earlier destinations lexicographically
    for i in range(len(adj_list[curr])):
        if adj_list[curr][i] > adj_list[curr][0]:
            adj_list[curr][i], adj_list[curr][0] = adj_list[curr][0], adj_list[curr][i]

    for next_dest in adj_list[curr]:
        adj_list[curr].remove(next_dest)
        result = reconstructItinerary(adj_list, next_dest, itinerary)
        if result:
            return result
        adj_list[curr].append(next_dest)  # Backtrack

    itinerary.pop()  # Backtrack if no complete itinerary found
    return []

def findItinerary(tickets):
    adj_list = defaultdict(list)
    for ticket in tickets:
        adj_list[ticket[0]].append(ticket[1])

    itinerary = []
    result = reconstructItinerary(adj_list, "JFK", itinerary)
    return result

# Example usage
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
itinerary = findItinerary(tickets)
print("-> ".join(itinerary))
