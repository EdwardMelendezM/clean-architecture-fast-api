build-db-seed:
	docker build -t db_test_image .

run-network:
	docker network create mynetwork

run-db-seed:
	docker run --network=mynetwork --name db_test_container -e MYSQL_ROOT_PASSWORD=root -d db_test_image

run-app:
	docker run --network=mynetwork -p 8000:8000 --name my-app-container -d nombre-de-tu-imagen

stop-db-seed:
	docker stop db_test_container

stop-app:
	docker stop my-app-container

rm-db-seed:
	docker rm db_test_container

rm-app:
	docker rm my-app-container

rmi-db-seed:
	docker rmi db_test_image

# Path: db/makefile
access-db:
	docker exec -it db_test_container mysql -u root -proot
