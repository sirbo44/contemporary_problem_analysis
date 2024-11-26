import folium, requests
from ip2geotools.databases.noncommercial import DbIpCity
from folium.plugins import MousePosition


# identify the IP address of the client
ip = requests.get('https://api.ipify.org').text
key = '949D49520ADEF75652B386A0317E08A8'
displays = ['240×160','320×240','432×240','480×270','480×320','640×400','800×480','854×480','1024×576','1280×720','1280×768','1280×800','1366×768','1366×900',
            '1440×900','1600×900','1680×945','1680×1050','1920×1080','1920×1200','2048×1152','2560×1440','2560×1600','3200×2048','3840×2160','3200×2400','3840×2400','5120×2880','5120×3200','5760×3240','6400×4096','6400×4800','7680×4320','7680×4800','15360×8640']





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
center = [37.97945, 23.71625]
m = folium.Map(control_scale=True,
                max_bounds=True,
                max_bounds_viscosity=1.0,
                location=center,#37.97945, 23.71625], # TO BE CHANGED TO [lat, lon] BEFORE RELEASE
                zoom_start=6, 
                min_lat=min_lat,
                max_lat=max_lat,
                min_lon=min_lon,
                max_lon=max_lon,
                min_zoom=3)

flights = requests.get('https://opensky-network.org/api/states/all').json()
flights = flights['states']
print("X:", flights[1][5], "Y:", flights[1][6])
print(type(flights[1][5]))



f = open('airports.csv', 'r+')
airports = f.readlines()
for i in range(len(airports)):
    airports[i] = airports[i].split(':')
    airports[i][15] = airports[i][15].replace('"\n', '')
    
    if airports[i][14] != 0.000 and airports[i][15] != 0.000 and airports[i][1] != 'N/A':
        if float(airports[i][14]) >= 29.24806 and float(airports[i][14]) <= 44.78027 and float(airports[i][15]) >= 2.61475 and float(airports[i][15]) <= 54.81349:
            folium.Marker(location=[airports[i][14],airports[i][15]], popup=airports[i][1]).add_to(m)
for flight in flights:
    if flight[5] != None and flight[6] != None:
        if float(flight[5]) >= 29.24806 and float(flight[5]) <= 44.78027 and float(flight[6]) >= 2.61475 and float(flight[6]) <= 54.81349:
            folium.Marker(location=[flight[5],flight[6]], popup=flight[1],icon=folium.Icon(icon='plane')).add_to(m)
# folium.Marker(location=[,], popup='test').add_to(m)
# MousePosition().add_to(m)




f.close()







m.save('map.html')


# [Your site name or product name] uses the IP2Location LITE database for <a href="https://lite.ip2location.com">IP geolocation</a>.