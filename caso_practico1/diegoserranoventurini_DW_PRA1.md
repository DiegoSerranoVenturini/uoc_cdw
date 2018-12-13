# CASO PRACTICO - 1 - diegoserranoventurini

NOTA INICIAL: La descripcion de los datos proporcionados se realiza en el punto 3 del ejericio; sin embargo, para dar una respuesta completa a las preguntas planteadas en el resto de apartados es imprescindible haber analizado previamente los datos. Por ello, el hilo argumental de las respuestas queda un tanto confuso ya que se asume un conocimiento de los datos que formalmente no ha sido planteado.

## Análisis de requerimientos

En este apartado se pretende realizar un estudio de los posibles casos de uso y necesidades que la construccion de este DWHU (_Data WareHouse Unified_) pretende dar respuesta.

Los agentes que se especifican en el enunciado son varios, y de naturaleza e intereses muy diversos (y contrapuestos en algunos casos). Los que se enumeran, sin detallar sus intereses particulares son:

- Sector turismo: OMT, agencias de viajes, cadenas hoteleras...
- Aerolineas
- Industria aerocomercial: tiendas en los aeropuertos, empresas de servicios alrededor de aeropuertos, servicios auxiliares aeroportuarios, ...
- Administracion publica
- Ciudadanos

En este caso practico/proyecto se pretende construir un DWHU que centraliza cierta informacion relevante a la actividad economica generada por las aerolineas y el trafico de viajeros en los aeropuertos. El principal uso de esta informacion es conocer la evolucion del numero de pasajeros entre paises; la actividad de las aerolineas; las rutas entre los paises y el impacto que estos numeros han tenido en sus ingresos vinculados al turismo.

Podemos identificar por tanto las siguientes necesidades para varios de los grupos interesados:

- Sin duda tanto para las administraciones publicas como para las privadas interesante conocer la evolucion del impacto del turismo en las economias nacionales. Encontramos que existen varias metricas socio-economicas interesantes en el conjunto de datos. Si un pais esta experimentando una tendencia ascendiente de visitantes y de ingresos puede plantearse inversiones en infraestructuras; mientras que otro que vea su numero de visitantes disminuir puede decidir aumentar su inversion en marketing y posicionamiento. 
- Para el sector turismo privado es importante conocer la actividad economica de las diferentes aerolineas, donde operan, con que equipamiento y con que volumen. Por ejemplo, una empresa que proporcione servicios de mantenimiento de aviones puede detectar lugares en los que sus _partners_ (aerolineas) esten operando y ellos no.
- Una necesidad que satisfaceria este DHW seria conocer el grado de conexion de los diferentes paises, es decir, cuanto trafico aereo tienen de salida y entrada. Esta metrica ayudaria a saber si un pais esta mas aislado o si tiene una mayor exposicion al turismo. Esto abriria la puerta a que las aerolineas puedan plantear nuevas rutas a paises pobremente conectados.
- Finalmente los ciudadanos conocerian el grado de expansion de las aerolineas y los codigos de todas las rutas y la actividad economica que la actividad de estas genera. De esta manera, tendrian mas argumentos para poder cuestionar politicas orientadas al turismo; y un mayor conocimento de los lugares que podrian emplear como destino vacacional.


En resumen, este DWH permitiria conocer la evolucion macro de la actividad turistica de los paises y cuan abiertos estan al resto del mundo; asi como el detalle de la actividad de las aerolineas en estos paises.

## Indicadores, hechos, dimensiones, atributos

A continuacion, como parte del proceso de definicion del DWHU vamos a identificar los hechos y dimensiones con sus metricas y sus atributos dentro de los datos proporcionados. Este contenido se empleara y extendera con los hechos derivados en el disenho formal del modelo multidimensional.

Las dimensiones identificadas son las siguientes:

