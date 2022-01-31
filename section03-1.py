# Get 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청1(encar)
url = "https://www.encar.com"

mem = urllib.request.urlopen(url)   # 수신된 정보를 저장

print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('header : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))
print('read : {}'.format(mem.read(100).decode('utf-8')))    # read() 의 인자로는 읽어올 정보의 용량(byte)를 정해준다
print('parse : {}'.format(urlparse('http://www.encar.co.kr?id=test&pw=1111')))  # url 을 의미단위로 분할

# 기본 요청2(ipify)
API = "https://api.ipify.org"

# Get 방식 Parameter
values = {
    'format' : 'json'
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param : {}'.format(params))

# 요청 URL 생성
URL = API + '?>' + params
print('요청 URL = {}'.format(URL))

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()

# 수신 데이터 디코딩
text = data.decode('UTF-8')
print('response : {}'.format(text))