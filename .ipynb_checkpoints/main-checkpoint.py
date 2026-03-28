from src.engine import PayoutSentinel
import os

# Ensure your GOOGLE_API_KEY is set in your environment
os.environ["GOOGLE_API_KEY"] = "AIzaSyBqe_JdRc5EUcGJfa3JQV3Gv_hIDUDW0u0"

def run_demo():
    sentinel = PayoutSentinel()
    event = {"event_id": "EVT-9982", "error": "Invalid BIC BANKUS33", "country": "India"}
    
    print("--- Starting Sentinel Analysis ---")
    result = sentinel.analyze(event)
    print(result["result"])

if __name__ == "__main__":
    run_demo()
