from ConectorSql import SqlConnector

sql = SqlConnector()
sql.IniciarConexion()

sql.BorrarDatos("Id = 2")

sql.CerrarConexión()
