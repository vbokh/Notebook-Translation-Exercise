import os
from dotenv import load_dotenv

load_dotenv()  # Looks in the ".env" file for environment variables

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")
