## init container를 적용한 Pod
> 컨테이너를 실행하기위해 먼저 실행되어야 하는 컨테이너<br>
> init container를 담고 있는 Pod는 main container를 실행하기 위해 init container가 실행 되어야한다.

## init container
- 앱 컨테이너를 실행하기 전에 미리 동작시킬 컽네이너
- 본 Container가 실행되기 전에 사전 작업이 필요할 경우 사용
- 초기화 컨테이너가 모두 실행된 후에 앱 컨테이너를 실행
- https://kubernetes.io/ko/docs/concepts/workloads/pods/init-containers/
  - 예제를 보고 적용시키면 좋을듯

## infra container(pause) 이해하기
> 모든 Pod에 하나씩 있음<br>
> Pod의 infra를 만들어 줌

 
## 출처
> https://youtu.be/ChArV14J6Ek?feature=shared
