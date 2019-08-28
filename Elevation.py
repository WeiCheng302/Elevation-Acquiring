import googlemaps
from googlemaps import convert
locations=(-22.88390639886955,-43.24645367951243)
def elevation(client, locations):
    params = {"locations": convert.shortest_path(locations)}
    return client._request("/maps/api/elevation/json", params).get("results", [])
gmap=googlemaps.Client(key='AIzaSyBA64oIPMzDbrmRc30sE3qZbKdCVRRiVLg')
result = elevation(gmap,locations)
print (result)
