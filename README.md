# 정규 표현식(Regular_Expression)

## 1. 정규 표현식(Regular_Expression) 정의
- 정규 표현식 혹은 정규식은 일종의 문자를 표현하는 공식으로, 특정 규칙이 있는 문자열 집합을 추출할 때 자주 사용되는 형식 언어입니다.
- 주로 Programming Language나 Text Editor등에서 문자열의 검색과 치환을 위한 용도로 사용하고 있습니다.

## 2. 정규 표현식의 필요성
- 정규 표현식을 사용하면 훨씬 간편하고 직관적인 코드를 작성할 수 있습니다.

다음 코드는 주민등록번호 뒷자리를 * 문자로 변경하는 코드입니다.
```python
data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"): 
  # 1. 전체 텍스트를 공백 문자로 나눈다.
    word_result = []
    for word in line.split(" "): 
    # 2. 나뉜 단어가 주민등록번호 형식인지 조사한다.
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"  
            # 3. 단어가 주민등록번호 형식이라면 뒷자리를 *로 변환한다.
        word_result.append(word)
    result.append(" ".join(word_result)) 
    # 4. 나뉜 단어를 다시 조립한다.
print("\n".join(result))
```

다음은 정규 표현식을 사용한 코드입니다.
```python
import re 

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
```
코드가 상당히 간결해진다는 것을 알수 있습니다. 만약 찾으려는 문자열 또는 바꾸어야 할 문자열의 규칙이 매우 복잡하다면 정규식의 효용은 더 커지게 됩니다.

출처 - (https://wikidocs.net/1642)


## 3. 파이썬에서의 정규 표현식 기본 사용법

- Python에서는 `re` 모듈을 통해 정규표현식을 사용합니다.
- `re.compile()`명령을 통해 정규표현식을 컴파일하여 변수에 저장한 후 사용합니다.
```python
import re
변수이름 = re.compile('정규표현식')
```

### 메타문자 (Meta characters)
: 문자를 설명하기 위한 문자로, 문자의 구성을 설명하기 위해 원래의 의미가 아닌 다른 의미로 쓰이는 문자를 말합니다.

1. `[]`
- 문자 클래스로, `[]`는 "대괄호 안에 포함된 문자들 중 하나와 매치"를 뜻합니다.
```python
[abc] # abc중 하나와 매치
```

1-2) `[]안 하이픈(-)`
- `하이픈(-)`은 두 문자 사이의 범위(from - to)를 의미합니다.
```python
[a-c] # [abc]와 같음
[0-5] # [012345]와 같음
[0-9] # 숫자
```

1-3) `[]안 캐럿(^)`
- `캐럿(^)`은 반대를 의미 합니다.
```python
[^0-9] # 숫자를 제외한 문자만 매치
[^abc] # a, b, c를 제외한 모든 문자와 매치
```

***자주 사용하는 문자 클래스***

:[0-9] 또는 [a-zA-Z] 등은 무척 자주 사용하는 정규 표현식입니다. 이렇게 자주 사용하는 정규식은 별도의 표기법으로 표현할 수 있습니다.
- \d - 숫자와 매치, [0-9]와 동일한 표현식
- \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식
- \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식. 맨 앞의 빈 칸은 공백문자(space)를 의미
- \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식
- \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식
- \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식


2. `Dot(.)`
- `.`은 줄바꿈 문자인 `\n`을 제외한 모든 문자와 매치됩니다.
```python
a.b # 'a + 모든 문자 + b'를 뜻함
aab # a와 b 사이의 a는 모든 문자에 포함되므로 매치
a0b # a와 b 사이의 0은 모든 문자에 포함되므로 매치
abc # a와 b 사이에 문자가 없기 때문에 매치되지 않음
```


3. `*`
- `*` 앞에 오는 문자가 0개를 포함하여 몇 개가 오든 모두 매치됩니다.
```python
lo*l

ll # 매치
lol # 매치
looool # 매치
looooooooooooooooooooool # 매치
lbl # 매치 안됨
loooooooooooobooooooool # 매치 안됨
```


4. `+`
- `+` 앞에 있는 문자가 최소 한 번 이상 반복되어야 매치됩니다.
```python
lo+l

ll # 매치 안됨
lol # 매치
looooool # 매치
```

