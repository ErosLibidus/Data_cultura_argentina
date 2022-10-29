# Data_cultura_argentina


Este repo carga los datos de la página web http://datos.cultura.gob.ar y extrae los csv correspondientes. Además, crea una carpeta para cada espacio cultural con la fecha donde se cargó. Después lo sube a una base de datos postgreSQL local. El archivo .sh crea la base de datos "cultura". Para que todo funcione solo se tiene que ejecutar el archivo main.py como administrador.

Aclaración: PostgreSQL tiene que estar configurado con un usuario que se llame "postgres" y la contraseña que sea "admin".
