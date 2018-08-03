#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe


import cgi
import functionsforDRW
import os

url = os.environ["REQUEST_URI"]
url = str(url)
token = functionsforDRW.parse_url(url, 'token')
token = int(token)
long = functionsforDRW.get_longitude(token)
lat = functionsforDRW.get_latitude(token)
name = functionsforDRW.get_name(token)
t = functionsforDRW.get_time(token)
time =''
for x in range(5):
    time += t[x]
a = """Content-Type: text/html\n\n
<html lang='en-US'>
<head>
<link rel = 'stylesheet' href='http://openlayers.org/en/v4.6.4/css/ol.css' type = 'text/css'>
<script src='http://openlayers.org/en/v4.6.4/build/ol.js' type='text/javascript'></script>
</head>
<body style='background-color:#A7ADC6;'>
<center><h3>
"""+ name + """ is in danger! As of """ + str(time) + """ they were located at these coordinates:
<div id= 'location'>""" + str((lat, long)) +"""</div>
<div> ............................................</div>
For an indepth search, enter these coordinates in Google maps.
<div><a href='http://www.google.com/maps' target='_blank'> <button type= 'button'>Google Maps</a></div>
<div id='map' class='map'></div>

<script>
var longitude ="""+str(long)+""";
var latitude = """+str(lat)+""";
var view;
var map;

function coordinates(){
var baseMapLayer = new ol.layer.Tile({
source: new ol.source.OSM()
});
var map = new ol.Map({
target: 'map',
layers: [ baseMapLayer],
view: new ol.View({
      center: ol.proj.fromLonLat([longitude, latitude]), // depends on user location // maybe do a function?
      zoom: 3 //Initial Zoom Level

    })
});

//Adding a marker on the map
var iconFeature = new ol.Feature({
geometry: new ol.geom.Point(
    ol.proj.fromLonLat([longitude, latitude]), //depend on user location

),

});

// iconFeature.setStyle(new Style({
//   image: new Icon (({
//     src: 'marker1.jpeg'
//   }))
// }));

var vectorSource = new ol.source.Vector({
features: [iconFeature],


});
var markerVectorLayer = new ol.layer.Vector({
source: vectorSource,

});
map.addLayer(markerVectorLayer);
}

function location1(){

}

window.onload = coordinates;
</script>
<style>
body{font-family:'courier new', serif;
font-size:20px;
color:white;
}
</style>
Audio, coming soon.
</center></h3>
</body>
</html>"""
print(a)