- Dimension `Lugar`. Existen tres niveles en esta dimension el aeropuerto, la ciudad y el pais. Cada uno de los cuales tiene varios atributos especificos. Algunos ejemplos son: geoposicionamiento, codigo identificativo, uso horario, continente...
- Dimension `Tiempo`. La granularidad de los datos es anual, ya que no se proporcionan hechos en otra unidad: dias, horas, o meses, etc.
- Dimension `Aerolinea`. Aunque existen aerolineas que son secciones de otras (como las low-cost de companhias grandes) no se especifica dicha relacion de jerarquia por lo que solo existe un nivel de granularidad.
- Dimension `Indicadores`. Esta dimension ayuda a identificar los hechos en las tablas historicas.
- Dimension `Equipamiento`. Esta dimension indica el tipo de tecnologia o aeronave empleada en el desempenho de la actividad.

En cuanto a hechos encontramos los siguientes:

- Rutas. Este hecho podria considerarse casi dimension es una interseccion entre varias dimensiones anteriores (Lugar - Aerolinea); contiene atributos propios como `stops` (numero de paradas), e interpretamos que es un "punto de vista desde el que se pueden analizar los datos", ya que se podrian generar reportes como numero de rutas que un pais contiene de entrada. Dicha metrica daria respuesta a uno de los requerimientos planteados.
- Numero de pasajeros anuales.
- Total de ingresos generados por el turismo en un pais.
- Porcentaje del GDP dedicado al intercambio comercial
- Numero de aerolineas que operan en un pais
- Numero de conexiones entre dos paises
- Numero de rutas entrantes/salientes de un pais 

Como se ha comentado en el apartado del disenho multidimensional se indicara como se agrupan dichas dimensiones y hechos en el DWHU; asi como el detalle de los atributos existentes.

## Analisis del _dataset_ proporcionado

En este apartado analizaremos todas las tablas proporcionadas, indicando para cada tabla los campos que contienen, su nombre (original y castellano), una breve descripcion del dato, su tipo y el nivel de informacion que contiene.

### `airlines.dat` 

--------------------------------------------------------------------------
 Atributo     Atributo (ESP)          Desc           Tipo    Nivel inf 
------------ ---------------- --------------------- ------ ---------------
 Airline ID    ID aerolinea    Identificador unico    INT   1 nivel con 
                                de la aerolinea en          6048 tipos
                                   OpenFlights                   

    Name         Nombre          Nombre de la          STR    1 nivel
                                 aerolinea    

   Alias          Alias        Alias por el que se     STR    1 nivel
                               conoce la aerolinea

   IATA           IATA           IATA codigo de 2      STR    1 nivel
                                      letras 
                               (si esta disponible)          
   
   ICAO           ICAO           ICAO codigo de 3      STR    1 nivel
                                     letras 
                               (si esta disponible)

  Callsign        Senal        Nombre por el que se    STR    1 nivel
                                 llama a las 
                                  aerolineas     

   Country        Pais         Pais o territorio       STR    1 nivel
                                 donde reside la     
                                    aerolinea 

   Active        Activa        Flag que indica si      STR    1 nivel 
                               la aerolinea esta             (equivalente 
                               	    activa o no                  a Y/N)
                                                   
--------------------------------------------------------------------------


### `airports.dat` 

-----------------------------------------------------------------------------
 Atributo     Atributo (ESP)          Desc            Tipo      Nivel inf 
