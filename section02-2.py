# urlopen 함수

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["/Users/oseunghwan/Desktop/test1.jpg", "/Users/oseunghwan/Desktop/index.html"]

# 다운로드 리소스 url
target_url = ["https://search.pstatic.net/sunny/?src=http%3A%2F%2Fwww.liveen.co.kr%2Fnews%2Fphoto%2F201810%2F234116_285924_011.jpg&type=sc960_832", "http://google.com"]

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("-------------------------")

        # 상태 정보 중간 출력
        print('Header info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print("-------------------------")

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed.")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download Failed")
        print("HRL Error Reason : ", e.reason)

    # 성공
    else:
        print()
        print("Download Succed.")