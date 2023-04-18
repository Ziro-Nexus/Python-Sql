from ConectorSql import SqlConnector

sql = SqlConnector()
sql.IniciarConexion()

sql.ActualizarDatos("ingreso_anual", 0, "Id = 1")

sql.CerrarConexión()
