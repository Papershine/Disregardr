import sched
import requests
import scanpost
from time import time, sleep
from globalvars import *


def run_request(scheduler):
    # send HTTP GET request to StackOverflow API
    url = 'https://api.stackexchange.com/2.3/questions/no-answers'
    params = {'key': API_KEY, 'order': 'desc', 'sort': 'activity', 'site': 'stackoverflow'}
    print('Requesting URL ' + url)
    r = requests.get(url, params=params)
    data = r.json()

    # handle quota
    print('Request response ' + str(r.status_code))
    print('Quota remaining ' + str(data['quota_remaining']))

    # scan returned list of posts
    scanpost.scan(data['items'])

    scheduler.enter(900, 1, run_request, (scheduler,))


def start_service():
    request_scheduler = sched.scheduler(time, sleep)
    request_scheduler.enter(1, 1, run_request, (request_scheduler,))
    request_scheduler.run()
