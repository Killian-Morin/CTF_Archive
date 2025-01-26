NAME = ctf_env

all : build run connect

run:
	docker compose -p ${NAME} up -d

build:
	docker compose pull
	docker compose -p ${NAME} build

connect:
	docker exec -it ${NAME} /bin/bash

down:
	docker compose -p ${NAME} down

clean: down
	docker system prune -af

.PHONY: all run build connect down clean