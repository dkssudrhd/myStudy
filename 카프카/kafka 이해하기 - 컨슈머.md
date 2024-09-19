# 컨슈머
> 토픽 파티션에서 레코드 조회하는 역할을 함


### 전형적인 컨슈머 사용 코드
```java
Properties prop = new Properties();
prop.put("bootstrap.servers", "localhost:9092");
prop.put("group.id", "group1");
prop.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
prop.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(prop);
consumer.subscribe(Collections.singleton("simple")); // 토픽 구독
while(조건문){
  ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
  for(ConsumerRecord<String, String> record : records){
    System.out.println(record.value() + ":" + record.topic() + ":" + record.partition() + ":" + record.offset());
  }
}
consumer.close();
```

## 토픽 파티션은 그룹 단위 할당
- 파티션 개수와 컨슈머 개수는 연관이 있다.

![image](https://github.com/user-attachments/assets/c47e7bd8-db5f-48b8-8ed3-a7d9d5fa1452)
> 컨슈머의 개수가 파티션의 개수 보다 많으면 노는 컨슈머가 생긴다.
>
> 컨슈머의 개수를 늘려야 한다면 파티션의 개수도 늘려야 한다.

## 커밋과 오프셋
![image](https://github.com/user-attachments/assets/0a371b1a-c5e7-4d23-bfca-992bc485e0a0)

> 이러한 과정을 계속 반복한다.

## 커밋된 오프셋이 없을 경우
- 처음 접근이거나 커밋한 오프셋이 없는 경우
- auto.offset.reset 설정 사용
   - earliest : 맨 처음 오프셋 사용
   - latest : 가장 마지막 오프셋 사용 (기본 값)
   - none : 컨슈머 그룹에 대한 이전 커밋이 없으면 익셉션(예외) 발생

## 컨슈머 설정
- 조회에 영향을 주는 주요 설정
  - fetch.min.bytes: 조회시 브로커가 전송할 최소 데이터 크기
    - 기본값 : 1
    - 이 값이 크면 대기시간은 늘지만 처리량이 증가한다.

  - fetch.max.wait.ms: 데이터가 최소 크기가 될 때까지 기다릴 시간
    - 기본값 : 500
    - 브로커가 리턴할 때까지 대기하는 시간으로 poll() 메서드의 대기 시간과 다름

  - max.partition.fetch.bytes: 파티션 당 서버가 리턴할 수 있는 최대 크기
    - 기본값 : 1MB

- 자동 커밋/수동 커밋
  - enable.auto.commit 설정
    - true: 일정 주기로 컨뮤가 읽은 오프셋을 커밋(기본값)
    - false: 수동으로 커밋 실행

  - auto.commit.interval.ms : 자동 커밋 주기
    - 기본값 : 5초

  - poll(), close() 메서드 호출시 자동 커밋 실행


### 수동 커밋 : 동기/비동기 커밋

- 동기

```java
ConsumerRecords<String, String> records = consumer.poll(Duration.ofSeconds(1));
for(ConsumerRecord<String, String> record : records){
    // 처리
}
try{
  consumer.commitSync();
} catch(Excption ex){
  // 커밋 실패시 에러 발생
}
```

- 비동기

```java
ConsumerRecords<String, String> records = consumer.poll(Duration.ofSeconds(1));
for(ConsumerRecord<String, String> record : records){
    // 처리
}
consumber.commitAsync(); // commitAsync(OffsetCommitCallback callback)
```

## 재처리와 순서
- 동일 메시지 조회 가능성
  - 일시적 커밋 실패, 리밸런스 등에 의해 발생

- 컨슈머는 멱등성(idempotence)을 고려해야 함
  - 예: 아래 메시지를 재처리 할 경우
    - 조회수 1증가 -> 좋아요 1 증가 -> 조회수 1증가
    - 단순 처리하면 조회수는 2가 아닌 4가 될 수 있다.

- 데이터 특성에 따라 타임스탬프, 일렬 번호 등을 활용해야한다.

## 세션 타임아웃, 하트비트, 최대 poll 간격

- 컨슈머는 하트비트를 전송해서 연결 유지
  - 브로커는 일정 시간 컨슈머로부터 하트비트가 없으면 컨슈머를 그룹에서 뺴고 리밸런스 징행
    - session.timeout.ms : 세션 타임 아웃 시간(기본값 10초)
    - heartbeat.interval.ms : 하트비트 전송 주기(기본 값 3초)
      - session.timeout.ms의 1/3 이하를 추천한다.

- max.poll.interval.ms : poll() 메서드의 최대 호출 간격
  - 이 시간이 지나도록 poll()하지 않으면 컨슈머를 그룹에서 빼고 리밸런스 진행

## 종료 처리
- 다른 쓰레드에서 wakeup() 메서드 호출
  - poll() 메서드가 WakeupException 발생 -> close() 메서드로 종료 처리

## 주의 할점
- KafkaConsumer는 쓰레드에 안전하지 않음
  - 여러 쓰레드에서 동시 사용하지 말 것!
  - wakeup() 메서드는 제외


### 출처
> https://www.youtube.com/watch?v=xqrIDHbGjOY
