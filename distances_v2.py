# Problem P4

import random
import math
import matplotlib.pyplot as plt
import string
import haversine as hs # haversine great-circle distance on a sphere

# Constants for the region of interest (ROI)
lat_min= 38.7 # minimum latitude in decimal degrees
lat_max= 38.78 # maximum latitude in decimal degrees
lon_min= -9.2 # same for longitude
lon_max= -9.1

def main():
    N=get_integer("Number of points: ",2,10)
    option=get_string("User provided (u), random (r), or automatic (a): ",["u","r","a"])
    # Create dictionary of coordinates
    d=get_coordinates(N,option)
    # Determine pair of points farthest apart
    point_1,point_2=farthest_apart(d)
    # print result and plot points
    print(f"{point_1} and {point_2} are farthest apart")
    plot_scatter(d)

# input dictionary of points
# side effect: scatter plot of points with labels
def plot_scatter(points: dict):
    x_vals = [point[0] for point in points.values()]
    y_vals = [point[1] for point in points.values()]
    plt.scatter(x_vals, y_vals)
    plt.xlabel('Lon')
    plt.ylabel('Lat')
    plt.title('Scatter Plot of Points')
    for label, point in points.items():
        plt.annotate(label, point, textcoords='offset points', xytext=(0, 10))
    plt.grid(True)
    plt.show()

# inputs: integer (number of points), string (option: user provided "u", random "r" or automatic "a")
# output: dictionary of points. The key is the point name and the value is a tuple lon,lat in decimal degrees
def get_coordinates(N: int, option: str) -> list:
    d=dict()
    for i in range(N):
        if option=='a':
            point_name=string.ascii_lowercase[i]
        else: 
            point_name=input("Point name: ")
        if option in ['r','a']:
            lon=random.uniform(lon_min, lon_max)
            lat=random.uniform(lat_min, lat_max)
        else:
            lon=get_decimal(f'Lon between {lon_min} and {lon_max}:',lon_min,lon_max)
            lat=get_decimal(f'Lat between {lat_min} and {lat_max}:',lat_min,lat_max)
        d[point_name]=lon,lat
    return d

# input: string (prompt to user), float (minimum value for input), float (maximum value for input)
# output: float (user's provided value between minimum and maximum)
def get_decimal(prompt: str,Min: float, Max: float) -> float:
    while True:
        try:
            x=float(input(prompt+' '))
        except ValueError:
            pass
        else:
            if Min <= x <= Max:
                return x

# input: string (prompt to user), integer (minimum value for input), integer (maximum value for input)
# output: integer (user's provided value between minimum and maximum)
def get_integer(prompt: str,Min: int, Max: int) -> int:
    while True:
        try:
            x=int(input(prompt+' '))
        except ValueError:
            pass
        else:
            if Min <= x <= Max:
                return x

# input: string (prompt to user), list (list of strings that acceptable values)
# output: string (user's provided value among the values in L)
def get_string(prompt: str,L: list) -> str:
    while True:
        try:
            x=input(prompt+' ')
        except ValueError:
            pass
        else:
            if x in L:
                return x.lower()

# input: tuple (lon,lat for 1st point), tuple (lon,lat for 2nd point)
# output: float (approximate distance in meters between P1 and P2)
def compute_distance(P1: tuple, P2: tuple) -> float:
    return hs.haversine(P1,P2)

# input: dictionary of points. The key is the point name and the value is a tuple lon,lat in decimal degrees
# output: tuple (name of point 1, name of point 2), where point 1 and 2 are the farthest aprt
def farthest_apart(d: dict) -> tuple:
    max_dist=0
    for name_1,P1 in d.items():
        for name_2,P2 in d.items():
            dist=compute_distance(P1,P2)
            if dist >= max_dist:
                max_dist=dist
                point_1,point_2=name_1,name_2
    return point_1,point_2

main()
