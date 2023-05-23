# -정규 표현식(Regular-Expression)-
## < 목 차 >
#### 1. 정규 표현식이란?
 (1) 정의<br>
 (2) 구성
#### 2. 정규 표현식의 필요성
#### 3. 파이썬에서의 기본 사용법
 (1) 메타 문자 <br>
 (2) re Python 정규표현식 모듈<br>
 (3) 패턴 객체의 메서드<br> 
   1.match
   2.search
   3.findall
   4.finditer<br>
#### + 문법 정리
#### 4. 코드 예제
 (1) 이메일 형식 검사(match 함수 사용)  
  + 만약 위 상황에서 search 함수를 쓴다면?<br>
 (2) 당첨자 발표 페이지-특정 패턴 가진 아이디 추출(findall 함수 사용)


<br><br>

## 1. 정규 표현식이란?
### (1) 정의
- 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어
- 텍스트에서 우리가 원하는 특정한 패턴을 찾을 때 요긴하게 사용
```
✏️ 어떤 문자열의 규칙을 찾아서 어떤 문자와 일치하는 것을 뭐로 바꿔라
-> 전화번호 형태의 패턴을 찾을 때 ex) 000-0000-0000
-> 웹사이트 형태의 패턴을 찾을 때 ex) http://www.~.com
-> 찾은 패턴을 다른 문자열로 변경 가능
-> 사용자가 입력한 데이터가 이메일이나 패스워드와 같은 특정패턴에 부합하는지 유효성검사 가능
```
<br>

### (2) 구성
<img src="https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/4af0b4cc-c1c7-49e1-ba39-ae50f351d317" width="70%"><br>
- <b>슬래시(/)</b> : 슬래시를 이용해 '나는 정규 표현식이야!'라고 나타냄<br>
-    <b>패턴</b>   : //안에 우리가 찾고자하는 패턴 작성<br>
-    <b>flag</b>   : 어떤 옵션을 이용해서 검색할 건지 flag를 활용할 수 있음.<br>

```
✏️ 어떻게 우리가 원하는 패턴을 작성해나가는지가 중요!
```

<br><br>


## 2. 정규 표현식의 필요성
- 조건문과 문자열 조작을 통해 해결할 수 있지만 그러면 코드가 너무 복잡해진다.<br> 
=> <b>정규표현식으로 해결하면 코드가 매우 간단하고 직관적이며 복잡한 문제가 주어졌을 때 큰 효용성을 보여줌.</b><br><br>

ex) 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경하시오.<br>

|여러 개의 조건을 활용해 문제 해결한 코드|정규표현식을 사용한 경우|
|------|---|
|<img src="https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/2108b89f-7d84-4b65-a1c9-471ff71ae05a" >|<img src="https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/49f6bda4-d8f4-40fe-a052-86bc8c6425d3">|

간단한 예제로 코드만 비교해보아도 정규표현식을 사용한 경우의 코드가 훨씬 간결한 것을 볼 수 있다.

```
✏️ 그 밖에 정규표현식의 사용이 필요한 경우
- 대소문자를 구별하지 않고 "car" 텍스트를 찾는데, 단어 중간에 car가 들어간 경우는 제외할 경우(scar, carry 등)
- DB에서 뽑은 텍스트를 태그를 포함해 웹페이지에 출력하려고 할 때
- 회원가입과 같은 input 폼이 있는 웹페이지를 만들 경우 형식이 맞게 작성되었는지 확인할 때
- 소스코드에서 단어를 조건에 맞게 치환하려고 할 때
- 특정 텍스트가 포함된 파일들을 걸러낼 때
- csv 등의 데이터를 처리할 때
- 파일의 특정 위치에서 원하는 텍스트를 찾을 때
```

<br><br>
## 3. 파이썬에서의 기본 사용법
### (1) 메타 문자
```. ^ $ * + ? \ | ( ) { } [ ]```<br>
정규식에서 사용되는 메타 문자는 다음과 같다. 
```
✏️ 메타문자란?
문자가 가진 원래의 의미가 아닌 특별한 용도로 사용되는 문자를 말한다.
```
### [] 문자 
<b>[] 안에 포함된 문자들 중 하나와 매치</b>를 뜻한다.
```python
# abc 중 하나와 매치
[abc]
```
- 'a' : a와 매치
- 'boy' : b와 매치
- 'dye' : a,b,c 중 어느 문자와도 매치X

