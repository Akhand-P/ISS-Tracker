import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url="http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("This time " +
           str(result["number"]) + " astronauts on the International Space Station: \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")
# print longitude and latitude
g = geocoder.ip('me')
file.write("\nYour current latitute and longitude are: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("map.gif")
screen.register_shape("iss2.gif")
iss = turtle.Turtle()
iss.shape("iss2.gif")
iss.setheading(45)
iss.penup()

while True:
    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    # Extract the ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    # Ouput lon and lat to the terminal
    latitude = float(lat)
    longitude = float(lon)
    print("\nLatitude: " + str(latitude))
    print("\nLongitude: " + str(longitude))

    # Update the ISS location on the map
    iss.goto(longitude, latitude)

    # Refresh each 1 seconds
    time.sleep(1)
