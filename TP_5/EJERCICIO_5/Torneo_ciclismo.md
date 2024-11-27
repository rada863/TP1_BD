**Ejercicio: Torneo de ciclismo**

**Esquema de BD:**

`TORNEO<cod_torneo, nombre_torneo, cod_corredor, cod_bicicleta,
marca_bicicleta, nyap_corredor, sponsor, DNI_presidente_sponsor,
DNI_medico>`

**Restricciones:**
a. El código del torneo es único y no se repite para diferentes torneos. Pero los nombres de
torneo pueden repetirse entre diferentes torneos (por ejemplo, el “Tour de Francia” se
desarrolla todos los años y siempre lleva el mismo nombre).
b. Un corredor corre varios torneos. Tiene un código único por torneo, pero en diferentes
torneos tiene diferentes códigos.
c. Cada corredor tiene varias bicicletas asignadas para un torneo.
d. Los cod_bicicleta pueden cambiar en diferentes torneos, pero dentro de un torneo son únicos.
f.Cada bicicleta tiene una sola marca.Cada corredor tiene varios sponsors en un torneo, y un sponsor puede representar a
varios corredores.
g. Cada sponsor tiene un único presidente y un único médico.
### Paso 1: Determinar las Dependencias Funcionales (DFs)

A partir del esquema y las restricciones dadas, podemos determinar las siguientes dependencias funcionales:

1. **cod_torneo → nombre_torneo, DNI_medico**:'cod_torneo' es el identificador único para cada torneo. Todos los demás atributos ('nombre_torneo', 'DNI_medico') dependen completamente de 'cod_torneo'. Esto asegura que para cada 'cod_torneo' hay un único 'nombre_torneo' y un único 'DNI_medico'.

2. **cod_corredor → nyap_corredor**:'cod_corredor' es el identificador único para cada corredor. El nombre y apellido ('nyap_corredor') de cada corredor depende completamente de su 'cod_corredor'.


3. **cod_bicicleta → marca_bicicleta**: 'cod_bicicleta' es el identificador único para cada bicicleta. La marca de la bicicleta ('marca_bicicleta') depende completamente de su 'cod_bicicleta'.

4. **sponsor, DNI_presidente_sponsor → (Identifica unívocamente cada sponsor y su presidente)**:La combinación de sponsor y 'DNI_presidente_sponsor' es necesaria para identificar de manera única cada registro de sponsor y su presidente. Un sponsor puede tener múltiples presidentes a lo largo del tiempo o múltiples presidentes pueden estar asociados con el mismo sponsor.


### Paso 2: Determinar las Claves Candidatas

Para determinar las **claves candidatas**, necesitamos encontrar un conjunto de atributos que puedan identificar de manera única a cada fila de la tabla `Torneo`.

`cod_torneo` es un identificador único que garantiza que cada torneo tenga un código distinto. Esto asegura que no haya dos torneos con el mismo `cod_torneo`, proporcionando una identificación única para cada torneo.

En la tabla `corredor`:

`cod_corredor` es un identificador único para cada corredor. Esto garantiza que cada corredor tenga un código distinto, evitando duplicados y asegurando que se pueda identificar de manera única a cada corredor en la tabla.

En la tabla `bicicleta`:
clave Candidata:`cod_bicicleta`

- `cod_bicicleta` es un identificador único para cada bicicleta, lo que garantiza que cada bicicleta tenga un código único. Esto       asegura que no haya duplicados y que cada bicicleta se pueda identificar de manera única.
En la tabla `sponsor` 

`{sponsor, DNI_presidente_sponsor}`:La combinación de sponsor y DNI_presidente_sponsor garantiza que cada registro sea único, identificando de manera única a cada sponsor y su presidente. Esto permite gestionar los sponsors y sus representantes sin duplicados.

En la tabla `corredor_torneo`:

`{cod_torneo, cod_corredor}`: La combinación de cod_torneo y cod_corredor identifica de manera única cada participación de un corredor en un torneo. Esto asegura que no haya duplicados en las combinaciones de corredores y torneos.
En la tabla `bicicleta_torneo`:

`{cod_torneo, cod_bicicleta, cod_corredor}`:La combinación de `cod_torneo` , `cod_bicicleta` y `cod_corredor` garantiza que cada asignación de bicicleta a un corredor en un torneo sea única. Esto permite gestionar las asignaciones sin duplicados.

En la tabla `corredor_sponsor`:

`{cod_torneo, cod_corredor, sponsor}`:La combinación de `cod_torneo`, `cod_corredor` y `sponsor` garantiza que cada relación de `sponsor`con un corredor en un torneo sea única. Esto asegura que no haya duplicados en las combinaciones de `sponsor` y corredores.


Por lo tanto, la **claves candidatas** son: 
  - `cod_torneo` 
  - `cod_corredor`
  - `cod_bicicleta`
  - `{sponsor, DNI_presidente_sponsor}`
  - `{cod_torneo, cod_corredor}`
  - `{cod_torneo, cod_bicicleta, cod_corredor}`
  - `{cod_torneo, cod_corredor, sponsor}`

Esta combinación asegura que cada registro en la tabla sea único y no haya duplicados.

### Paso 3: Diseño en Tercera Forma Normal (3FN)

