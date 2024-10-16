import numpy as np
from scipy.optimize import minimize

# Radius of the Earth in kilometers
R = 6371

# Function to calculate great-circle distance using the Haversine formula
def haversine(lat1, lon1, lat2, lon2, radius=R):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return radius * c

# Function to calculate the variance of distances from a candidate point to the three locations
def distance_variance(point, locations):
    lat, lon = point
    distances = [haversine(lat, lon, loc_lat, loc_lon) for loc_lat, loc_lon in locations]
    return np.var(distances)  # We want to minimize the variance

# Given locations (latitude, longitude) in degrees
locations = [
    (29.62581320033086, 52.55850268818534),
    (38.24829879437154, 48.29124638967477),
    (35.69973201622158, 51.33808843321214)
]

# Initial guess for the point (using the centroid as a starting point)
initial_guess = np.mean(locations, axis=0)

# Print initial guess (centroid) for debugging
print(f"Initial guess (centroid): {initial_guess}")

# Perform the optimization to find the point with the minimal distance variance
result = minimize(distance_variance, initial_guess, args=(locations,), method='Nelder-Mead', tol=1e-10)

# Extract the optimized latitude and longitude
optimized_lat, optimized_lon = result.x

# Print the final optimized point
print(f"{optimized_lat}, {optimized_lon}")