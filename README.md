# Taller Lenguajes de programación

## Librerias requeridas
- mysql-connector
- pandas

## Estructura

Para modificar los parametros del servidor SQL se debe modificar el archivo server-config.json el cual contiene:

```json
{`
    "host": "localhost",
    "user": "andres",
    "password": "",
    "database": "andres_clientes_potenciales"
}
````

Al modificar este archivo afectará todos los puntos del ejercicio.

<hr>

El taller se divide en los siguientes archivos, cada uno representando un punto del ejercicio.

- 0-insertar_datos.py
- 1-actualizar_datos.py
- 2-borrar_datos.py
- 3-exportar_sql.py
- 4-exportar_csv.py

todos estos archivos hacen uso de la clase ConectorSql la cual se encuentra en ConectorSql.py y se encarga de manejar todas
las conexiones SQL de una manera m