Para llevar el esquema a la **Tercera Forma Normal (3FN)**, necesitamos eliminar dependencias transitivas y asegurarnos de que cada atributo no clave dependa únicamente de la clave primaria completa. Esto implica dividir la tabla en varias tablas relacionadas para reducir la redundancia y asegurar la integridad de los datos.

Tabla: TORNEO

cod_torneo (Clave primaria)
nombre_torneo
cod_corredor
cod_bicicleta
marca_bicicleta
nyap_corredor

sponsor

DNI_presidente_sponsor
DNI_medico

Normalización Hasta 3FN.
Vamos a dividir la tabla original en varias tablas para asegurar que cada tabla esté en 3FN.

Nuevo Diseño en 3FN
1. Tabla Torneo
cod_torneo (Clave primaria)
nombre_torneo
DNI_medico


2. Tabla Corredor
cod_corredor (Clave primaria)
nyap_corredor


3. Tabla Bicicleta
cod_bicicleta (Clave primaria)
marca_bicicleta


4. Tabla Sponsor
sponsor (Parte de la clave primaria compuesta)
DNI_presidente_sponsor (Parte de la clave primaria compuesta)
Clave primaria compuesta: (sponsor, DNI_presidente_sponsor)

5. Tabla Corredor_Torneo
cod_torneo (Clave foránea que referencia a Torneo)
cod_corredor (Clave foránea que referencia a Corredor)
Clave primaria compuesta: (cod_torneo, cod_corredor)


6. Tabla Bicicleta_Torneo
cod_torneo (Clave foránea que referencia a Torneo)
cod_bicicleta (Clave foránea que referencia a Bicicleta)
cod_corredor (Clave foránea que referencia a Corredor)
Clave primaria compuesta: (cod_torneo, cod_bicicleta, cod_corredor)


7. Tabla Corredor_Sponsor
cod_torneo (Clave foránea que referencia a Torneo)
cod_corredor (Clave foránea que referencia a Corredor)
sponsor (Clave foránea que referencia a Sponsor)
Clave primaria compuesta: (cod_torneo, cod_corredor, sponsor)

Consultas SQL para Crear las Tablas en 3FN

sql
CREATE TABLE Torneo (
    cod_torneo INTEGER PRIMARY KEY,
    nombre_torneo TEXT,
    DNI_medico TEXT
);

CREATE TABLE Corredor (
    cod_corredor INTEGER PRIMARY KEY,
    nyap_corredor TEXT
);

CREATE TABLE Bicicleta (
    cod_bicicleta INTEGER PRIMARY KEY,
    marca_bicicleta TEXT
);

CREATE TABLE Sponsor (
    sponsor TEXT,
    DNI_presidente_sponsor TEXT,
    PRIMARY KEY (sponsor, DNI_presidente_sponsor)
);

CREATE TABLE Corredor_Torneo (
    cod_torneo INTEGER,
    cod_corredor INTEGER,
    FOREIGN KEY (cod_torneo) REFERENCES Torneo(cod_torneo),
    FOREIGN KEY (cod_corredor) REFERENCES Corredor(cod_corredor),
    PRIMARY KEY (cod_torneo, cod_corredor)
);

CREATE TABLE Bicicleta_Torneo (
    cod_torneo INTEGER,
    cod_bicicleta INTEGER,
    cod_corredor INTEGER,
    FOREIGN KEY (cod_torneo) REFERENCES Torneo(cod_torneo),
    FOREIGN KEY (cod_bicicleta) REFERENCES Bicicleta(cod_bicicleta),
    FOREIGN KEY (cod_corredor) REFERENCES Corredor(cod_corredor),
    PRIMARY KEY (cod_torneo, cod_bicicleta, cod_corredor)
);

CREATE TABLE Corredor_Sponsor (
    cod_torneo INTEGER,
    cod_corredor INTEGER,
    sponsor TEXT,
    FOREIGN KEY (cod_torneo) REFERENCES Torneo(cod_torneo),
    FOREIGN KEY (cod_corredor) REFERENCES Corredor(cod_corredor),
    FOREIGN KEY (sponsor) REFERENCES Sponsor(sponsor),
    PRIMARY KEY (cod_torneo, cod_corredor, sponsor)
);
Descripción del Esquema Normalizado

Torneo:
Guarda la información básica de cada torneo.
No contiene dependencias transitivas ni parciales.

Corredor:

Almacena la información de cada corredor.
No contiene dependencias transitivas ni parciales.

Bicicleta:

Almacena información sobre cada bicicleta.
No contiene dependencias transitivas ni parciales.

Sponsor:

Almacena información sobre los sponsors y sus presidentes.
No contiene dependencias transitivas ni parciales.

Corredor_Torneo:

Gestiona la participación de los corredores en los torneos.
La combinación de cod_torneo y cod_corredor identifica de manera única cada participación.

Bicicleta_Torneo:

Gestiona las bicicletas asignadas a los corredores en cada torneo.
La combinación de cod_torneo, cod_bicicleta y cod_corredor identifica de manera única cada asignación.

Corredor_Sponsor:

Gestiona los sponsors de cada corredor en cada torneo.
La combinación de cod_torneo, cod_corredor y sponsor identifica de manera única cada relación de patrocinio.

Este diseño normalizado en 3FN reduce la redundancia y asegura la integridad de los datos en la base de datos del campeonato de ciclismo
