import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
    # feels_like : '체감온도',
    # humidity : '습도',
    # pressure : '기압',
    # temp : '온도',
    # temp_max : '최고온도',
    # temp_min : '최저온도',
    # description : '요약',
    # icon : '아이콘',
    # main : '핵심’
    # id : ‘식별자’

def get_result(api_key):
    lat = 37.56
    lon = 126.978

    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    # 한글 Key 매핑
    key_map = {
        'feels_like': '체감온도',
        'humidity': '습도',
        'pressure': '기압',
        'temp': '온도',
        'temp_max': '최고온도',
        'temp_min': '최저온도',
        'description': '요약',
        'icon': '아이콘',
        'main': '핵심',
        'id': '식별자'
    }

    result = {}

    # main 한글화
    main_data = {}
    for key, value in data['main'].items():
        if key in key_map:
            main_data[key_map[key]] = value

    # weather 한글화 (리스트 주의)
    weather_data = {}
    for key, value in data['weather'][0].items():
        if key in key_map:
            weather_data[key_map[key]] = value

    result['기온정보'] = main_data
    result['날씨정보'] = weather_data

    return result


# 여러분의 OpenWeatherMap API 키를 설정하세요
api_key = '2e8a4778a50cc759876022093b00683d'

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_result(api_key)
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)

