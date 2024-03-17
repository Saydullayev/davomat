import math

def calculate_distance(lat1, lon1, lat2, lon2 ):
    earth_radius = 6371  # Radius of the earth in km
    d_lat = (lat2 - lat1) * math.pi / 180  # Convert degrees to radians
    d_lon = (lon2 - lon1) * math.pi / 180
    a = (
        math.sin(d_lat / 2) * math.sin(d_lat / 2) +
        math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) *
        math.sin(d_lon / 2) * math.sin(d_lon / 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c * 1000  # Distance in meters
    return distance