[] 안의 두 문자에 -를 사용하면 두 문자 사이의 범위를 뜻한다.
- [a-c] : [abc]와 같음
- [0-5] : [012345]와 같음.
- [a-zA-Z] : 모든 알파벳

- 자주 사용하는 문자 클래스<br>

| 문자 클래스 | 뜻                           |설명|
| --------- | ---------------------------- |---|
| `\d`      | digit 숫자                   |	숫자 [0-9]와 같다.|
| `\D`      | digit 숫자 아님              |	비숫자 [^0-9]와 같다.|
| `\w`      | word 문자                    |	숫자 + 문자 [a-zA-Z0-9]와 같다.|
| `\W`      | word 문자 아님               |숫자 + 문자가 아닌 것 [^a-zA-Z0-9]와 같다.|
| `\s`      | space 공백                   |공백 [ \t\n\r\f\v]와 같다.|
| `\S`      | space 공백 아님              |비공백 [^ \t\n\r\f\v]와 같다.|
| `\b`      | 단어 경계        |단어 경계 (`\w`와 `\W`의 경계)|
| `\B`      | 단어 경계가 아님 |	비단어 경계|

<br>

```
✏️ [] 안에서 ^는 반대를 뜻한다.
- [^0-9] : 숫자를 제외한 문자만 매치
- [^abc] : a,b,c를 제외한 모든 문자와 매치
```
<br>

### . 모든 문자
줄바꿈 문자인 \n을 제외한 <b>모든 문자</b>와 매치된다.
```python
# 'a + 모든 문자 + b'를 뜻함
a.b
```
- aab : a와 b 사이의 a는 모든 문자에 포함되므로 매치
- a0b : a와 b 사이의 0은 모든 문자에 포함되므로 매치
- abc : a와 b 사이에 문자가 없기 때문에 매치X

```
✏️ [] 사이에서 .을 사용할 경우 문자 원래의 의미인 마침표가 된다.
a[.]b
- a.b : a와 b 사이에 마침표가 있으므로 매치
- a0b : a와 b 사이에 마침표가 없으므로 매치X
```

<br>

### * 반복
* 앞에 오는 문자가 <b>0개를 포함하여 몇 개가 오든</b> 모두 매치된다.
```python
lo*l
```
- ll : 매치
- lol : 매치
- looool : 매치
- lbl : 매치X

<br>

### + 최소 한 번 이상 반복
+ 앞에 있는 문자가 <b>최소 한 번 이상 반복</b>되어야 매치된다.
```python
lo+l
```
- ll : 매치X
- lol : 매치
- looool : 매치

<br>

### ? 없거나 하나 있거나
? 앞에 있는 문자가 <b>없거나 하나</b> 있을 때 매치된다.
```python
lo?l
```
- ll : 매치
- lol : 매치
- looool : 매치X

<br>

### {m,n} 반복 횟수 지정
{m,n} 앞에 있는 문자가 <b>m번에서 n번까지 반복</b>될 때 매치된다.
```python
lo{3, 5}l
```
- ll : 매치X
- lol : 매치X
- lool : 매치
- 1oooool : 매치 
- looooool : 매치X
```
✏️ {m} 형태로 사용하면 m번 반복인 경우만 매치
{0,} = *
{1,} = +
{0,1} = ?
```

<br>

### | 여러 개의 표현식 중 하나
여러 개의 정규표현식들을 | 로 구분하면 <b>or 의 의미가 적용되어 정규표현식들 중 어느 하나와 매치</b>된다.
```python
a|b|c
```
- a : 매치
- b : 매치
- c : 매치
- a b : 매치
- a b c : 매치
- v : 매치X

<br>

### ^ 문자열의 제일 처음과 매치
문자열이 <b>^의 뒤에 있는 문자로 시작</b>되면 매치된다. 
여러 줄의 문자열일 경우 첫 줄만 적용된다. 
(단, re.MULTILINE 옵션이 적용되면 각 줄의 첫 문자를 검사하여 매치된다.)
```python
^a
```
- a : 매치
- aaa : 매치
- baaa : 매치X
- 1aaa : 매치X

<br>