------------ ---------------- ---------------------- -------- ---------------
 Airport ID    ID aeropuerto   Identificador unico     INT       1 nivel 
                                del aeropuerto en                 
                                   OpenFlights                      

   Name          Nombre           Nombre del           STR       1 nivel 
                                  aeropuerto
   
   City          Ciudad           Nombre de la         STR       1 nivel
                                   ciudad donde 
                                   se encuentra el
                                   aeropuerto                           

   Country        Pais            Nombre del           STR       1 nivel
                                   pais donde                                                                                      
                                  se encuentra el                                                                                       
                                    aeropuerto                                                                                      
                                                                                                                                                                                                                                                 
   IATA	        IATA              IATA codigo de       STR       1 nivel
                                    3 letras                                                                                                           
                                                                                                                          
   ICAO	        ICAO              ICAO codigo de       STR       1 nivel
                                    4 letras                                                                                 
                                                                                                                          
 Latitute      Latitud            Grados decimales     FLOAT       6 
                                  (negativo es sur,             decimales
                                  	positivo es norte)                                                                                                      
                                                                                                                       
 Longitude     Longitud            Grados decimales    FLOAT        6 
                                  (negativo es                  decimales
                                  	oeste, 
                                   positivo es 
                                    este)                                              
                                                                                                                       
 Altitude      Altitud              Altitud en         FLOAT        6  
                                       "pies"                    decimales                                                                 
                                                                                                                       
 Timezone      Uso horario          Horas de 
                                     diferencia        FLOAT      1 decimal
                                      respecto a                                                                                
                                        UTC                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
  DST           DST               Horario de           STR     1 nivel -
                                    invierno (                 7 valores
                                    E - EUROPA,
                                    A - US/CAN,
                                    S - America Sur
                                    0 - AUST
                                    Z - Nueva Zel.
                                    N - None
                                    U - Desconocido
                                    )

  TZ          Zona horaria         Zona horaria en     STR      1 nivel
                                       Olson 
 
  Type         Tipo                Tipo aeropuerto     STR      1 nivel -
                                                                4 valores

--------------------------------------------------------------------------
 

### `routes.dat` 

--------------------------------------------------------------------------
 Atributo     Atributo (ESP)          Desc           Tipo    Nivel inf 
------------ ---------------- --------------------- ------ ---------------
 Airline ID    ID aerolinea    Identificador unico    INT   1 nivel con 
                                de la aerolinea en          6048 tipos
                                   OpenFlights                   

 Airline       Nombre            Nombre de la         STR    1 nivel
               aerolinea           aerolinea    


 Source       Aeropuerto         codigo IATA/ICAO     STR    1 nivel
 airport       origen            del aeropuerto
                                  de origen
                               
 Source       ID Aeropuerto     codigo OpenFlights    STR    1 nivel
 airport       origen            del aeropuerto
   ID                             de origen

Destination   Aeropuerto         codigo IATA/ICAO     STR    1 nivel
 airport       destino            del aeropuerto
                                  de destino
                                  
Destinatio   ID Aeropuerto     codigo OpenFlights     STR    1 nivel
 airport       destino            del aeropuerto
   ID                             de destino

Codeshare    Compartido         indicador de si       STR    1 nivel
                                 el vuelo esta 
                                 compartido

 Stops        Paradas           numero de paradas     INT    1 nivel

 Equipment    Equipamiento      tres letras           STR
                                 indicando 
                                 el 
                                 equipamiento               

--------------------------------------------------------------------------


### `worldbank_comercio_ext_anual_pais.csv` 

--------------------------------------------------------------------------
 Atributo     Atributo (ESP)          Desc           Tipo    Nivel inf 
------------ ---------------- --------------------- ------ ---------------      
  Country      Nombre Pais       Nombre del          STR     1 nivel
   Name                               pais                

  Country      Codigo Pais       Codigo del          STR     1 nivel
   Code                               pais                

 Indicator     Codigo            Codigo del 
   Code        Indicador           indicador         STR     1 nivel

 Indicator     Nombre            Nombre del 
   Name        Indicador           indicador         STR     1 nivel
  
  YEAR         ANHO             Sucesion de          INT     anhos desde     
                                   anhos                       1960

--------------------------------------------------------------------------

### `worldbank_ing_turismo_anual_pais.csv` 

--------------------------------------------------------------------------
 Atributo     Atributo (ESP)          Desc           Tipo    Nivel inf 
------------ ---------------- --------------------- ------ ---------------      
  Country      Nombre Pais       Nombre del          STR     1 nivel
   Name                               pais                

  Country      Codigo Pais       Codigo del          STR     1 nivel
   Code                               pais                

 Indicator     Codigo            Codigo del 
   Code        Indicador           indicador         STR     1 nivel

 Indicator     Nombre            Nombre del 
   Name        Indicador           indicador         STR     1 nivel
  
  YEAR         ANHO             Sucesion de          INT     anhos desde     
                                   anhos                       1960

