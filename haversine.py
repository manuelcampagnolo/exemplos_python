from myfunctions import mysqrt, mycos, myarcsin, mysqsin, get_decimal

def main():
    lat1=get_decimal('Latitude 1st point in decimal degrees',-90,90)
    lon1=get_decimal('Longitude 1st point in decimal degrees',-180,180)
    lat2=get_decimal('Latitude 2nd point in decimal degrees',-90,90)
    lon2=get_decimal('Longitude 2nd point in decimal degrees',-180,180)
    print(f"the distance between points is {haversine((lat1,lon1),(lat2,lon2))} km")

def haversine(p1,p2):
    R=6371
    lat1,lon1=p1 # degrees
    lat2,lon2=p2
    A=mysqsin((lat2-lat1)/2)
    B=mysqsin((lon2-lon1)/2)
    C=A*A+mycos(lat1)*mycos(lat2)*B*B
    if C<0:
        C=0
    H=mysqrt(C)
    if H>1: 
        H=1
    return 2*R*myarcsin(H)

lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

A=(-0.116773, 51.510357)
B=(-77.009003, 38.889931)

print(haversine(A, B))
    



