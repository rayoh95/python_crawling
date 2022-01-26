# urllib 사용법 . 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F213%2F2018%2F10%2F01%2F0001061799_001_20181001151141895.jpg&type=sc960_832'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = '/Users/oseunghwan/Desktop/test1.jpg'
save_path2 = '/Users/oseunghwan/Desktop/index.html'

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    # 성공
    print('Download Succeed')
