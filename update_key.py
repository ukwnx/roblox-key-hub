import math
from datetime import datetime, timezone

def generate_roblox_key():
    now_utc = datetime.now(timezone.utc)
    year_seed = now_utc.year
    day_seed = now_utc.timetuple().tm_yday
    
    complex_formula = math.floor((day_seed * 84920) + (year_seed * 3.14159))
    
    seed = complex_formula & 0xFFFFFFFF
    seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
    
    low = 10000000
    high = 99999999
    generated_key = low + (seed % (high - low + 1))
    
    return str(generated_key)

if __name__ == "__main__":
    try:
        current_key = generate_roblox_key()
        with open("key1.txt", "w") as file:
            file.write(current_key)
        print(f"Successfully wrote Key 1: {current_key}")
    except Exception as e:
        print(f"Failed to write file: {e}")
