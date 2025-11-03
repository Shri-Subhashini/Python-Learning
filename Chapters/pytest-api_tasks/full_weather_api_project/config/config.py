import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://api.openweathermap.org/data/2.5/weather")
API_KEY = os.getenv("API_KEY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "London")
