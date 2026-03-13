import requests
from pprint import pprint

# 문제4. C번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.

import requests
from pprint import pprint

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

    # 기본 정보(main)
    main = data['main']

    basic = {
        None: main.get('sea_level'),
        '기압': main.get('pressure'),
        '습도': main.get('humidity'),
        '온도': main.get('temp'),
        '온도(섭씨)': round(main.get('temp') - 273.15, 2),
        '체감온도': main.get('feels_like'),
        '체감온도(섭씨)': round(main.get('feels_like') - 273.15, 2),
        '최고온도': main.get('temp_max'),
        '최고온도(섭씨)': round(main.get('temp_max') - 273.15, 2),
        '최저온도': main.get('temp_min'),
        '최저온도(섭씨)': round(main.get('temp_min') - 273.15, 2),
    }

    # 날씨 정보(weather)
    weather = []
    for w in data['weather']:
        weather.append({
            '식별자': w.get('id'),
            '아이콘': w.get('icon'),
            '요약': w.get('description'),
            '핵심': w.get('main')
        })

    result = {
        '기본': basic,
        '날씨': weather
    }

    return result

# 여러분의 OpenWeatherMap API 키를 설정하세요
api_key = '2e8a4778a50cc759876022093b00683d'
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_result(api_key)
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)