--------------------------------------------------------------------------

### `worldbank_pasajeros_anual_pais.csv` 

--------------------------------------------------------------------------
 Atributo     Atributo (ESP)          Desc           Tipo    Nivel inf 
------------ ---------------- --------------------- ------ ---------------

  Country      Codigo Pais       Codigo del          STR     1 nivel
   Code                               pais                

 Indicator     Codigo            Codigo del 
   Code        Indicador           indicador         STR     1 nivel

 Indicator     Nombre            Nombre del 
   Name        Indicador           indicador         STR     1 nivel
  
  YEAR         ANHO             Sucesion de          INT     anhos desde     
                                   anhos                       1960

--------------------------------------------------------------------------

### `worldbank_poblacion_anual_pais.csv` 

--------------------------------------------------------------------------
 Atributo     Atributo (ESP)          Desc           Tipo    Nivel inf 
------------ ---------------- --------------------- ------ ---------------
  Country      Codigo Pais       Codigo del          STR     1 nivel
   Code                               pais                

 Indicator     Codigo            Codigo del 
   Code        Indicador           indicador         STR     1 nivel

 Indicator     Nombre            Nombre del 
   Name        Indicador           indicador         STR     1 nivel
  
  YEAR         ANHO             Sucesion de          INT     anhos desde     
                                   anhos                       1960

--------------------------------------------------------------------------

### `equipamientos.js` 

----------------------------------------------------------------------------------- 
 Atributo           Atributo (ESP)          Desc              Tipo    Nivel inf 
------------------ ------------------- --------------------- ------ ---------------
desc_equipamiento   desc_equipamiento   Descripcion            STR    1 nivel
                                         equipamiento 
                                         (aeronave)               

cod_equipamiento    cod_equipamiento    Codigo equipamiento    STR    1 nivel

-----------------------------------------------------------------------------------

### `paises.xml`

-------------------------------------------------------------------------------------
 Atributo           Atributo (ESP)          Desc               Tipo    Nivel inf 
------------------ ------------------ ---------------------- -------- ---------------
  cod_pais             cod_pais             Codigo pais        STR       1 nivel        
        
 cod_pais2             cod_pais2        Codigo alternativo     STR       1 nivel
                                              pais
 
 desc_pais             desc_pais         Nombre pais           STR       1 nivel
 
 cod_continente     cod_continente      codigo continente      STR       1 nivel

 desc_continente    desc_continente     nombre continente      STR       1 nivel   

 latitute             Latitud            Grados decimales      FLOAT     6 decimales
                                         (negativo es sur, 
                                          positivo es        norte)                                                                                                      
                                                                                                                              
 longitude            Longitud            Grados decimales     FLOAT     6 decimales
                                         (negativo es 
                                         	oeste, 
                                          positivo es 
                                           este)                                              
                                                             
-------------------------------------------------------------------------------------


## Analisis funcional

A continuacion se van a especificar los requisitos funcionales solicitados en la contruccion de este DWHU.

-----------------------------------------------------------------------------------------------------------------------
 Numero   Requerimiento                                                                  Prioridad       Exigible
-------- ------------------------------------------------------------------------------ ----------- -------------------
   1      Se cargara la informacion proporcionada en el sistema, cuidando de solo            1             SI
           cargar aquellos datos relevantes
   
   2      Se creara un DWHU para satisfacer las necesidades de todos los agentes             1             SI
                especificados

   3       Se creara un modelo OLAP para la consulta de la informacion                       2             SI
              multidimensional

   4       Se crearan vistas OLAP realizando varios analisis requeridos                      3             NO 

-----------------------------------------------------------------------------------------------------------------------


## Diseño del modelo conceptual, lógico y físico

Realizado el analisis de los datos y de los requerimientos pasamos a analizar que como se va a construir el DWHU unificado, que tablas, dimensiones, atributos, etc.

