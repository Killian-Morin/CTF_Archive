NAME = environment

all : build run connect

run:
	docker-compose -p ${NAME} up -d

build:
	docker-compose -p ${NAME} build

connect:
	docker exec -it ${NAME} /bin/bash

down:
	docker-compose -p ${NAME} down

clean: down
	docker system prune -af

fclean: clean

.PHONY: all run build connect down clean fclean