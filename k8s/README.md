# Kubernetes config output

```sh
NAME                                  READY   STATUS    RESTARTS   AGE
pod/app-deployment-5b7d68f666-8glmq   1/1     Running   0          3m25s
pod/app-deployment-5b7d68f666-9klhn   1/1     Running   0          3m25s
pod/app-deployment-5b7d68f666-d6tcg   1/1     Running   0          3m25s

NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-service   LoadBalancer   10.109.163.122   localhost     5000:30809/TCP   7s
service/kubernetes    ClusterIP      10.96.0.1        <none>        443/TCP          54m
```

## Helm

After many attempts could not make Helm work.

```sh
> ./helm install python-app python-app
> Error: INSTALLATION FAILED: template: python-app/templates/serviceaccount.yaml:1:14: executing "python-app/templates/serviceaccount.yaml" at <.Values.serviceAccount.create>: nil pointer evaluating interface {}.create
```
