from lib.OnlineStatusChecker import OnlineStatusChecker
import os
from dotenv import load_dotenv

load_dotenv()
ACCOUNT_PATH = os.getenv('ACCOUNT_PATH')
NICKNAME = os.getenv('NICKNAME')

checker = OnlineStatusChecker(account_path=ACCOUNT_PATH, nickname=NICKNAME)
result = checker.check_online_status()
print(result)