import random
import time


def simulate_delivery_speed(base_speed, traffic_factor):
    # Simulate traffic affecting delivery speed
    delay = random.uniform(0, traffic_factor)
    time.sleep(delay)
    return base_speed + delay


# Number of markets
num_markets = 5

# Total amount of rice to distribute
total_rice = 10000  # in kilograms

# Distribute rice to markets
rice_distribution = [random.randint(100, 1000) for _ in range(num_markets)]

# Ensure the total distributed rice is equal to the total amount
total_distributed_rice = sum(rice_distribution)
if total_distributed_rice != total_rice:
    # Adjust the distribution to match the total amount
    ratio = total_rice / total_distributed_rice
    rice_distribution = [int(r * ratio) for r in rice_distribution]

# Simulate delivery to markets with traffic affecting speed
base_delivery_speed = 10  # in kg/s
traffic_factor = 5  # Random traffic factor affecting delivery speed

# Display the distribution and simulate delivery speed
for i in range(num_markets):
    delivery_speed = simulate_delivery_speed(
        base_delivery_speed, traffic_factor)
    delivery_time = rice_distribution[i] / delivery_speed
    print(
        f"Market {i + 1}: {rice_distribution[i]} kg, Delivery Speed: {delivery_speed:.2f} kg/s, Delivery Time: {delivery_time:.2f} seconds")

print(f"\nTotal Distributed Rice: {sum(rice_distribution)} kg")
