from ConectorSql import SqlConnector

sql = SqlConnector()
sql.IniciarConexion()

query = 'INSERT INTO clientes_potenciales(nombre, apellido, edad, ingreso_anual, puntaje_credito)\
	VALUES("Andres", "Rios", 21, 320000, 0);'

sql.InsertarDatos(query)
sql.CerrarConexión()
