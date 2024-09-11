import folium
from folium.plugins import HeatMap
import pandas as pd

def generate_heatmap(coordinates, output_file="heatmap.html"):
    """
    Generate a heatmap from a list of geographic coordinates.

    Args:
    coordinates (list of tuple): A list of (latitude, longitude) pairs.
    output_file (str): The file name where the heatmap will be saved.

    Returns:
    None
    """
    # Find the center of the map by averaging coordinates
    latitudes = [coord[0] for coord in coordinates]
    longitudes = [coord[1] for coord in coordinates]
    center_lat = sum(latitudes) / len(latitudes)
    center_lon = sum(longitudes) / len(longitudes)

    # Create a folium map centered on the average location
    m = folium.Map(location=[center_lat, center_lon], zoom_start=8)

    # Add the HeatMap layer to the map
    HeatMap(coordinates).add_to(m)

    # Save the map as an HTML file
    m.save(output_file)
    print(f"Heatmap saved to {output_file}")

def load_coordinates_from_csv(file_path, lat_column, lon_column):
    """
    Load coordinates from a CSV file using pandas.

    Args:
    file_path (str): Path to the CSV file.
    lat_column (str): Name of the column containing latitude.
    lon_column (str): Name of the column containing longitude.

    Returns:
    list of tuple: A list of (latitude, longitude) pairs.
    """
    df = pd.read_csv(file_path)

    # Extract latitude and longitude and create a list of tuples
    coordinates = list(zip(df[lat_column], df[lon_column]))

    return coordinates

# Example usage:
if __name__ == "__main__":
    # Path to your CSV file
    csv_file_path = "adsb_gt10k.csv"

    # Column names in the CSV file for latitude and longitude
    latitude_column = "latitude"
    longitude_column = "longitude"

    # Load coordinates from the CSV file
    coordinates = load_coordinates_from_csv(csv_file_path, latitude_column, longitude_column)

    # Generate the heatmap
    generate_heatmap(coordinates, "SEA_Paths_V2.html")
