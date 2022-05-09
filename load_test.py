import requests, time, logging, time

from concurrent import futures
from random     import randint
from configuration import rps, max_workers, url

logging.basicConfig(filename='posting.log', level = logging.DEBUG)

def post_record(url, rps, max_workers):
    record = {
    'heartbeat' : randint(50, 110),
    'bloodpressure' : randint(70, 150),
    'bodytemperature' : (randint(340, 400)/10),
    'oxygensaturation' : randint(85, 100)
    }
    time.sleep(max(max_workers/rps - 0.1, 0.01))
    start = time.perf_counter()
    res = requests.post(url, json = record)
    if not res.status_code==200:
        logging.error(f'post_fail:{record}, code:{res.status_code}')
        pass
    finish = time.perf_counter()
    logging.info(f'post_success:{record}, {finish - start }')
 
# def cool_down():
#     time.sleep(period)

#if __name__ == '__main__':
    
while True:    
    start = time.perf_counter()

    with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        #executor.submit(cool_down) 
        executor.map(post_record, [url]*max_workers, [rps] * max_workers, [max_workers] * max_workers)

    finish = time.perf_counter()

    #print(f'Finished in {round(finish-start, 2)} second(s)')
    
    logging.debug(f'start= {start} ,finish= {finish}')

    #print ('start=', start ,'finish=', finish)
              
# if __name__ == '__main__':
    
#     while True:    
#         start = time.perf_counter()

#         with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
#             executor.map(post_record, [url]*5)

#         finish = time.perf_counter()

#         print(f'Finished in {round(finish-start, 2)} second(s)')

#         print ('start=', start ,'finish=', finish)