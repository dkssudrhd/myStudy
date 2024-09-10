## K8s namespace
- namespace
  - 클러스터 하나를 여러 개의 논리 적인 단위로 나눠서 사용
- 쿠버네티스 클러스터 하나를 여러 팀이나 사용자가 함께 공유
- 용도에 따라 실행해야 하는 앱을 구분할 때 사용
- 물리적으로는 하나이지만 논리적으로 나눠서 사용
- 분리해서 해당 namespace만 보고싶다면 확인할 수 있다.
  - 관리에 유용함

## 네임스페이스 사용하기
- namespace 생성
  - CLI

```bash
kubectl create namespace blue
kubectl get namespaces
```

  - yaml
```bash
kubectl create namespace green --dry-run -o yaml > green-ns.yaml
vim green-ns.yaml
kubectl create -f green-ns.yaml
```
- namespace 관리
  ```bash
  kubectl get namespaces
  kubectl delete namespace
  ```

### 선택하지 않으면 Default

### namespace pods 확인
```bash
kubectl get pods -n <namespace>
```

## yaml파일에서 설정할 수도 있음

```yaml
apiVersion: v1
Kind: Pod
metadata:
  name: mypod
  namespace: orange
spec:
  containers:
  - image: nginx:1.14
    name : nginx
    ports:
    - containerPort: 80
```

### base namespace를 default가 아닌 내가 선택한 걸로 바꾸기
> config에 namespace를 저장해야 함

```bash
kubectl config set-context <config 이름> --namespace=<namespace 이름>
```

```bash
kubectl config use-context <바꿀 context>
kubectl config current-context
```

## namespace 삭제시
- namespace 안에 여러가지 API가 존재
- 그래서 namespace를 지울 때는 주의해야 한다.
- 다 날라감

## 출처
> https://youtu.be/pfkx8KDAZyk?feature=shared
