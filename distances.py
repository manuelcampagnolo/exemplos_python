import random

# Constants
lat_min= 38.4
lat_max= 38.7
lon_min= -8.6
lon_max= -8.1

def get_coordinates(N: int) -> list:
    L=[]
    for _ in range(N):
        lat=get_decimal(f'Lat between {lat_min} and {lat_max}:',lat_min,lat_max)
        lon=get_decimal(f'Lon between {lon_min} and {lon_max}:',lon_min,lon_max)
        L.append((lat,lon))
    return(L)

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
            else:
                return random.uniform(Min, Max)


def compute_distance(L: list) -> float:
    pass


print(get_coordinates(3))



