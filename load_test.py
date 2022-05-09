import requests, time, logging, time

from time       import sleep
from datetime   import datetime
from concurrent import futures
from random     import randint
from configuration import rps, max_workers, url

logging.basicConfig(filename='posting.log', level = logging.DEBUG)

start_time = datetime.now()

def post_record(url, rps, max_workers):
    record = {
    'heartbeat' : randint(50, 110),
    'bloodpressure' : randint(70, 150),
    'bodytemperature' : (randint(340, 400)/10),
    'oxygensaturation' : randint(85, 100)
    }
    # time.sleep(max(max_workers/rps - 0.1, 0.01))
    start = time.perf_counter()
    res = requests.post(url, json = record)
    if not res.status_code==200:
        logging.error(f'post_fail:{record}, code:{res.status_code}')
    else:
        finish = time.perf_counter()
        logging.info(f'post_success:{record}, {finish - start }')

#if __name__ == '__main__':
time_delta = datetime.now() - start_time 
while time_delta.total_seconds() < 9:
    time_delta = datetime.now() - start_time
    with_before = datetime.now()
    with futures.ThreadPoolExecutor(max_workers = max_workers) as executor:
        executor.map(post_record, [url] * rps, [rps] * rps, [max_workers] * rps)
    
    time_delta_with = datetime.now() - with_before
    logging.info(f'one_cycle_time : {time_delta_with.total_seconds()}')
    
    if time_delta_with.total_seconds() < 1:
        sleep(1 - (time_delta_with.total_seconds()))