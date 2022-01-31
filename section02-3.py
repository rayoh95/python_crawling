# lxml 사용 - pip install lxml ,requests, cssselect

import requests
import lxml.html


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    # 스크랩핑 대상 URL
    response = requests.get("https://www.naver.com")

    # 신문사 링크 딕셔너리 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)

    for url in urls:
        print(url)


def scrape_news_list_page(response):
    # url 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content)

    for a in root.xpath('.api_list .api_item a.api_link'):
        # 링크
        url = a.get('href')
        urls.append(url)
    
    return urls


# 스크랩핑 시작
if __name__ == "__main__":
    main()