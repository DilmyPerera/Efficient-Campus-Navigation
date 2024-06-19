import tkinter as tk
import heapq
import math  #For calculating positions on the canvas
from PIL import Image, ImageTk






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


# Sample campus map data with x, y coordinates for each building
campus_map = {
    "MAIN GATE": {"TP1": 100, "x": 600, "y": 580},
    "TP1": {"MAIN GATE": 35, "LIB": 110, "TP2": 25, "x": 600, "y": 535},
    "LIB": {"TP1": 110, "BS CANTEEN": 56, "x": 490, "y": 535},
    "TP2": {"TP1": 25, "BS CANTEEN": 60, "TP3": 34, "x": 600, "y": 510},
    "BS CANTEEN": {"TP2": 60, "LIB": 56, "FBS": 52, "x": 540, "y": 510},
    "TP3": {"TP2": 34, "FBS": 100, "TP4": 59, "x": 600, "y": 476},
    "FBS": {"TP3": 100, "BS CANTEEN": 52, "x": 500, "y": 476},
    "TP4": {"TP3": 59, "CP1": 40, "TP5": 49, "x": 600, "y": 417},
    "CP1": {"TP4": 40, "TP22": 34, "x": 640, "y": 432},
    "TP5": {"TP4": 49, "TP6": 107, "FAS CANTEEN": 108, "x": 600, "y": 368},
    "TP6": {"TP5": 107, "CP2": 93, "CL": 93, "x": 493, "y": 368},
    "CP2": {"TP6": 93, "TP7": 193, "x": 400, "y": 368},
    "CL": {"TP6": 93, "LH": 115, "x": 493, "y": 275},
    "LH": {"CL": 115, "TP23": 107, "x": 493, "y": 160},
    "TP7": {"CP2": 193, "MC": 62, "TP8": 60, "x": 300, "y": 368},
    "MC": {"TP7": 62, "x": 300, "y": 430},
    "TP8": {"TP7": 60, "TCH": 58, "TP9": 145, "x": 240, "y": 368},
    "TCH": {"TP8": 58, "x": 240, "y": 310},
    "TP9": {"TP8": 145, "FOT": 258, "x": 95, "y": 368},
    "FOT": {"TP9": 258, "TP10": 188, "x": 95, "y": 110},
    "TP10": {"FOT": 188, "EL": 40, "TP11": 210, "x": 283, "y": 110},
    "EL": {"TP10": 40, "x": 283, "y": 70},
    "TP11": {"TP10": 210, "LH4": 30, "TP12": 107, "x": 493, "y": 110},
    "LH4": {"TP11": 30, "x": 493, "y": 80},
    "TP12": {"TP11": 107, "TP13": 20, "x": 600, "y": 110},
    "TP13": {"TP12": 20, "TP23": 30, "SLH": 100, "TP14": 110, "x": 600, "y": 130},
    "SLH": {"TP13": 100, "x": 700, "y": 85},
    "TP14": {"TP13": 110, "CP3": 35, "CP5": 90, "x": 710, "y": 130},
    "CP3": {"TP14": 35, "x": 710, "y": 165},
    "CP5": {"TP14": 90, "TP15": 52, "x": 800, "y": 130},
    "TP15": {"CP5": 52, "FAS": 18, "TP16": 50, "x": 852, "y": 130},
    "FAS": {"TP15": 50, "x": 870, "y": 130},
    "TP16": {"TP15": 50, "FCH": 18, "x": 852, "y": 80},
    "FCH": {"TP16": 18, "TP17": 101, "x": 870, "y": 80},
    "TP17": {"FCH": 101, "TP18": 154, "x": 971, "y": 80},
    "TP18": {"TP17": 154, "CP4": 61, "x": 971, "y": 234},
    "CP4": {"TP18": 61, "TP19": 113, "x": 910, "y": 234},
    "TP19": {"CP4": 113, "TP20": 86, "x": 858, "y": 234},
    "TP20": {"TP19": 86, "ITC": 62, "TP21": 200, "x": 858, "y": 320},
    "ITC": {"TP20": 62, "x": 920, "y": 320},
    "TP21": {"TP20": 200, "AMMACHCHI": 72, "FBS MB": 58, "x": 858, "y": 520},
    "AMMACHCHI": {"TP21": 72, "Gate2": 10, "x": 930, "y": 550},
    "Gate2": {"AMMACHCHI": 10, "x": 950, "y": 560},
    "FBS MB": {"TP21": 58, "TP22": 126, "x": 800, "y": 497},
    "TP22": {"FBS MB": 126, "CP1": 34, "DOE": 32, "x": 674, "y": 447},
    "DOE": {"TP22": 32, "x": 674, "y": 415},
    "TP23": {"FAS CANTEEN": 100, "LH": 107, "x": 600, "y": 160},
    "FAS CANTEEN": {"TP5": 108, "TP23": 100, "x": 600, "y":260}
}


