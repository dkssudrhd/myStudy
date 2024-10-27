![](https://velog.velcdn.com/images/dkssudrhd/post/f94dcede-4d74-4a3a-990e-3ee8cc2e2e93/image.png)


## 전파 속성이란?
> 이미 트랜잭션이 진행중일 때 추가 트랜잭션 진행을 어떻게 할지 결정하는 것

## 기본 전파속성
> 기본 전파 속성은 REQUIERD를 사용한다.

## 적용법 
```java
@Transactional(propagation = Propagation.REQUIRED)
public void save(){
    
}
```



## 정리 표
| |의미|이전에 트랜잭션이 없을 때 |이전에 트랜잭션이 있을 때|
|:---:|:---:|:---:|:---:|
| REQUIERD | 트랜잭션 필요 | 트랜잭션 생성 | 이전 트랜잭션 사용
| SUPPORTS | 트랜잭션 지원 | 트랜잭션 없이 진행 | 이전 트랜잭션 사용	
| MANDATORY | 트랜잭션 의무 | 예외 처리 | 이전 트랜잭션 사용
| ERQUIERS_NEW | 트랜잭션 생성| 새로운 트랜잭션 생성 | 이전 트랜잭션을 잠시 멈추고 새로운 트랜잭션 생성
| NOT_SUPPORTED | 트랜잭션 지원하지 않음 | 트랜잭션 없이 진행 | 이전 트랜잭션을 잠시 멈추고 진행
| NEVER | 트랜잭션 사용안함 | 트랜잭션 없이 진행| 예외 처리
| NESTED | 트랜잭션 중첩| 트랜잭션 생성| 새로운 트랜잭션을 만들어 중첩
> 예외는 IllegalTransactionStateException
