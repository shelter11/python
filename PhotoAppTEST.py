import logging
import requests
from threading import Thread


MAX_THREAD = 50
URL = 'http://server/webapp'
LOGIN_URL = 'http://server/auth/login'
logging.basicConfig(filename="responses.log", format='%(asctime)s - %(message)s', level=logging.INFO)


def writelog(line):
    logging.info(line)
    print(line)


def prescript(n, nn):
    global URL
    try:
        # for one per request
        session = requests.session()

        login_data = {'UserName': 'user',
                      'Password': 'password'}
        session.post(LOGIN_URL, data=login_data)

        req = session.get(URL)
        # print req.content
        print "working!"

        writelog(str(n) + " : " + str(req.content))

    except Exception as e:
        writelog(str(n) + " : " + str(e))


def start():
    global MAX_THREAD
    arr_thread = []

    for i in range(1, MAX_THREAD):
        arr_thread.append(Thread(target=prescript, args=(i, i)))

    for i in range(1, MAX_THREAD):
        arr_thread[i-1].start()

        # if line below commented then requests perform simultaneously, else one by one
        # arr_thread[i-1].join()


writelog('BEGIN')
start()
writelog('END')
