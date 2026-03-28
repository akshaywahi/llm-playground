from src.engine import PayoutSentinel
import os
from dotenv import load_dotenv

# Load variables from .env into os.environ BEFORE any other code runs
load_dotenv()

# Validate the key was actually loaded
if not os.getenv("GOOGLE_API_KEY"):
    raise EnvironmentError("GOOGLE_API_KEY not found. Check your .env file.")

def run_demo():
    sentinel = PayoutSentinel()
    event = {"event_id": "EVT-9982", "error": "Invalid BIC BANKUS33", "country": "India"}
    
    print("--- Starting Sentinel Analysis ---")
    result = sentinel.analyze(event)
    print(result["result"])

if __name__ == "__main__":
    run_demo()
