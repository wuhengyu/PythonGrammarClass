## hello-kubernetes-demo简单实例

### Service部署

```
1.vi hello.service.yaml
2.kubectl create -f hello-service.yaml --record
3.kubectl get svc | grep hello-service
4.kubectl describe svc/hello-service
5.curl 101.210.28.58:30008/hello
6.kubectl run -i --tty busybox --image=busybox --restart=Never
7.nslookup hello-service
```

### Deployment部署

```
1.vi hello.deployment.yaml
2.kubectl create -f hello-deployment.yaml --record=true
3.kubectl get deployments
4.kubectl describe svc/hello-service
5.curl 101.210.28.58:30008/hello
    5.1.[v0.1]：hello, kubernetes!
```

### 请求的自动负载均衡

```
1.kubectl get pods | grep hello
2.kubectl logs -f hello-deloyment-855394444-wmcxj
3.curl 101.210.28.58:30008/hello
    3.1.[v0.1]：hello, kubernetes!
4.kubectl logs -f hello-deloyment-855394444-wmcxj
```

### 服务伸缩

```
1.vi hello.deployment.yaml(pods数量改为3)
2.kubectl apply -f hello.deployment.yaml
3.kubectl get pods | grep hello
4.kubectl logs -f hello-deloyment-855394444-s137d
5.curl 101.210.28.58:30008/hello
    5.1.[v0.1]：hello, kubernetes!
```

### 服务版本升级

```
1.vi hello.deployment.yaml(image改为0.2)
2.kubectl apply -f hello.deployment.yaml
3.kubectl rollout status deployment/hello.deployment(逐一替换旧版本的pod)
4.curl 101.210.28.58:30008/hello
    4.1.[v0.2]：hello, kubernetes!
5.kubectl rollout undo deployments/hello.deployment(回退上个版本)
6.curl 101.210.28.58:30008/hello
    6.1.[v0.1]：hello, kubernetes!
```