### $ 문자열의 제일 마지막과 매치
문자열이 $의 앞에 있는 문자로 끝나면 매치된다. 
여러 줄의 문자열일 경우 마지막 줄만 적용된다. 
(단, re.MULTILINE 옵션이 적용되면 각 줄의 마지막 문자를 검사하여 매치된다.)
```python
a$
```
- a : 매치
- aaa : 매치
- baaa : 매치
- aaa1 : 매치X

<br>

### \A , \Z
\A 는 ^ 와 동일하지만 re.MULTILINE 옵션을 무시하고 항상 문자열 첫 줄의 시작 문자를 검사한다. 
\Z 는 $ 와 동일하지만 re.MULTILINE 옵션을 무시하고 항상 문자열 마지막 줄의 끝 문자를 검사한다.

<br>

<b><조건이 있는 표현식></b><br>
### 표현식1(?=표현식2)
표현식1 뒤의 문자열이 표현식2와 매치되면 표현식1 매치
```python
# hello 뒤에 world가 있으면 hello를 매치
'hello(?=world)'
```
- helloworld : hello 뒤에 world가 있기 때문에 hello가 매치
- byworld : hello가 없기 때문에 매치X
- helloJames : hello 뒤에 world가 없기 때문에 매치X

<br>

### 표현식1(?!=표현식2)
표현식1 뒤의 문자열이 표현식2와 매치되지 않으면 표현식1 매치
```python
# hello 뒤에 world가 없으면 hello를 매치
'hello(?!=world)'
```
- helloworld : hello 뒤에 world가 있기 때문에 hello가 매치X
- byworld : hello가 없기 때문에 매치X
- helloJames : hello 뒤에 world가 없기 때문에 매치

<br>

### (?<=표현식1)표현식2
표현식2 앞의 문자열이 표현식1과 매치되면 표현식2 매치
```python
# world 앞에 hello가 있으면 world를 매치
(?<=hello)world
```
- helloworld : world 앞에 hello가 있기 때문에 world가 매치
- byworld : world 앞에 hello가 없기 때문에 매치X
- helloJames : world가 없기 때문에 매치X

<br>

### (?<!=표현식1)표현식2
표현식2 앞의 문자열이 표현식1과 매치되지 않으면 표현식2 매치
```python
# world 앞에 hello가 없으면 world를 매치
(?<!hello)world
```
- helloworld : world 앞에 hello가 있기 때문에 world가 매치X
- byworld : world 앞에 hello가 없기 때문에 매치
- helloJames : world가 없기 때문에 매치X

<br>

---

<br>

### (2) re Python 정규표현식 모듈 
Python에서는 re 모듈을 통해 정규표현식을 사용한다.
```python
import re
```
re.compile() 명령을 통해 정규표현식을 컴파일하여 변수에 저장한 후 사용할 수 있다.
```python
변수이름 = re.compile('정규표현식')
```
정규표현식을 컴파일하여 변수에 할당한 후 타입을 확인해보면 \_src.SRE_Pattern 이라는 이름의 클래스 객체인 것을 볼 수 있다.<br>
<p align="center"><img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/4a8b7e2a-b6ea-4b1b-8a08-8d1c318894c7" width = "70%"></p> 

<br>

---

<br>

### (3) 패턴 객체의 메서드 
패턴 객체는 매치를 검색할 수 있는 4가지 메서드를 제공한다.
다음 정규표현식으로 각각의 메서드를 비교해보자!
```python
p = re.compile('[a-z]+')
```
#### 1. match : 시작부터 일치하는 패턴 찾기
- 문자열의 처음 시작부터 검색하여 일치하지 않는 부분이 나올 때까지 찾는다.
```
✏️ 문자열 중간에 찾을 패턴이 있어도 시작부터 패턴이 일치하지 않으면 찾지 않는다.
```
- 매치될 때는 match객체를 리턴!
- 매치되지 않을 때는 None을 리턴
- ex)<br>
match 객체를 돌려줌.<br>
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/2a2c43d1-de28-4023-9218-efb9d041e9f2" width = "70%"> <br>
2가 [a-z]+ 정규식에 부합하지 않으므로 None 리턴
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/b0b0b955-7de4-4242-a676-9712ce30cce6" width = "70%"> <br><br>

