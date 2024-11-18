import folium, requests
from ip2geotools.databases.noncommercial import DbIpCity

# identify the IP address of the client
ip = requests.get('https://api.ipify.org').text
key = '949D49520ADEF75652B386A0317E08A8'

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

m = folium.Map(control_scale=True,
                max_bounds=True,
                max_bounds_viscosity=1.0,
                location=[37.97945, 23.71625], # TO BE CHANGED TO [lat, lon] BEFORE RELEASE
                zoom_start=6, 
                min_lat=min_lat,
                max_lat=max_lat,
                min_lon=min_lon,
                max_lon=max_lon,
                min_zoom=3)

# flights = requests.get('https://opensky-network.org/api/states/all').json()
# print(flights)

f = open('airports.csv', 'r+')
airports = f.readlines()
for i in range(len(airports)):
    airports[i] = airports[i].split(':')
    airports[i][15] = airports[i][15].replace('"\n', '')
    
    if airports[i][14] != 0.000 and airports[i][15] != 0.000 and airports[i][1] != 'N/A':
        if float(airports[i][14]) >= 32.5889 and float(airports[i][14]) <= 43.1 and float(airports[i][15]) >= 8.7425 and float(airports[i][15]) <= 38.69:
            folium.Marker(location=[airports[i][14],airports[i][15]], popup=airports[i][1]).add_to(m)
f.close()







m.save('map.html')


# [Your site name or product name] uses the IP2Location LITE database for <a href="https://lite.ip2location.com">IP geolocation</a>.