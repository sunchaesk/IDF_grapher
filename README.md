# IDF Grapher
generate graphs from Energyplus `.idf` files.
Tested only on Energyplus 23.1

## functionalities
`generate_connections`: returns list of list(start_zone, end_zone)
`generate_adjacency`: return dictionary of key: zone, val: list of connected zones


## dependencies
PLY
networkx - not-essential
