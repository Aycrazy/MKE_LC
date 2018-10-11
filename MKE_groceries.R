library(tidyverse)
library(readxl)
library(RSocrata)
library(data.table)
library(leaflet)
library(geojsonio)
library(rgdal)
library(htmltools)

setwd("~/Documents/MKE_OD")

#mke <- rgdal::readOGR("mke_geo.geojson", "OGRGeoJSON")

mke <- geojsonio::geojson_read("mke_geo.geojson",what = "sp")

mke@data

map.county <- map_data('county') %>%
    filter(region %in% c('wisconsin')) %>%
    rename( county = subregion, state = region) %>%
    filter(county == 'milwaukee')
    
View(map.county)

mke.points <- fortify(mke)

#points outline map
ggplot() +
    geom_path(data=mke.points, aes(long, lat, group = group))+
    coord_map() +
    geom_point(data = groc_snap,aes(x=latG, y = longG, color = snap))

pal <- colorNumeric("viridis", NULL)


#map points
leaflet(groc_snap) %>% addTiles() %>%
    addMarkers(~latG, ~longG, popup =  ~htmlEscape(store_name))
    
mke$style = list(
    weight = 1,
    color = "#555555",
    opacity = 1,
    fillOpacity = 0.8
)

leaflet() %>% addGeoJSON(mke)


ggplot(mke)+
    geom_polygon()

groc_snap <- read_csv('groceries_snap.csv')

