import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the road network
road_network = nx.Graph()
road_network.add_edge('A', 'B', weight=1.5)  # Example road segment from A to B
road_network.add_edge('B', 'C', weight=2.0)  # Example road segment from B to C
# Add more road segments and intersections to model the Champaign-Urbana road network

# Step 2: Define the bus class
class Bus:
    def __init__(self, bus_id, route):
        self.bus_id = bus_id
        self.route = route
        self.current_location = route[0]  # Start at the first location
        self.speed = 1.0  # Adjust as needed
        self.passenger_capacity = 50  # Adjust as needed

    def move(self):
        # Move the bus along the route based on its speed
        current_index = self.route.index(self.current_location)
        next_index = (current_index + 1) % len(self.route)
        self.current_location = self.route[next_index]

    def __str__(self):
        return f"Bus {self.bus_id} - Current location: {self.current_location}"

# Step 3: Create a bus object
bus_route = ['A', 'B', 'C']  # Example route for the bus
bus = Bus(1, bus_route)

# Step 4: Simulate bus movement
simulation_steps = 10  # Number of simulation steps
for step in range(simulation_steps):
    bus.move()
    print(bus)

# Step 5: Visualize the road network and bus movement
pos = nx.spring_layout(road_network)  # Position the nodes in the graph
nx.draw(road_network, pos, with_labels=True, node_size=500, node_color='lightblue')  # Draw the road network
nx.draw_networkx_nodes(road_network, pos, nodelist=[bus.current_location], node_color='red', node_size=500)  # Draw the bus
plt.show()
