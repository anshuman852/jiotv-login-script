import os
import requests
import time
USERNAME=os.environ.get('USERNAME')
PASSWORD=os.environ.get('PASSWORD')
URL=os.environ.get('URL')
interval_in_days=os.environ.get('INTERVAL_IN_DAYS', 3)
interval_in_days=int(interval_in_days)
while True:
    payload = {'email': USERNAME, 'pass': PASSWORD}
    r=requests.post(URL, data=payload,timeout=90)
    print(r.status_code)
    if r.status_code == 200:
        print('Success')
    else:
        print('Failed')
    time.sleep(interval_in_days * 24 * 60 * 60)