5. `?`
- `?` 앞에 있는 문자가 없거나 하나 있을 때 매치됩니다.
```python
lo?l

ll # 매치
lol # 매치
lool # 매치 안됨
```

6. `{m, n}`
- `{m, n}` 앞에 있는 문자가 m 번에서 n번까지 반복될 때 매치됩니다.
```python
lo{3, 5}l

 ll # 매치 안됨
 lol # 매치 안됨
 loool # 매치
 loooool # 매치
 looooool # 매치 안됨
```

7. `|`
- 여러 개의 정규표현식들을 `|`로 구분하면 `or`의 의미가 적용되어 정규표현식들 중 어느 하나와 매치됩니다.
```python
a|b|c # hello or hi or bye

a # 매치
b # 매치
c # 매치
a b # 매치
a b c # 매치
d # 매치 안됨
```

8. `^`
- 문자열이 `^`의 뒤에 있는 문자로 시작되면 매치됩니다. 여러 줄의 문자열일 경우 첫 줄만 적용됩니다.
```python
^a

a # 매치
aaa # 매치
baaa # 매치 안됨
1aaa # 매치 안됨
```

9. `$`
- 문자열이 `$`의 앞에 있는 문자로 끝나면 매치됩니다. 여러 줄의 문자열일 경우 마지막 줄만 적용됩니다.
```python
a$

a # 매치
aa # 매치
baa # 매치
aabb # 매치안됨
```

10. `\`
- 특수 문자를 이스케이프 하거나, 특수한 의미를 가진 문자와 매칭됩니다.
```python
import re

pattern ='$15'
string = 'Hello $10'

match = re.search(pattern,  string)
if match:
  print("성공") # '\'가 '$'를 단순 문자로 만들어 성공
else:
  print("실패") # '\'가 없다면 실패
```


11. `()`
- 정규표현식을 `()` 안에 넣으면 그 부분만 그룹화됩니다. `groups` 메서드를 통해 그룹들을 튜플 형태로 리턴 할 수 있습니다.

```python
p = re.search('(hello)(world)', 'helloworld') # 정규표현식 hello와 world의 매치 결과를 각각 그룹화

p.group() # 인자를 넣지 않으면 전체 매치 결과 리턴
helloworld

p.group(0) # group()와 같다
helloworld

p.group(1) # 1번 그룹 매치 결과 리턴
hello

p.group(2) # 2번 그룹 매치 결과 리턴
world
```

### 패턴 객체의 메서드

다음과 같은 패턴을 생성합니다.
```python
import re
p = re.compile('[a-z]+')
```

1. match(): 문자열의 처음부터 정규식과 매치되는지 조사합니다.
```python
m = p.match("python")
print(m)
<re.Match object; span=(0, 6), match='python'> # "python" 문자열은 [a-z]+ 정규식에 부합되므로 match 객체를 돌려줌

n = p.match("3 python")
print(n)
None # "3 python" 문자열은 처음에 나오는 문자 3이 정규식에 부합되지 않으므로 None 반환
```

2. search(): 문자열 전체를 검색하여 정규식과 매치되는지 조사합니다.
```python
m = p.match("python")
print(m)
<re.Match object; span=(0, 6), match='python'> # match 메서드를 수행했을 때와 동일

n = p.match("3 python")
print(n)
<re.Match object; span=(2, 8), match='python'> # 문자열 전체를 검색하기 때문에 "3 " 이후의 "python" 문자열과 매치
```

3. findall(): 정규식과 매치되는 모든 문자열을 리스트로 리턴합니다.
```python
result = p.findall("life is too short")
print(result)
['life', 'is', 'too', 'short'] # 패턴 [a-z]+과 매치되는 모든 값을 찾아 리스트로 리턴
```

4. finditer(): 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴합니다.
```python
result = p.finditer("life is too short")
for r in result: print(r)
...
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'> #findall과 동일하지만 결과로 반복 가능한 객체를 리턴
```

### match 객체의 메서드

- group(): 매치된 문자열을 리턴합니다.
- start(): 매치된 문자열의 시작 위치를 리턴합니다.
- end(): 매치된 문자열의 끝 위치를 리턴합니다.
- span(): 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴합니다.

```python
m = p.match("python")
m.group()
'python'
m.start()
0
m.end()
6
m.span()
(0, 6)
```
