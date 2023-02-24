"""Geographic clustering of historical wildfire data
CS 210, University of Oregon
Thalia Hundt
Credits: TBD
"""
import doctest
import csv
import sys
sys.path.append('../../')
import config
import graphics

def make_map() -> graphics.utm_plot.Map:
    """Create and return a basemap display"""
    map = graphics.utm_plot.Map(config.BASEMAP_PATH,
                                config.BASEMAP_SIZE,
                                (config.BASEMAP_ORIGIN_EASTING, config.BASEMAP_ORIGIN_NORTHING),
                                (config.BASEMAP_EXTENT_EASTING, config.BASEMAP_EXTENT_NORTHING))
    return map

def get_fires_utm(path: str) -> list[tuple[int, int]]:
    """Read CSV file specified by path, returning a list 
    of (easting, northing) coordinate pairs within the 
    study area. 
    
    >>> get_fires_utm("data/test_locations_utm.csv")
    [(442151, 4729315), (442151, 5071453), (914041, 4729315), (914041, 5071453)]
    """
    with open(path, newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file)
    easting = int(row["Easting"])
    northing = int(row["Northing"])
    xy = []
    for y in path:
        print(xy)

        
        
    
def main():
    doctest.testmod()
    fire_map = make_map()
    input("Press enter to quit")

if __name__ == "__main__":
    main()
