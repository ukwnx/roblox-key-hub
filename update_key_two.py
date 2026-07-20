import math
from datetime import datetime, timezone

def generate_roblox_key_two():
    now_utc = datetime.now(timezone.utc)
    seed = (now_utc.year * 543) + (now_utc.month * 127) + (now_utc.day * 812)
    raw_key = (seed * 16807) % 2147483647
    today_key = math.floor(raw_key)
    
    return str(today_key)

if __name__ == "__main__":
    try:
        current_key = generate_roblox_key_two()
        with open("key2.txt", "w") as file:
            file.write(current_key)
        print(f"Successfully wrote Key 2: {current_key}")
    except Exception as e:
        print(f"Failed to write file: {e}")