### Diseño conceptual

Analizando la informacion de la que disponemos encontramos dos tablas de hechos con varias dimensiones cada una que se especificaran a continuacion.

------------------------------------------------------------------------------------------------------------
  Tabla de hecho                                   Descripcion                                                                 
----------------------------- ------------------------------------------------------------------------------ 
 `h_KPI_socio_economico`          Incluye resultados socio economicos para un LUGAR, TIEMPO y un INDICADOR
              
 `h_actividad_aeroportuaria`     Incluye la operativa de las aerolineas en el desarrollo de su actividad
------------------------------------------------------------------------------------------------------------

En la primera tabla encontramos tres dimensiones

- LUGAR: con dos niveles `d_l_pais` y `d_l_continente`. 
- TIEMPO: con un nivel `d_t_anho`. Esta dimension podria ampliarse a `d_t_decada`
- INDICADOR: con un nivel `d_i_indicador`. 

y una metrica:

- VALOR: con el valor numerico del INDICADOR para ese LUGAR y TIEMPO.

En la segunda tablas encontramos las dimensiones

- AEROLINEA: con un nivel `d_a_aerolinea`
- LUGAR: con cuatro niveles `d_l_aeropuerto`, `d_l_ciudad`, `d_l_pais` y `d_l_continente`.
- EQUIPAMIENTO: con un nivel `d_e_equipamiento`

El hecho seria la ruta existente interseccion de las dimensiones anteriores, con atributos:

- PARADAS
- COMPARTIDO

### Diseño fisico

A continuacion vamos a implementar el disenho conceptual anterior en Oracle.

Primero comenzamos con las tablas de dimensiones:

#### d_lugar_aeropuerto

Esta tabla tiene los siguientes campos y es la dimension mas compleja que encontramos:

- id_aeropuerto: clave primaria. numero
- cod_aeropuerto: cod aeropuerto. varchar(3)
- cod_aeropuerto2: cod aeropuerto. varchar(4)
- cod_ciudad: cod ciudad. varchar(22)
- desc_ciudad: desc ciudad. varchar2(22)
- id_pais: codigo pais. varchar2(22)
- desc_pais: desc pais. varchar2(22)
- id_continente. codigo pais. varchar2(22)
- desc_continente. desc continente. varchar2(22)
- latitud: numero
- longitud: numero
- altitud: numero
- zona horaria: varchar(22)


#### d_lugar_pais

Esta tabla tiene los siguientes campos y es la dimension mas compleja que encontramos:

- id_pais: clave primaria pais. varchar2(22)
- desc_pais: desc pais. varchar2(22)
- id_continente. codigo pais. varchar2(22)
- desc_continente. desc continente. varchar2(22)
- latitud_pais: numero
- longitud_pais: numero

#### d_tiempo

Esta tabla tiene los siguientes campos:

- year: clave primaria. number
- decada: number

#### d_indicador

Esta tabla tiene los siguientes campos:

- id_indicador: clave primaria. number
- cod_indicador: codigo indicador. varchar(22)
- desc_indicador: desc indicador. varchar(50)

#### d_aerolinea

Esta tabla tiene los siguientes campos:

- id_aerolinea: clave primaria. number
- cod_aerolinea: codigo aerolinea. varchar(2)
- cod_aerolinea: codigo aerolinea 2. varchar(3)
- desc_aerolinea: desc aerolinea. varchar(50)
- id_pais. clave foranea. number

#### d_equipamiento

Esta tabla tiene los siguientes campos

- id_equipamiento. clave primaria. number
- cod_equipamiento. varchar(22)
- desc_equipamiento. varchar2(255)

--------

Finalmente las tablas de hechos:

#### h_KPI_socio_economico

Contiene los campos:

- year
- id_pais
- id_indicador
- value


#### h_actividad_aeroportuaria

Contiene los campos

- id_aerolinea
- id_aeropuerto1
- id_aeropuerto2
- equipamiento
- paradas
- compartida





















