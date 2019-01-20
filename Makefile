default:
	docker build -t iliketrains .
	docker run -p 4000:80 iliketrains
TOSTOP := $(shell docker ps -q --filter ancestor=iliketrains)
stop:
	docker stop $(TOSTOP)

TOLOG := $(shell docker ps -q --filter ancestor=iliketrains)
logs:
	docker logs $(TOLOG)


docker-push:
	docker push anshulaggarwal/iliketrains:latest

clean:
	rm ./iliketrains
