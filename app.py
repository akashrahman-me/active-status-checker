from dotenv import load_dotenv
from lib.TimeoutRunner import TimeoutRunner
from lib.OnlineStatusChecker import OnlineStatusChecker
from utils.notify import notify
import time
import os

load_dotenv()
ACCOUNT_PATH = os.getenv('ACCOUNT_PATH')
NICKNAME = os.getenv('NICKNAME')

def alert_timeout():
    dirname = os.path.abspath(__file__)
    dirname = os.path.dirname(dirname)
    notify( icon=f"{dirname}\\images\\timeout.png",
            title="Timeout Warning",
            message="Online status processing is timeout!" )

def checker_func():
    checker = OnlineStatusChecker(account_path=ACCOUNT_PATH, nickname=NICKNAME)
    result = checker.check_online_status()
    time.sleep(30)
    return result

if __name__ == '__main__':
    timer = TimeoutRunner()

    while True:
        status = None
        try:
            status = timer.run_with_timeout(checker_func, 60, alert_timeout)

        except Exception as err:
            print(err)
            status = None

        if status:
            time.sleep(60 * 60)
        else:
            time.sleep(60 * 5)


