import heapq



def find_shortest_path(campus_map, source, destination):
    # Dijkstra's algorithm to find the shortest path
    priority_queue = [(0, source)]
    distances = {building: float('infinity') for building in campus_map}
    previous_buildings = {building: None for building in campus_map}
    distances[source] = 0

    while priority_queue:
        current_distance, current_building = heapq.heappop(priority_queue)

        if current_distance > distances[current_building]:
            continue

        for neighbor, weight in campus_map[current_building].items():
            if neighbor in ['x', 'y']:
                continue
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_buildings[neighbor] = current_building
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous_buildings[current]
    path.reverse()

    if path[0] == source:
        return path, distances[destination]
    else:
        return None, float('infinity')