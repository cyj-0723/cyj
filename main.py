import requests
from bs4 import BeautifulSoup
import re

def get_calorie_from_naver(food):
    query = f"{food} 칼로리"
    url = f"https://search.naver.com/search.naver?query={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("네이버 검색 페이지를 불러오는 데 실패했습니다.")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # 칼로리 정보가 들어있는 div 태그 찾기 (2025년 기준 구조)
    calorie_div = soup.find("div", class_="api_kgkg_area")
    if calorie_div:
        text = calorie_div.get_text()
        # "100g당 52kcal" 또는 "1회 제공량당 100kcal" 같이 추출
        match = re.search(r"(\d+\.?\d*)\s?kcal", text)
        if match:
            calorie = float(match.group(1))
            return calorie
    return None

def main():
    food = input("음식 이름을 입력하세요: ")
    weight = input("무게(g)를 입력하세요: ")

    try:
        weight = float(weight)
    except:
        print("무게는 숫자로 입력해주세요.")
        return

    calorie_per_100g = get_calorie_from_naver(food)
    if calorie_per_100g is None:
        print("칼로리 정보를 찾지 못했습니다.")
        return

    total_calorie = calorie_per_100g * (weight / 100)
    print(f"{weight}g의 {food}에는 약 {total_calorie:.2f} kcal가 포함되어 있습니다.")

if __name__ == "__main__":
    main()
