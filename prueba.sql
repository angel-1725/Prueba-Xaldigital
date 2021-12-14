/*1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año? BENITO JUAREZ*/
select NOMBRE_AEROPUERTO from aereopuertos WHERE ID_AEROPUERTO = (select ID_AEROPUERTO from(select ID_AEROPUERTO, count(*)  as c from (select ID_AEROPUERTO, DIA from vuelos WHERE DIA>="2021-01-01") as t group by ID_AEROPUERTO order by c desc limit 1)as t1);
/*2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año? Aeromar*/
select NOMBRE_AEROLINEA from aereolineas WHERE ID_AEROLINEA = (select ID_AEROLINEA from(select ID_AEROLINEA, count(*)  as c from (select ID_AEROLINEA, Y from vuelos WHERE DIA>="2021-01-01") as t group by ID_AEROLINEA order by c desc limit 1)as t1);
/*3. ¿En qué día se han tenido mayor número de vuelos? 2021-05-02*/
select DIA from(select DIA, count(*)  as c from vuelos group by DIA order by c desc limit 1)as t;
/*4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día? Ninguna, todas tienen como maximo 2, excepto Aeromexico con maixmo un vuelo */
select NOMBRE_AEROLINEA from aereolineas where ID_AEROLINEA in (select ID_AEROLINEA from (select count(DIA) as c, ID_AEROLINEA,DIA from vuelos group by ID_AEROLINEA,DIA) as t where t.c>2);