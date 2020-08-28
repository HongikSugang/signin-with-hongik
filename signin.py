import requests

def signin_with_hongik(user_id, user_pw):
    res = requests.post(
        'https://ap.hongik.ac.kr/login/LoginExec3.php',
        data={'USER_ID': user_id, 'PASSWD': user_pw}
    )
    res.raise_for_status()
    return False if res.text.find('SetCookie') == -1 else True