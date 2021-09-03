# Example setup to simulate CPU throttling in Kubernetes
This setup runs a small CPU load generator using 25 iterations of recursive fibonacci per loop.

## Pre-requisites
1. Minikube & Docker
2. kubectl
3. helm (for prometheus)

## Steps
### Deploy Prometheus using Helm Charts
1. `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
2. `helm install prometheus prometheus-community/prometheus`
3. `kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-np`
4. `minikube service prometheus-server-np`
5. You should see the Prometheus UI

### Build the docker image
1. Clone this repo
2. Set the build context to minikube
- For Windows, run `minikube -p minikube docker-env`, and copy and run the commands in the output
- For Linux / MacOS, run `eval $(minikube -p minikube docker-env)`
3. Build the image by running `docker build -t abhishek/cpu-usage .`

### Deploy the image in Minikube
1. Run `kubectl apply -f cpu-usage.yaml`
2. Confirm the container is running by checking `kubectl get pods`

### What to expect
* In the default setup (master), the CPU limits and requests are set to 250 millicores. Depending on available resources, you should be able to see each iteration take longer and behave inconsistently. This is due to excessive CPU throttling, and it can be visualized using the following query in the Prometheus UI: 
`container_cpu_cfs_throttled_seconds_total{pod=~"cpu-usage-.*", container="cpu-usage", id=~"/docker/.*"}`
* The app also logs a message to the console and can be checked using `kubectl logs -f <pod-name>`
* Once you've run this setup for a brief period of time to see the throttling in action, you can now edit the deployment to remove CPU limits and let it run as a [burstable QoS type](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/#create-a-pod-that-gets-assigned-a-qos-class-of-burstable). Run this command, and it should popup a text editor where you can live-edit the deployment's yaml file (remove limits.cpu):
`kubectl edit deployment cpu-usage`
* Although you wouldn't see throttle periods / seconds tracked anymore (because throttling is inapplicable in a burstable QoS type), you should be able to see the app's logs and determine each iteration takes far less time, and show little to no spikes in processing time.

