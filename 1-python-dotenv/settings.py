# settings.py
from dotenv import load_dotenv, find_dotenv
from pathlib import Path  # Python 3.6+ only
import os

# 一、自动搜索 .env 文件
load_dotenv(verbose=True)

# 二、与上面方式等价
load_dotenv(find_dotenv(), verbose=True)

# 三、或者指定 .env 文件位置
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

SECRET_KEY = os.getenv("EMAIL")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

print(SECRET_KEY)
print(DATABASE_PASSWORD)
