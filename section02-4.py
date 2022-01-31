import requests
from lxml.html import fromstring, tostring


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """
    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL
    response = session.get("https://www.naver.com")

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    for name, url in urls.items():
        print(name, url)



def scrape_news_list_page(response):
    # url 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    for a in root.xpath('//*[@id="NM_NEWSSTAND_DEFAULT_THUMB"]/div[1]/div[4]/div/div[2]/div[1]/a'):

        # a 구조 확인
        # print(a)

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

        name, url = extract_contents(a)
        #딕셔너리 삽입
        urls[name] = url
    
    return urls


def extract_contents(dom):
    # 링크 주소
    link = dom.get('href')

    # 신문사 명
    name = dom.xpath('./img')[0].get('alt') # xpath('./img') 는 리스트

    return name, link


# 스크랩핑 시작
if __name__ == "__main__":
    main()
