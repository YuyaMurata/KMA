import folium
import pandas as pd

cities = pd.DataFrame({
    'train': ['駒込', '日暮里', '池袋', '鶯谷'],
    'latitude': [35.736489, 35.727772, 35.728926, 35.720495],
    'longtude': [139.746875, 139.770987, 139.71038, 139.778837],
})

map = folium.Map(location=[35.736489, 139.746875], zoom_start=14)

for i, r in cities.iterrows():
    folium.Marker(location=[r['latitude'], r['longtude']], popup=r['train']).add_to(map)

map.save("map_train.html")

