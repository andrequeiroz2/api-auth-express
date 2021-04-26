build:
	docker build -t andrequeiroz2/api-auth-express:latest .

push:
	docker push andrequeiroz2/api-auth-express:latest

pull:
	docker pull andrequeiroz2/api-auth-express:latest

run:
	docker run -p 6010:6010 andrequeiroz2/api-auth-express:latest