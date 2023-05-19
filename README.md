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
































