import requests
from bs4 import BeautifulSoup

login_url = 'http://www.hanbit.co.kr/member/login_proc.php'

user = ''
password = ''

# requests.session 메서드는 해당 reqeusts를 사용하는 동안 cookie를 header에 유지하도록 하여
# 세션이 필요한 HTTP 요청에 사용됩니다.
session = requests.session()

params = dict()
params['m_id'] = user
params['m_passwd'] = password

# javascrit(jQuery) 코드를 분석해보니, 결국 login_proc.php 를 m_id 와 m_passwd 값과 함께
# POST로 호출하기 때문에 다음과 같이 requests.session.post() 메서드를 활용하였습니다.
# 실제코드: <form name="frm"  id="frm"  action="#" method="post">
res = session.post(login_url, data = params)

# 응답코드가 200 즉, OK가 아닌 경우 에러를 발생시키는 메서드입니다.
res.raise_for_status()

# 'Set-Cookie'로 PHPSESSID 라는 세션 ID 값이 넘어옴을 알 수 있다.
# print(res.headers)

# cookie로 세션을 로그인 상태를 관리하는 상태를 확인해보기 위한 코드입니다.
# print(session.cookies.get_dict())

# 여기서부터는 로그인이 된 세션이 유지됩니다. session 에 header에는 Cookie에 PHPSESSID가 들어갑니다.
mypage_url = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'
res = session.get(mypage_url)

# 응답코드가 200 즉, OK가 아닌 경우 에러를 발생시키는 메서드입니다.
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

# Chrome 개발자 도구에서 CSS SELECTOR를 통해 간단히 가져온 CSS SELECTOR 표현식을 사용
he_coin = soup.select_one('#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span')

# 다음과 같이 class를 .mileage_section2 로 그리고 그 하부 태그중에 span이 있다는 식으로 표현도 가능함
# he_coin = soup.select_one('.mileage_section2 span')

print ('mileage is', he_coin.get_text())