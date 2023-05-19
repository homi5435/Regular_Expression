import re

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

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


pattern ='\$15'
string = 'Hello $15'

match = re.search(pattern,  string)
if match:
    print("성공") # '\'가 '$'를 단순 문자로 만들어 성공
else:
    print("실패") # '\'가 없다면 실패

p = re.compile('[a-z]+')

m = p.match("python")
print(m)

n = p.match("3 python")
print(n)

m = p.search("python")
print(m)

n = p.search("3 python")
print(n)

result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
for r in result: print(r)

m.group()

m.start()

m.end()

m.span()