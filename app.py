from dotenv import load_dotenv
from plyer import notification
from lib.TimeoutRunner import TimeoutRunner
from lib.OnlineStatusChecker import OnlineStatusChecker
from utils.notify import notify
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
    return result

if __name__ == '__main__':
    notification.notify(
        title="Inspect the online analysis",
        message="We will send you a notification with the result within the next minute, ensuring you receive the update promptly."
    )

    timer = TimeoutRunner()
    timer.run_with_timeout(checker_func, 60, alert_timeout)


