# Demo Flask + Redis with Kubernetes

This repository contains a practice flask app which connects to a Redis database. It also contains Kubernetes config files to run the app with services like minikube. The idea behind this repo is to have a template for setting up Flask apps within a Kubernetes cluster. 

## Running with Docker Compose

This app can also be run with `docker-compose`. In order to do this the redis host in the `flask/app/views.py` and `flask/config.py` files must be changed. Presently it is set to:

`r = redis.Redis(host="redis.default.svc.cluster.local", port=6379)`

this must be changed to

`r = redis.Redis(host="redis", port=6379)`

Once this is done, run the following commands:

1. Build the Docker images with: `docker-compose -f docker-compose.yml build`
2. Start the Docker containers with: 'docker-compose -f docker-compose.yml up'

Now navigate to the localhost URL returned by your terminal to access the app. Alternatively you can visit:

`http://0.0.0.0:5000/?user=Farida`

to see the app in action. 

## Running with Kubernetes

To run a flask app connected to redis via Kubernetes locally, follow the steps below:

**Note**: This presumes you have `kubectl` cli and `minikube` installed and running.

1. Point local containter registry to the minikube local registry. In the terminal, run: 

`eval $(minikube -p minikube docker-env)`

2. In the flask app, when connecting to the redis instance, we will need to connect to the redis pod within the Kubernetes cluster. So the host name in Python must be set to

`r = redis.Redis(host="<name>.default.svc.cluster.local", port=6379)`

where `<name>` is the name given to the redus service found in the metadata section of the `kubernetes_configs/redis-service.yaml` file. For this repository the default value is set to 

`r = redis.Redis(host="redis.default.svc.cluster.local", port=6379)`

which will suffice.

3. Build a docker image from the `Dockerfile` in `flask` directory. In the terminal, run:

```
cd flask 
docker build -t <name of image> .
```

4. Make YAML deployment and service config files for the flask app and redis database. These are contained in the `kubernetes_configs` directory. 

5. Create the deployment and services via `kubectl` cli. 

6. Run minikube service: `minikube service <app service name>`

7. Interact with the app with URL returned


