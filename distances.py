import random
import math
import matplotlib.pyplot as plt

# Constants
lat_min= 38.4
lat_max= 38.7
lon_min= -8.6
lon_max= -8.1
coef_lat=1100000 # 1 degree corresponds approx to ... meters
coef_lon=900000

def main():
    N=get_integer("Number of points: ",2,10)
    option=get_string("User provided (u) or random (r): ",["u","r"])
    # Create dictionary of coordinates
    d=get_coordinates(N,option)
    # Determine pair of points farthest apart
    max_dist=0
    for name_1,P1 in d.items():
        for name_2,P2 in d.items():
            dist=compute_distance(P1,P2)
            if dist >= max_dist:
                max_dist=dist
                point_1,point_2=name_1,name_2
    print(f"{point_1} and {point_2} are farthest apart")
    plot_scatter(d)

def plot_scatter(points: dict):
    x_vals = [point[0] for point in points.values()]
    y_vals = [point[1] for point in points.values()]
    plt.scatter(x_vals, y_vals)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot of Points')
    for label, point in points.items():
        plt.annotate(label, point, textcoords='offset points', xytext=(0, 10))
    plt.grid(True)
    plt.show()



def get_coordinates(N: int, option: str) -> list:
    d=dict()
    for _ in range(N):
        point_name=input("Point name: ")
        if option=='r':
            lat=random.uniform(lat_min, lat_max)
            lon=random.uniform(lon_min, lon_max)
        else:
            lat=get_decimal(f'Lat between {lat_min} and {lat_max}:',lat_min,lat_max)
            lon=get_decimal(f'Lon between {lon_min} and {lon_max}:',lon_min,lon_max)
        d[point_name]=lat,lon
    return(d)

# input: string (prompt to user), float (minimum value for input), float (maximum value for input)
# output: integer (user's provided integer between minimum and maximum)
def get_decimal(prompt: str,Min: float, Max: float) -> float:
    while True:
        try:
            x=float(input(prompt+' '))
        except ValueError:
            pass
        else:
            if Min <= x <= Max:
                return x



def get_integer(prompt: str,Min: int, Max: int) -> int:
    while True:
        try:
            x=int(input(prompt+' '))
        except ValueError:
            pass
        else:
            if Min <= x <= Max:
                return x


def get_string(prompt: str,L: list) -> str:
    while True:
        try:
            x=input(prompt+' ')
        except ValueError:
            pass
        else:
            if x in L:
                return x.lower()



def compute_distance(P1: tuple, P2: tuple) -> float:
    dx=P1[0]-P2[0]
    dy=P1[1]-P2[1]
    return math.sqrt(dx*dx+dy*dy)


#print(get_coordinates(3))
#print(compute_distance((0,10),(0,0)))
main()