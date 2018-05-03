import schedule
import time
import logging
from ml_task import model_update
from compute import daily_compute

FORMAT = '%(asctime)-15s %(levelname)s %(module)s %(filename)s:%(lineno)d - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='./test.log', filemode='a')

def main():

    schedule.every(1).minutes.do(model_update)
    schedule.every(1).minutes.do(daily_compute)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
