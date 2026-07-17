from dotenv import load_dotenv
import os

load_dotenv()


def get_required_env(key: str) -> str:
    value = os.getenv(key)
    if value is None or value.strip() == "":
        raise ValueError(f"Required environment variable '{key}' is not set.")
    return value


DATABASE_URL = get_required_env("DATABASE_URL")

# Optional variables
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
APP_NAME = os.getenv("APP_NAME", "Bank API")