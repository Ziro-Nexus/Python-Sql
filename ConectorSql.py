import json
import mysql.connector
import pandas as pd

class SqlConnector:
    config = {}
    conector = None

    def __init__(self):
        with open("server-config.json", "r") as f:
            json_config = json.loads(f.read())
            self.config["host"] = json_config["host"]
            self.config["user"] = json_config["user"]
            self.config["password"] = json_config["password"]
            self.config["database"] = json_config["database"]


    def IniciarConexion(self):
        # la conexión inicial puede fallar
        try:
            self.conector = mysql.connector.connect(**self.config)
            print("La conexión se ha establecido satisfactoriamente")
        except:
            raise Exception("Conexión fallida con la base de datos")
    

    def ExportarCsv(self):
        p = pd.read_sql("SELECT * FROM clientes_potenciales;", con=self.conector)
        database_name = self.config["database"]
        p.to_csv(f"{database_name}.csv")



    def ExportarSql(self):
        cursor = self.conector.cursor()
        database_name = self.config["database"]
        try:
            cursor.execute("SELECT * FROM clientes_potenciales;")
            with open(f"{database_name}.sql", "w") as f:
                for line in cursor:
                    f.write(str(line) + "\n")
        except:
            print("No se pudo exportar a formato SQL")
        
        

    def ActualizarDatos(self, campo, valor, condicional):
        cursor = self.conector.cursor()
        try:
            cursor.execute(f"UPDATE clientes_potenciales SET {campo} = {valor} WHERE {condicional};")
            self.conector.commit()
        except:
            print("Falló al actualizar dato")


    def BorrarDatos(self, condicional):
        cursor = self.conector.cursor()
        try:
            cursor.execute(f"DELETE FROM clientes_potenciales WHERE {condicional};")
            self.conector.commit()
        except:
            print("No se pudo borrar el usuario")


    def InsertarDatos(self, query):
        cursor = self.conector.cursor()
        # la inserción de datos puede fallar
        try:
            cursor.execute(query)
            self.conector.commit()
            print("Los nuevos datos se han guardado satisfactoriamente")
        except:
            print("Falló al insertar datos")


    def ObtenerConfiguracion(self):
        return self.config
    

    def CerrarConexión(self):
        if self.conector == None:
            return

        self.conector.close()
        print("La conexión se ha cerrado satisfactoriamente")
    