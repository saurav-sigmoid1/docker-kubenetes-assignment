minikube mount ./dags/:/mnt/airflow/dags
./script-apply.sh
kubectl get pods

Execute the airflow pod
kubectl exec -it <pod> -- bash

add Fernet key
FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
export FERNET_KEY=$FERNET_KEY

initiate the data base
airflow initdb

forward the port
kubectl port-forward svc/<service>  8080:8080