# Tkinter GUI implementation
def handle_find_path():
    source = source_entry.get()
    destination = destination_entry.get()

    if source not in campus_map or destination not in campus_map:
        result_label.config(text="Invalid source or destination. \nPlease try again.")
        return

    shortest_path, distance = find_shortest_path(campus_map, source, destination)

    if shortest_path:
        path_text = " \n↓\n ".join(shortest_path)
        result_label.config(text=f"Shortest Path: \n{path_text} \n(Distance: {distance} meters)")
        draw_map(shortest_path)
    else:
        result_label.config(text="No path found between these buildings.")
        draw_map([])

def draw_map(shortest_path):
    canvas.delete("all")  # Clear previous drawings
    canvas.create_image(0, 0, image=image, anchor='nw')

    # Draw all paths between buildings in gray
    for building, data in campus_map.items():
        x1, y1 = data['x'], data['y']
        for neighbor, distance in data.items():
            if neighbor not in ['x', 'y']:
                x2, y2 = campus_map[neighbor]['x'], campus_map[neighbor]['y']
                canvas.create_line(x1, y1, x2, y2, fill="gray")

                # Add distance labels to each path
                mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
                angle = math.atan2(y2 - y1, x2 - x1)
                offset_x = 10 * math.sin(angle)
                offset_y = 10 * math.cos(angle)
                #canvas.create_text(mid_x + offset_x, mid_y - offset_y, text=str(distance), font=("Arial", 8),
                #fill="gray")

    # Draw the shortest path in red
    if len(shortest_path) > 1:
        for i in range(len(shortest_path) - 1):
            building1 = shortest_path[i]
            building2 = shortest_path[i + 1]
            x1, y1 = campus_map[building1]['x'], campus_map[building1]['y']
            x2, y2 = campus_map[building2]['x'], campus_map[building2]['y']
            canvas.create_line(x1, y1, x2, y2, fill="red", width=4)

            # Add distance labels to the red paths
            distance = campus_map[building1][building2]
            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            angle = math.atan2(y2 - y1, x2 - x1)
            offset_x = 10 * math.sin(angle)
            offset_y = 10 * math.cos(angle)
            #canvas.create_text(mid_x + offset_x, mid_y - offset_y, text=str(distance), font=("Arial", 8), fill="red")

    # Draw buildings as dots with labels
    for building, data in campus_map.items():
        x, y = data['x'], data['y']
        if building in shortest_path:
            # Highlight buildings in the shortest path
            canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill="red", outline="red")
            canvas.create_text(x, y, text=building, font=("Arial", 8, "bold"), fill="white")
        else:
            # Regular buildings
            canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill="black", outline="black")
            canvas.create_text(x, y - 15, text=building, font=("Arial", 7), fill="white")    
            

root = tk.Tk()
root.title("University Path Finder")

# Set the window to fullscreen
root.state("zoomed")

# Create a frame for the left side controls
control_frame = tk.Frame(root)
control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

source_label = tk.Label(control_frame, text="Source:")
source_label.pack(anchor="w")

source_entry = tk.Entry(control_frame)
source_entry.pack(anchor="w")

destination_label = tk.Label(control_frame, text="Destination:")
destination_label.pack(anchor="w")

destination_entry = tk.Entry(control_frame)
destination_entry.pack(anchor="w")

find_button = tk.Button(control_frame, text="Find Shortest Path", command=handle_find_path)
find_button.pack(anchor="w", pady=10)

result_label = tk.Label(control_frame, text="")
result_label.pack(anchor="w")

