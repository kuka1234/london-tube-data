# London Tube Helper

## This tool allows you to:
* View stations on each tube line.
* View lines that are accessible on each station.

### Enter 1 or 2 to depending on your needs.
#### Entering back will take you back to the first choice.

1. Enter line name, this will return every station on the line in the order of the stations.
2. Enter station name, this will return every line that is accessible on this station.

## For developers

### There are two tables: 
1. `Stations` table: (`id`: (VARCHAR), `name`: (VARCHAR))
2. `StationsLine` table: (`stationId` (VARCHAR), `lineName`(VARCHAR), `pos`(INT))

The `pos` column in `StationsLine` table is needed to order currently order the output of stations on a line.

The `stationsId` and id in the stations table are foreign keys.

#### Further improvements:
* Index `stations` table by `id`, and `StationsLine` table by `stationId` and `lineName`.
* Add `Primary key` and `Foreign keys` constraints on the table.
* Ensure the `StationsLine` table is always sorted respective to `pos` to ensure fast reads, as the result of the query will not have to be sorted.
* Functionality can be added to add new or remove old tube stations or lines.