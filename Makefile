run: up

up: docker-compose.yml 
			docker-compose -f ./docker-compose.yml up --build -d

ssh:
	docker exec -it resume-parser bash

down: docker-compose.yml
	docker-compose down --remove-orphans
