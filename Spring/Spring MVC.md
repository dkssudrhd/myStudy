## Servlet이란?
> 자바를 사용하여 웹페이지를 동적으로 생성하는 서버측 프로그램
> 자바 클래스의 일종
> Spring MVC 내부에서는 서블릿 기반으로 웹 애플리케이션이 작동하며, 스피링 부트는 아파치 톰캣이 내장됨


## MVC란
> Model, View, Controller이며 애플리케이션을 개발할 때 사용하는 디자인 패턴
> MVC로 나누어 각 역할에 맞게 코드를 작성하는 개발 방식

### Model 
> 클라이언트의 요청을 전달받으면 요청 사항을 처리하기 위한 작업을 진행
> 클라이언트에게 응답으로 돌려주는 작업의 처리 결과 데이터를 의미

### View
> 웹 브라우저와 같이 화면에 보이는 리소스를 제공하는 역할

### Controller
> 클라이언트 측의 요청을 직접적으로 전달받는 엔드포이트로써 Model과 View의 중간에서 상호작용을 해주는 역할

## Spring MVC 구조
![spring mvc 구조](https://velog.velcdn.com/images/dkssudrhd/post/c2e33ba3-2be0-46f5-9bb9-cb060579d586/image.png)

### DispatcherServlet
> HTTP 프로토콜로 들어오는 모든 요청을 가장 먼저 받아 적합한 컨트롤러에게 위임해주는 프론트 컨트롤러

#### 처리 순서 
> 클라이언트 요청 -> 서블릿 컨테이너 -> 디스패처 서블릿 -> 해당 컨트롤러

### HandlerMapping
> 클라이언트 요청 URL을 어떤 컨트롤러가 처리할 지 결정하는 기능

### Controller
> Controller 는 클라이언트의 요청을 처리한 뒤, 결과를 리턴 응답 결과를 Model에 담아 전달한다.
HandlerAdpater에 의해 ModelAndView로 변환된다.

### ModelAndView
> Controller 에서 처리한 결과 정보 및 View 선택에 필요한 정보를 가짐

### ViewResolver
> ModelAndView를 전달 받은 DispatcherServlet은 실제 클라이언트에게 보여질 View를 렌더링하기 위해 어떤 view 객체를 사용할 지 결정하는 역할

### View
> ViewResolver에 의해 View 객체가 결정되고 해당 객체를 통해 View를 렌더링한다.

### MVC 패턴의 장단점

#### 장점
- 화면과 비즈니스 로직을 분리해서 작업이 가능함
- Model, View, Controller 영역별 개발로 확장성이 뛰어남

#### 단점
- MVC 패턴의 각 부분을 설계하고 구현하는 것이 쉽지 않음
- 다른 기술과 함께 사용하련느 경우 유연성 부족이 문제가 될 수 있음
- 구성 요소간의 의존성이 높아지기 때문에 규모가 큰 프로젝트에서는 확장성에 한계가 있을 수 있다.

### 출처 
> https://docs.spring.io/spring-framework/reference/web/webmvc.html
> https://catsbi.oopy.io/f52511f3-1455-4a01-b8b7-f10875895d5b
> https://ittrue.tistory.com/234
