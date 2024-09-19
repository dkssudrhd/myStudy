
# 프로듀서

## 토픽에 메시지 전송
### 토픽, 키, 값

```java
Properties prop = new Properties();
prop.put("bootstrap.servers", "kafka01:9092,kafka01:9092,kafka01:9092");
prop.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
prop.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

KafkaProducer<Integer, String> producer = new KafkaProducer<>(prop);

producer.send(new ProducerRecord<>("topicname", "key", "value"));
producer.send(new ProducerRecord<>("topicname", "value"));

producer.close();
```

### 프로듀서의 기본 흐름
![image](https://github.com/user-attachments/assets/ba349d8a-78d2-4109-a5bf-4ddfd1885cc7)

> 배치를 통해 메시지를 모아서 보냄

### Sender의 기본 동작
![image](https://github.com/user-attachments/assets/a13f5f0e-0f8a-444a-9621-001adca15eb8)

> - Sender는 배치에 메시지를 다 차지 않아도 보냄
> - batch.size = 배치 크기. 배치가 다 차면 바로 전송한다.
> - linger.ms = 전송 대기 시간
>     - 대기 시간을 주면 그 시간만큰 기다렸다 배치를 전송한다. 없으면 바로 전송

### 전송 결과 확인 안할 경우
```java
producer.send(new ProducerRecord<>("simple", "value");
```
- 전송 실패를 알 수 없다.
- 실패에 대한 별도 처리가 필요 없는 메시지 전송에 사용한다.

### 전송 결과 확인 할 경우

1. Future 사용 방식
```java
Future<RecordMetadata> f = producer.send(new ProducerRecord<>("topic", "value"));
try{
  RecordMetadata meta = f.get();
} catch(ExecutionException ex){
}
```

- fature의 get를 사용하면 하나의 메세지를 보내고 블러킹 된다.
- 배치에 쌓이지 않고 1개씩만 들어간다.
- 그래서 처리량이 떨어짐
- 대신 확실하게 결과를 알 수 있다.
- 처리량이 낮아도 되는 경우에만 사용한다.

2. Callback 사용 방식
```java
producer.send(new ProducerRecord<>("simple", "value),
  new Callback(){
    @Override
    public void onCompletion(RecordMetadata metadata, Exception ex){
    }
  }
}
```

- 처리량 저하를 발생시키지 않음

## 전송 보장과 ack

### ack = 0
- 서버 응답을 기다리지 않음
- 전송 보장도 zero

### ack = 1
- 파티션의 리더에 저장되면 응답 받음
- 리더 장애시 메시지 유실 가능

### ack = all(또는 -1)
- 모든 리플리카에 저장되면 응답 받음
  - 브로커 min.insysnc.replicas 설정에 따라 달라짐

## ack + min.insysnc.replicas
- min.insysnc.replicas (브로커 옵션)
  - 프로듀서 ack 옵션이 all 일 때 저장에 성공했다고 응답할 수 있는 동기화된 리플리카 최소 개수

- 예 1.
  - 리플리카 개수 3, ack = all , min.insysnc.replicas = 2
  - 리더에 저장하고
    팔로워 중 한 개에 저장하면 성공 응답

- 예 2.
  - 리플리카 개수 3, ack = all , min.insysnc.replicas = 1
  - 리더에 저장되면 성공 응답
    ack = 1 과 동일

- 예 3.
  - 리플리카 개수 3, ack = all , min.insysnc.replicas = 3
  - 리더와 팔로워 2개에 저장되면 성공 응답
  - 팔로워 중 한개라도 장애가 나면 리플리카 부족으로 저장에 실패함
    -그래서 보통 리플리카 개수와 min.insysnc.replicas 개수는 다르게 설정한다.

## 에러 유형
- 전송 과정에서 실패
  - 전송 타임 아웃
  - 리더 다운에 의한 새 리더 선출 진행 중
  - 브로커 설정 메시지 크기 한도 초과

- 전송 전에 실패
  - 직렬화 실패, 프로듀서 자체 요청 크기 제한 초과
  - 프로듀서 버퍼가 차서 기다린 시간이 최대 대기 시간 초과

### 실패 대응 1 : 재시도
- 재시도
  - 재시도 가능한 에러는 재시도 처리

- 재시도 위치
  - 프로듀서는 자체적으로 브로커 전송 과정에서 에러가 발생하면 재시도 가능한 에러에 대한 재전송 시도
    - retries 속정
  - send() 메서드에서 익셉션 발생시 익셉션 타입에 따라 send() 재호출
  - 콜백 메서드에서 익셉션 받으면 타입에 따라 send() 재호출
- 아주 아주 특별한 이유가 없다면 무한 재시도 X

### 실패 대응 2 : 기록
- 추후 처리를 위해 기록
  - 별도 파일, DB 등을 이용하여 실패한 메시지 기록
  - 추후에 수동 보정 작업 진행

- 기록위치
  - send() 메서드에서 익셉션 발생시
  - send() 메서드에 전달한 콜백에서 익셉션 받는 경우
  - send() 메서드가 리턴한 Future의 get() 메서드에서 익셉션 발생시

### 재시도와 메시지 중복 전송 가능성
- 브로커 응답이 늦게 와서 재시도할 경우 중복 발송 가능

![image](https://github.com/user-attachments/assets/8bc46b67-ce6e-4186-8ae6-10145c1e3155)

> enable.idempotence 속성을 통해 중복 가능성을 줄일 수 있음

### 재시도와 순서
- max.in.flight.requests.per.connection
  - 블로킹없이 한 커넥션에서 전송할 수 있는 최대 전송중인 요청 개수
  - 이 값이 1보다  크면 재시도 시점에 따라 메시지 순서가 바뀔 수 있음
    - 전송 순서가 중요하면 이 값을 1로 지정(그래야 순서대로 진행가능)

> 전송중이 배치에 3개가 있을 경우
>
> - 배치 1 전송 -> 실패
> - 배치 2 전송 -> 성공
> - 배치 3 전송 -> 성공
> - 배치 1 전송 재시도 -> 성공

### 출처 
> https://www.youtube.com/watch?v=geMtm17ofPY
