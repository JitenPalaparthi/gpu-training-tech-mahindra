minikube start

minikube status

minikube node add 1

kubectl api-resources

kubectl get all -A

kubectl create ns nginx-ns

kubectl delete ns nginx-ns

kubectl apply -f kubernetes-containers/kube/nginx-namespace.yaml 

kubectl get ns

kubectl apply -f kubernetes-containers/kube/nginx-pod.yaml

kubectl get pods -A

kubectl get pods -n nginx-ns

kubectl describe po nginx-pod -n nginx-ns