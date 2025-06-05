import streamlit as st

import requests
from bs4 import BeautifulSoup

def get_calorie_from_naver(food):
    query = f"{food} 칼로리"
    url = f"https://search.naver.com/search.naver?query={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/90.0.4430.212 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # 네이버 음식 칼로리 정보가 들어있는 태그 찾아보기 (2025년 현재 기준)
    try:
        # 검색 결과에서 칼로리 수치가 들어있는 div 태그 클래스명 예시
        calorie_div = soup.find("div", class_="api_kgkg_area")  
        if calorie_div:
            calorie_text = calorie_div.get_text()
            # 예) "칼로리 100g당 52kcal"
            import re
            match = re.search(r"(\d+\.?\d*)\s?kcal", calorie_text)
            if match:
                calorie = float(match.group(1))
                return calorie
    except Exception as e:
        return None

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

