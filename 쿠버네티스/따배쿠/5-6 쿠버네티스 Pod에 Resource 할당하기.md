### 만약 Resource 제한을 걸지 않으면?
> Pod가 cpu와 memory를 전부 다 사용할 수 있다.
>
> 디도스 공격을 받아서 Pod에 cpu와 memory가 가득차버리면 다른 Pod가 작동하지 않을 수 있다.

### 그래서 어떻게?
> Pod한태 limit 제한을 해줘야 한다.
>
> 또는 Schedule에서 요청을 보낼 때 cpu와 memory 설정을 할 수 있다.

### limits 와 request의 차이
> limit는 사용의 최대 리소스 양을 제한
>
> request는 최소한의 리소스 양을 설정

### limits 가 초과될때?
> 초과된 파드는 종료되고 다시 스케줄링 된다.

### 설정방법 

```yaml
 apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx:latest
    resources:
      requests:
        memory: 64Mi
        cpu: 250m
      limits:
        memory: 128Mi
        cpu: 500m
```

### 쿠버네티스 CPU 단위
> 1core = 1000m
> 0.2core = 200m  

### 쿠버네티스에서 RAM 단위
> 1MB = 1000KB
>
> 1Mi = 1024 Ki

### 출처 
> https://youtu.be/lxCtyWPsb-0?feature=shared
