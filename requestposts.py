import sched
import requests
from time import time, sleep


def run_request(scheduler):
    r = requests.get()
    scheduler.enter(60, 1, run_request, (scheduler,))


request_scheduler = sched.scheduler(time, sleep)
request_scheduler.enter(60, 1, run_request, (request_scheduler,))
request_scheduler.run()
