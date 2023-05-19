# -정규 표현식(Regular-Expression)-
## 목차

## 정규 표현식이란?
### <정의>
- 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어
- 텍스트에서 우리가 원하는 특정한 패턴을 찾을 때 요긴하게 사용
```
✏️ 어떤 문자열의 규칙을 찾아서 어떤 문자와 일치하는 것을 뭐로 바꿔라
-> 전화번호 형태의 패턴을 찾을 때 ex) 000-0000-0000
-> 웹사이트 형태의 패턴을 찾을 때 ex) http://www.~.com
-> 찾은 패턴을 다른 문자열로 변경 가능
-> 사용자가 입력한 데이터가 이메일이나 패스워드와 같은 특정패턴에 
부합하는지 유효성검사 가능
```
<br>

### <구성>
<img src="https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/4af0b4cc-c1c7-49e1-ba39-ae50f351d317" width="50%"><br>
- <b>슬래시(/)</b> : 슬래시를 이용해 '나는 정규 표현식이야!'라고 나타냄<br>
-    <b>패턴</b>   : //안에 우리가 찾고자하는 패턴 작성<br>
-    <b>flag</b>   : 어떤 옵션을 이용해서 검색할 건지 flag를 활용할 수 있음.<br>

```
✏️ 어떻게 우리가 원하는 패턴을 작성해나가는지가 중요!
```
<br>

## 정규 표현식의 필요성
- 조건문과 문자열 조작을 통해 해결할 수 있지만 그러면 코드가 너무 복잡해진다.<br> 
=> <b>정규표현식으로 해결하면 코드가 매우 간단하고 직관적이며 복잡한 문제가 주어졌을 때 큰 효용성을 보여줌.</b><br><br>

ex) 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경하시오.<br>

|여러 개의 조건을 활용해 문제 해결한 코드|정규표현식을 사용한 경우|
|------|---|
|<img src="https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/2108b89f-7d84-4b65-a1c9-471ff71ae05a" >|<img src="https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/49f6bda4-d8f4-40fe-a052-86bc8c6425d3">|

간단한 예제로 코드만 비교해보아도 정규표현식을 사용한 경우의 코드가 훨씬 간결한 것을 볼 수 있다.

```
✏️ 그 밖에 정규표현식의 사용이 필요한 경우
- 대소문자를 구별하지 않고 "car" 텍스트를 찾는데, 단어 중간에 car가 들어간 경우는 
제외할 경우(scar, carry 등)
- DB에서 뽑은 텍스트를 태그를 포함해 웹페이지에 출력하려고 할 때
- 회원가입과 같은 input 폼이 있는 웹페이지를 만들 경우 형식이 맞게 작성되었는지 
확인할 때
- 소스코드에서 단어를 조건에 맞게 치환하려고 할 때
- 특정 텍스트가 포함된 파일들을 걸러낼 때
- csv 등의 데이터를 처리할 때
- 파일의 특정 위치에서 원하는 텍스트를 찾을 때
```
<br>
 
## 파이썬에서의 기본 사용법