#### 2. search : 전체 문자열에서 첫 번째 매치 찾기
- 문자열 전체에서 검색하여 처음으로 매치되는 문자열을 찾는다.
```
✏️ match가 문자열의 처음부터 검색하기 때문에 중간에 패턴이 있어도 시작부터 일치하지 않으면 찾지 않는다면, search는 문자열 전체를 검색하기 때문에 시작이 일치하지 않아도 일치하는 패턴이 존재한다면 가장 처음으로 일치하는 패턴을 찾는다. 나머지 특징은 match와 동일하다~!
```
- ex)<br>
match 객체를 돌려줌.(match와 동일)<br>
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/660c0d8e-f505-4d76-9a46-1c4a307606c3" width = "70%"> <br>
match 객체를 돌려줌.(match와는 달리 시작이 일치하지 않아도 패턴을 찾음.)
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/bb6fe251-de96-4b65-b141-bb896a2dcbfe" width = "70%"> <br><br>

#### 3. findall : 모든 매치를 찾아 리스트로 반환
- 문자열 내에서 일치하는 모든 패턴을 찾아 리스트로 반환한다.
- ex)<br>
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/86f8a94b-c187-4070-a910-1e104d789386" width = "70%"> <br><br>


#### 4. finditer : 모든 매치를 찾아 반복가능 객체로 반환
 - findall과 동일하지만 결과로 반복 가능한 객체를 리턴한다. 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.
- ex)<br>
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/05fb49ea-35fc-477f-97cb-84b02d0cf97c" width = "70%"> <br><br>

<br>
 
## + 문법 정리
### Groups and ranges
| Character | 뜻                                     |
| --------- | -------------------------------------- |
| `\|`      | 또는                                   |
| `()`      | 그룹                                   |
| `[]`      | 문자셋, 괄호안의 어떤 문자든           |
| `[^]`     | 부정 문자셋, 괄호안의 어떤 문가 아닐때 |
| `(?:)`    | 찾지만 기억하지는 않음                 |


### Quantifiers

| Character   | 뜻                                  |
| ----------- | ----------------------------------- |
| `?`         | 없거나 있거나 (zero or one)         |
| `*`         | 없거나 있거나 많거나 (zero or more) |
| `+`         | 하나 또는 많이 (one or more)        |
| `{n}`       | n번 반복                            |
| `{min,}`    | 최소                                |
| `{min,max}` | 최소, 그리고 최대                   |

### Boundary-type

| Character | 뜻               |
| --------- | ---------------- |
| `\b`      | 단어 경계        |
| `\B`      | 단어 경계가 아님 |
| `^`       | 문장의 시작      |
| `$`       | 문장의 끝        |

### Character classes

