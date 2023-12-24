# Makefile

.PHONY: build run stop clean

# Nombre de la imagen del contenedor Docker
IMAGE_NAME = my-mysql-container

# Puerto en el que se mapeará el puerto de MySQL en el contenedor
MYSQL_PORT = 3306

# Nombre del contenedor Docker en ejecución
CONTAINER_NAME = my-mysql-container

# Contraseña para el usuario root de MySQL
MYSQL_ROOT_PASSWORD = mysecretpassword

build:
    # Construir la imagen Docker
	docker build -t $(IMAGE_NAME) .

run:
    # Ejecutar el contenedor Docker con MySQL
	docker run -d -p $(MYSQL_PORT):$(MYSQL_PORT) --name $(CONTAINER_NAME) -e MYSQL_ROOT_PASSWORD=$(MYSQL_ROOT_PASSWORD) $(IMAGE_NAME)

stop:
    # Detener y eliminar el contenedor Docker
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

clean: stop
    # Eliminar la imagen Docker
	docker rmi $(IMAGE_NAME)
