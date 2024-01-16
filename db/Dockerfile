# Utiliza la imagen oficial de MySQL desde Docker Hub
FROM mysql:latest

# Variables de entorno para la configuración de MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

# Copia scripts SQL personalizados, si es necesario
# COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

# Puerto en el que MySQL estará escuchando
EXPOSE 3306

# Comando para ejecutar al iniciar el contenedor
CMD ["mysqld"]
