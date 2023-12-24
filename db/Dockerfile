# Usa la imagen oficial de MySQL desde Docker Hub
FROM mysql:latest

# Variables de entorno para configurar la base de datos
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=db_products
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

# Puerto en el que se ejecutará MySQL dentro del contenedor
EXPOSE 3306

# Copia el script SQL personalizado al directorio de inicialización de la base de datos
COPY ./init.sql /docker-entrypoint-initdb.d/

# Comando para iniciar MySQL al arrancar el contenedor
CMD ["mysqld"]
