from graph.graph import Graph


def business_trip(graph, destination):
    """
       function called business trip
       Arguments: graph, array of city names
       Return: the cost of the trip (if it’s possible) or null (if not)
    """
    if graph.get_nodes() is not None and destination:

        weight_total = 0

        for i, dest in enumerate(destination):
            connecting_flights = graph.get_neighbors(dest)
            if i < len(destination) - 1:
                next_dest = destination[i + 1]
            else:
                break

            connection_list = [x.vertex for x in connecting_flights]

            if next_dest not in connection_list:
                return (False, 0)

            weight_next_dest = [x.weight for x in connecting_flights if x.vertex == next_dest]

            weight_total += sum(weight_next_dest)

        return True, weight_total
    return False, 0