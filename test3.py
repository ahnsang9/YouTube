import requests
import json
from bs4 import BeautifulSoup as bs

def web_request(method_name, url, dict_data, is_urlencoded=True):
    """Web GET or POST request를 호출 후 그 결과를 dict형으로 반환 """
    method_name = method_name.upper()  # 메소드이름을 대문자로 바꾼다
    if method_name not in ('GET', 'POST'):
        raise Exception('method_name is GET or POST plz...')

    if method_name == 'GET':  # GET방식인 경우
        response = requests.get(url=url, params=dict_data)
    elif method_name == 'POST':  # POST방식인 경우
        if is_urlencoded is True:
            response = requests.post(url=url, data=dict_data,
                                     headers={'Content-Type': 'application/x-www-form-urlencoded'})
        else:
            response = requests.post(url=url, data=json.dumps(dict_data), headers={'Content-Type': 'application/json'})

    dict_meta = {'status_code': response.status_code, 'ok': response.ok, 'encoding': response.encoding,
                 'Content-Type': response.headers['Content-Type']}
    if 'json' in str(response.headers['Content-Type']):  # JSON 형태인 경우
        return {**dict_meta, **response.json()}
    else:  # 문자열 형태인 경우
        return {**dict_meta, **{'text': response.text}}

# GET방식 호출 테스트
url  = 'https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DmKzaPWr6tQ%2540OGJOvAySTa12df4ePULTkTLSVV803qKujPy9GC0O0HaJu2kTwM6ITrx8Pi94g6tQgRs3DHXPufg%253D%253D%26encode_state%3Dtrue' # 접속할 사이트주소 또는 IP주소를 입력한다
data = {'id_email_2' : 'ahnsang9@nave.com',
        'id_password_3' : 'wpgk!'}    # 요청할 데이터

with requests.Session() as s:
    response = s.get(url=url, params=data)
    #response = web_request(method_name='GET', url=url, dict_data=data)

    dict_meta = {'status_code': response.status_code, 'ok': response.ok, 'encoding': response.encoding,
                     'Content-Type': response.headers['Content-Type']}

    if 'json' in str(response.headers['Content-Type']):  # JSON 형태인 경우
        response = {**dict_meta, **response.json()}
    else:  # 문자열 형태인 경우
        response = {**dict_meta, **{'text': response.text}}
    print(response)

    if response['ok'] == True:
        print ('성공')
        # 성공 응답 시 액션
    else:
        pass
        # 실패 응답 시 액션
    main_page = s.get('https://www.melon.com/mymusic/playlist/mymusicplaylist_list.htm?memberKey=38091076')
    soup = bs(main_page.text,'html.parser')
    print(soup.select('body'))

    if response['ok'] == True:
        print ('성공')
        # 성공 응답 시 액션
    else:
        pass