| Character | 뜻                           |
| --------- | ---------------------------- |
| `\`       | 특수 문자가 아닌 문자        |
| `.`       | 어떤 글자 (줄바꿈 문자 제외) |
| `\d`      | digit 숫자                   |
| `\D`      | digit 숫자 아님              |
| `\w`      | word 문자                    |
| `\W`      | word 문자 아님               |
| `\s`      | space 공백                   |
| `\S`      | space 공백 아님              |

<br>
<br>
  
## 4. 코드 예제
  ### (1) 이메일 형식 검사(match 함수 사용) 
  이메일을 입력받아 이메일 형식을 만족하는지 검사하는 예제이다.<br>
  영문이나 숫자로 시작해 @ 뒤에 영문 그리고 . 뒤에 영문으로 끝나도록 할 것 이다.<br>
  위 조건을 정규표현식으로 표현한다면 다음과 같을 것이다.<br>
  ```
  [A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+&
  ```
  <br>
  조건에 부합하면 '적합' 부합하지 않으면 '부적합'을 출력할 것이고, 시작부터 조건을 만족하는지 확인해야 하기 때문에 match 함수를 사용할 것이다.<br><br>
  
  다음과 같이 코드를 입력하고 결과 값을 확인해보자.
```python
import re
  
email_regex = re.compile("[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+$")
email_input = input("이메일을 입력하세요 : ")

if email_regex.match(email_input):
    print("적합")
else:
    print("부적합")
```
  <br>
  <b>< '적합'인 경우 : 영문or숫자 + @ + 영문 + . + 영문의 조합인 경우></b><br> 
  - abc123@na.c<br>
  - 123abc@na.c<br>
  - 12345@ab.c<br>
  - abcde@ab.c
<br><br>
    <b>< '부적합'인 경우 ></b> <br>
  - abcd@123.a : @ 뒤에 영문이 아닌 숫자가 온 경우<br>
  - abc@a.123 : . 뒤에 숫자가 아닌 영문이 온 경우<br>
  - abc@.a : @와 .사이에 영문이 없는 경우<br>
  - !abc@a.a : 영문or숫자가 아닌 다른 문자로 시작한 경우<br>
  - abc@a.a! : 영문이 아닌 다른 문자로 끝난 경우<br>
 <br><br>
      
  ### + 만약 위 상황에서 search 함수를 쓴다면?
  search 함수는 문자열의 시작부터 검사하는 것이 아닌 문자열의 전체에서 매칭되는 부분을 찾는 것이기 때문에,<br>
   위 정규식대로 입력하면 시작 문자가 영문이나 숫자가 아니더라도(ex. !abc@ab.c) 부적합이 아닌 적합을 출력할 것이다.
     <br>
   시작부터 조건에 맞추려면 문자열의 제일 처음과 매치시키는 ^를 사용해 정규식을 다음과 같이 수정해야 한다.
  ```
  ^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+&
  ```
 <br>
     그럼 match를 사용했던 것과 동일하게 알맞은 결과가 출력된다.
  <br><br><br>
  
  ### (2) 당첨자 발표 페이지-특정 패턴 가진 아이디 추출(findall 함수 사용)
  <a href="http://m.yes24.com/Event/EventWinnerDetail?iContentNo=59080&NoticeYn=Y">yes24의 당첨자 페이지</a>에 가보면 다음과 같이 이벤트에 당첨된 사람들의 아이디 끝 3자리가 별표 처리된 채로 쭉 나오는데 그 패턴을 이용해 매치되는 모든 텍스트를 추출해볼 것이다.<br><br>
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/da670aa7-3dd9-4b89-9c1a-5ed19a3f5c7b">

<br>
먼저, BeautifulSoup을 이용해 웹 페이지를 크롤링해온다.<br><br>
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/c75af04a-e58e-4777-9f2b-2734c8932f30"><br>
그럼 위와 같이 페이지의 html 정보가 텍스트로 추출된다. 이 소스에서 아이디 텍스트의 규칙을 반영한 정규표현식을 정의해 매치되는 텍스트를 추출해 볼 것이다.<br><br>
  
문자열의 규칙을 보면 아이디는 모두 알파벳이나 숫자로 시작하여 ***(별 3개)로 끝난다.<br>
<img src = "https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/1e402784-36fd-40b5-950c-5ee65430a9a0" width = "15%">
  <br><br>
그럼 이걸 정규표현식을 이용해 표현해보면? 다음과 같을 것이다.
  ```python
  [a-zA-Z0-9] + \*{3}
  ```
  - [a-zA-Z0-9]는 알파벳 대소문자나 숫자가 최소 1개 이상 있는 문자열을 의미한다.
  - \*{3}는 문자 그대로 인식하기로 한 *이 3번 반복하는 문자열을 의미한다.

<br>

위 정규표현식과 매치되는 모든 문자열을 찾기 위해 findall 함수를 사용할 것이다.<br>
  
![image](https://github.com/khbbbbi/Regular-Expression_BIGDATA/assets/102509150/4c3053c9-0609-40d4-a1b4-5cc0055f2229)
 
<br><br>

> [ 출처 ]<br>
     유튜브 : <a href = "https://www.youtube.com/watch?v=dTDoTR0MXjU">정규표현식이란? 파이썬 정규표현식의 기초와 활용</a><br>
     유튜브 : <a href = "https://youtu.be/t3M6toIflyQ">정규표현식, 더이상 미루지 말자</a><br>
     위키독스 : <a href = "https://wikidocs.net/4308#match">점프 투 파이썬</a><br>
     Github.io : <a href = "https://nachwon.github.io/regular-expressions/">[Python 문법] 정규표현식</a><br>
     Velog : <a href = "https://velog.io/@sp1rit/Python-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D">Python 정규 표현식</a><br>
     chatgpt
