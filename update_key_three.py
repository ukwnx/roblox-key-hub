import math
from datetime import datetime, timezone

def generate_roblox_key_three():
    now_utc = datetime.now(timezone.utc)
    # Custom formula math variant unique to Script Three
    seed = (now_utc.year * 714) + (now_utc.month * 311) + (now_utc.day * 943)
    raw_key = (seed * 23456) + 98765432
    today_key = math.floor(raw_key)
    
    return str(today_key)

if __name__ == "__main__":
    try:
        current_key = generate_roblox_key_three()
        with open("key3.txt", "w") as file:
            file.write(current_key)
        print(f"Successfully wrote Key 3: {current_key}")
    except Exception as e:
        print(f"Failed to write file: {e}")
