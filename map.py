import folium, requests, json
from ip2geotools.databases.noncommercial import DbIpCity
from folium.plugins import MousePosition, Search
from folium.features import GeoJson
import math
from bs4 import BeautifulSoup


# identify the IP address of the client
ip = requests.get('https://api.ipify.org').text
key = '949D49520ADEF75652B386A0317E08A8'

# Get map bounds





# get the location of the client
#
# TO BE UNCOMMENTED BEFORE RELEASE
#
# response = requests.get('https://api.ip2location.io/?key={}&ip={}'.format(key, ip)).json()
# lat = response['latitude']
# lon = response['longitude']

# create a map
min_lat = -90
max_lat = 90
min_lon = -180
max_lon = 180
center = [0,0]                   # CENTER FOR TESTING
zoom = 6
m = folium.Map(control_scale=True,
                max_bounds=True,
                max_bounds_viscosity=1.0,
                location=center,#37.97945, 23.71625], # TO BE CHANGED TO [lat, lon] BEFORE RELEASE
                zoom_start=zoom, 
                min_lat=min_lat,
                max_lat=max_lat,
                min_lon=min_lon,
                max_lon=max_lon,
                min_zoom=3)
flights = requests.get('https://opensky-network.org/api/states/all').json()
flights = flights['states']
print("X:", flights[1][5], "Y:", flights[1][6])
print(type(flights[1][5]))


#TEST FOR FINDING THE TOP RIGHT CORNER
coords = [math.tan(math.degrees(45) + center[0]/2), center[1]]
print(coords)




f = open('airports.json', 'r+', encoding='utf-8-sig')
airports = json.loads(f.read())
airports_locations = folium.FeatureGroup(name="Airports").add_to(m)



for i in range(len(airports)):    
    if airports[i]['latitude'] != 0.000 and airports[i]['longitude'] != 0.000 and airports[i]['code'] != 'N/A':
        if float(airports[i]['latitude']) >= 29.24806 and float(airports[i]['latitude']) <= 44.78027 and float(airports[i]['longitude']) >= 2.61475 and float(airports[i]['longitude']) <= 54.81349:
            folium.Marker(location=[airports[i]['latitude'],airports[i]['longitude']], popup=airports[i]['code']).add_to(airports_locations)
for flight in flights:
    if flight[5] != None and flight[6] != None:
        if float(flight[5]) >= 29.24806 and float(flight[5]) <= 44.78027 and float(flight[6]) >= 2.61475 and float(flight[6]) <= 54.81349:
            folium.Marker(location=[flight[5],flight[6]], popup=flight[1],icon=folium.Icon(icon='plane')).add_to(m)
#folium.Marker(location=top_right_coords, popup='test', icon=folium.Icon(color='red')).add_to(m)        # RED MARKER FOR TESTING



statesearch = Search(
    layer=airports_locations,
    placeholder="Search ...",
    collapsed=False,
    search_label="name",
    weight=3,
    position='topright'
).add_to(m)







folium.LayerControl().add_to(m)
MousePosition().add_to(m)




f.close()
m.save('map.html')

map_html = m.get_root().render()
soup = BeautifulSoup(map_html, 'html.parser')
scripts = soup.find('script')
for i in range(7):
    scripts = scripts.find_next('script')
new_tag = soup.new_tag('script')
new_tag.string = """
            let mapElement = document.querySelector(".folium-map");
            let bounds = window[mapElement.id].getBounds();
            console.log("Top-right corner: ", bounds.getNorthEast());
            """
scripts.insert_after(new_tag)
with open('map.html', 'w') as f:
    f.write(str(soup))

print(bounds.getNorthEast())



# [Your site name or product name] uses the IP2Location LITE database for <a href="https://lite.ip2location.com">IP geolocation</a>.





# for [0,0] -> top right corner is 10.46621, 21.07178
# for [0,100] -> bottom left corner is 10.46621, 121.07178
# for [10,0] -> top right corner is 20.1591, 21.07178
# for [10,100] -> bottom left corner is 20.1591, 121.07178

# SUMURRIZE
# FOR MOVEMENTS IN X AXIS MAKES NO PROBLEM, THE DISTANCE IS THE SAME

# for [0,0] -> top right corner is 10.46621, 21.07178
# for [10,0] -> top right corner is 20.1591, 21.07178
# for [40,0] -> bottom left corner is 47.59135, 21.07178
# FOR MOVEMENTS IN Y AXIS, THE DISTANCE IS NOT THE SAME
