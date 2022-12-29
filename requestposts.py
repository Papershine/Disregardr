import sched
import requests
import scanpost
import time
from globalvars import *


def run_request(scheduler):
    # send HTTP GET request to StackOverflow API
    url = 'https://api.stackexchange.com/2.3/questions/no-answers'
    params = {'key': API_KEY,
              'pagesize': 100,
              'todate': int(time.time() - 86400),  # 86400 sec is 24 hrs
              'order': 'desc',
              'sort': 'creation',
              'site': 'stackoverflow',
              'filter': '!FhcrK3mc6lnEuo(KA2NlM4T8zF'}
    print('[PostService] Requesting URL ' + url)
    r = requests.get(url, params=params)
    data = r.json()

    # handle response
    print('[PostService] Request response ' + str(r.status_code))
    if r.status_code != 200:
        print("[PostService][ERR] ERROR! Non 200 status code!")
        print("[PostService][ERR] Error details: " + data['error_name'] + " " + str(data['error_id']))
        print(data['error_message'])
    quota = data['quota_remaining']
    print('[PostService] Quota remaining ' + str(quota))

    # scan returned list of posts
    scanpost.scan(data['items'])  # TODO: address potential crash

    # deal with quota limit
    if quota <= 10:
        print('[PostService][WARN] !! LOW QUOTA, BACKING OFF FOR 2 HOURS !!')
        # TODO: send backoff to chat
        scheduler.enter(7200, 1, run_request, (scheduler,))
        return

    # deal with backoff
    backoff = data.get('backoff', 0)
    if backoff >= 900:
        print('[PostService][WARN] BACKOFF RECEIVED OF ' + str(backoff) + ' seconds')
        scheduler.enter(backoff, 1, run_request, (scheduler,))
        return

    # run again in 900 seconds
    scheduler.enter(900, 1, run_request, (scheduler,))


def start_service():
    request_scheduler = sched.scheduler(time.time, time.sleep)
    request_scheduler.enter(1, 1, run_request, (request_scheduler,))
    request_scheduler.run()
