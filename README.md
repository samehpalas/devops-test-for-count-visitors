terraform apply --auto-approve
eks config update ..
kubectl apply -f ./k8s/


------------
Terraform for provisionning the below EKS infrastructure:

VPC 
EKS (private subnet as worker node,..)
ingress controller (nginx-alb) by helm package mgr (as mutlip files automatically)
install Monitoring tools (stack >prometheus-Grafana-Alert Manager-..)
install Cert-Manager resources CRDs ( certificate, cluster issuer,..)

--------
install kubectl, config
update kube-config :
>aws eks update-kubeconfig --name <cluster-name> --region <region>

--------

Kubectl Yaml files
------------------
namespaces first
APPs
APP-SVCs
DB
DB-SVC
EBS by (pv and provisioner) PV,provisioner manually or storageclass
PVC
..
cluster issuer and certificate resourcesto secure APPs
---------
destroy infra:
kubectl delete -f
-delete images inside ecr manually to be able to delete ecr
-terraform destro --autp-approve
when project finish:
check 3shan $$
(DNS registra+hosted zone and records,ecr,just check if there ec2,lb,asg,natgw,eip,eks)