import os
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
BASE_URL = os.getenv('BASE_URL', 'https://foodgram-frontend-1.foodgram.education-services.ru').rstrip('/')
API_URL = os.getenv('API_URL', 'https://foodgram-backend-1.foodgram.education-services.ru').rstrip('/')
SELENOID_URL = os.getenv('SELENOID_URL', '')
BROWSER_VERSION = os.getenv('BROWSER_VERSION', '128.0')
WAIT_TIMEOUT = 20
REQUEST_TIMEOUT = 30
