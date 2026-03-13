# 1. from과 import
from conf.settings import NAME, MAIN_URL
from utils.create_url import create_url

print(create_url(NAME, MAIN_URL))

# 2. import 
import conf.settings
import utils.create_url

# conf.setting 모듈에서 NAME과 NAIN_URL 값을 참조
# 모듈명.변수명 형태로 사용
name = conf.settings.NAME
main_url = conf.settings.MAIN_URL

# 모듈명.함수명
result = utils.create_url.create_url(name, main_url)
print(result)