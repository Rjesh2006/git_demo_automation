# test_nta.py

from datetime import datetime

def log_status(message: str):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[✅ SUCCESS] {message}")
    print(f"🕒 Timestamp  : {timestamp}")
    print(f"📦 Environment: Test")
    print(f"💬 Note       : Script executed flawlessly!\n")

if __name__ == "__main__":
    log_status("Test script executed — Jenkins cron is working perfectly  update eeeeeeeeeeeeeeeeeeeeee🚀")
