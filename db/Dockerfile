# Utiliza la imagen oficial de MySQL desde Docker Hub
FROM mysql:latest

# Variables de entorno para la configuración de MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

# Copia el script SQL al contenedor
COPY ./sql-scripts/seed.sql /docker-entrypoint-initdb.d/

# Puerto en el que MySQL estará escuchando (no es necesario si no estás haciendo mapeo de puertos)
# EXPOSE 3306

# Comando para ejecutar al iniciar el contenedor
CMD ["mysqld"]

#Hostname: 127.0.0.1
#Port: 3306
#Username: myuser
#Password: mypassword

