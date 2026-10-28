import requests, json
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
        "boxoffice/searchDailyBoxOfficeList.json")

def get_movie_audience(date:str, movie_name:str):
    try:
        data = requests.get(BASE_URL, 
                            params={"key" : API_KEY, "targetDt": date}, 
                            timeout=10).json()
    except:
        print("[E0] 네트워크 API 요청에 실패하였습니다.")
    
    try:
        data = data['boxOfficeResult']['dailyBoxOfficeList']
    except KeyError:
        print("[E1] API에서 받은 결과를 파싱할 수 없습니다.\n없는 값 : ['boxOfficeResult']['dailyBoxOfficeList2']")
        return None
    
    try:
        for i in data:
            if i['movieNm'] == movie_name:
                return f"{int(i['audiCnt']):,}명"
        return f"'{movie_name}' 은(는) {date} 순위에 없습니다."
    except:
        print("[E2] 영화 비교 중 문제가 발생하였습니다.")

def get_boxoffice_rank_1(date):
    params = {"key" : API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data['boxOfficeResult']['dailyBoxOfficeList']
    return movies[0]['movieNm']

