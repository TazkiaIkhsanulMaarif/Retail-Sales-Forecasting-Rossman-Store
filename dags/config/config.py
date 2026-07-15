import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, "main.env"))

RAW_TRAIN_PATH = os.path.join(BASE_DIR, "data", "raw_backup", "train_raw.csv")
RAW_STORE_PATH = os.path.join(BASE_DIR, "data", "raw_backup", "store_raw.csv")


SNOWFLAKE_CONFIG = {
    "account": os.environ.get("SNOWFLAKE_ACCOUNT"),
    "user": os.environ.get("SNOWFLAKE_USER"),
    "password": os.environ.get("SNOWFLAKE_PASSWORD"),
    "authenticator": os.environ.get("SNOWFLAKE_AUTHENTICATOR"),
    "passcode": os.environ.get("SNOWFLAKE_PASSCODE"),
    "warehouse": os.environ.get("SNOWFLAKE_WAREHOUSE"),
    "database": os.environ.get("SNOWFLAKE_DATABASE"),
    "client_request_mfa_token": True,
}

def validate_snowflake_config() -> None:
    # 1. Validasi variabel wajib seperti biasa
    missing = [key for key, value in SNOWFLAKE_CONFIG.items() if not value and key not in ["authenticator", "passcode", "client_request_mfa_token"]]
    if missing:
        raise EnvironmentError(f"Missing required Snowflake environment variable(s): {missing}. Please check your main.env file.")
    
    # 2. TAMBAHKAN KODE INI: Bersihkan nilai None agar tidak memicu eror 'NoneType' di library Snowflake
    if SNOWFLAKE_CONFIG.get("authenticator") is None:
        SNOWFLAKE_CONFIG.pop("authenticator", None)
    if SNOWFLAKE_CONFIG.get("passcode") is None:
        SNOWFLAKE_CONFIG.pop("passcode", None)
    
    # Matikan token MFA karena sudah di-bypass
    SNOWFLAKE_CONFIG["client_request_mfa_token"] = False

SCHEMA_RAW = "RAW"
SCHEMA_STAGING = "STAGING"
SCHEMA_DWH = "DWH"

TABLE_RAW_TRAIN = "RAW_TRAIN"
TABLE_RAW_STORE = "RAW_STORE"
TABLE_STG_TRAIN = "STG_TRAIN"
TABLE_STG_STORE = "STG_STORE"