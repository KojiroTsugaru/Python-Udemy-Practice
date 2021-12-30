import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58,-99.89], zoom_start=6, tiles="Stamen Terrain")

def ColorProducer(elevation):
    if elevation < 1000:
        return 'green'
    if 1000 <= elevation < 3000:
        return 'orange'
    if elevation > 3000:
        return 'red'

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat,lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el), icon=folium.Icon(color=ColorProducer(el))))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))

map.add_child(fg)


map.save("Map1.html")