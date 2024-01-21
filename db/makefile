build-db-seed:
	docker build -t db_test_image .

run-db-seed:
	docker run -p 3306:3306 --name db_test_container -d db_test_image

stop-db-seed:
	docker stop db_test_container

rm-db-seed:
	docker rm db_test_container

rmi-db-seed:
	docker rmi db_test_image

# Path: db/makefile
access-db:
	docker exec -it db_test_container mysql -u root -proot

