import os
import time
import sys
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def birthday_banner():
    # Dynamic RGB text cycle banner er jonno
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    banner = [
        "  _    _                           ____  _     _   _ ",
        " | |  | |                         |  _ \\| |   | | | |   ",
        " | |__| | __ _ _ __  _ __  _   _  | |_) | |__ | |_| |__ ",
        " |  __  |/ _` | '_ \\| '_ \\| | | | |  _ <| '_ \\| __| '_ \\",
        " | |  | | (_| | |_) | |_) | |_| | | |_) | | | | |_| | | |",
        " |_|  |_|\\__,_| .__/| .__/ \\__, | |____/|_| |_|\\__|_| |_|",
        "              | |   | |     __/ |                       ",
        "              |_|   |_|    |___/                        "
    ]
    c = random.choice(colors)
    for line in banner:
        print(f"{c}{line}")
    print('\033[0m')

def draw_cake(frame):
    # frame single ba double er upor base kore mombatir shikha (flame) flicker korbe
    flicker_1 = "🕯️" if frame % 2 == 0 else " 🔥"
    flicker_2 = " 🔥" if frame % 2 == 0 else "🕯️"
    
    cake_color = '\033[95m'    # Magenta Cake Base
    cream_color = '\033[97m'   # White Cream
    candle_color = '\033[96m'  # Cyan Candles
    reset = '\033[0m'
    
    print(f"       {candle_color} {flicker_1}   {flicker_2}   {flicker_1}   {flicker_2} {reset}")
    print(f"        {candle_color}||   ||   ||   ||{reset}")
    print(f"    {cream_color}****~~~~~~~~~~~~~~~~~~~~****{reset}")
    print(f"    {cake_color}|  {cream_color}H A P P Y   B I R T H  {cake_color}|{reset}")
    print(f"  {cream_color}******~~~~~~~~~~~~~~~~~~~~~~~~******{reset}")
    print(f"  {cake_color}|        {cream_color}D  A  Y   {user_name}        {cake_color}|{reset}")
    print(f"  {cake_color}===================================={reset}\n")

def falling_confetti(width=50, height=6):
    # Screen-er upor colorful confetti ba star pother bristi effect
    star_symbols = ['*', '+', '•', '✨', '°']
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    
    for _ in range(height):
        line = ""
        for _ in range(width):
            if random.random() < 0.1: # 10% chance density array
                line += f"{random.choice(colors)}{random.choice(star_symbols)}\033[0m"
            else:
                line += " "
        print(line)

def run_animation():
    frame = 0
    colors_pool = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    
    try:
        while True:
            clear_screen()
            
            # 1. Falling Confetti print korbe top-e
            falling_confetti()
            print("\n")
            
            # 2. Dynamic Rotating Heading
            birthday_banner()
            
            # 3. Candle Flickering Cake
            draw_cake(frame)
            
            # 4. Color Cycling Wishing Message
            current_color = colors_pool[frame % len(colors_pool)]
            next_color = colors_pool[(frame + 1) % len(colors_pool)]
            
            print(f"{current_color}  ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨")
            print(f"     Wishing you a day filled with love and cheer! ")
            print(f"  ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨{next_color}")
            
            print("\n\033[90m[ Press Ctrl+C to Stop the Celebration ]\033[0m")
            
            # Control frame sync speed
            time.sleep(0.3)
            frame += 1
            
    except KeyboardInterrupt:
        clear_screen()
        print("\033[92m✨ Program stopped gracefully. Hope RUPAM liked the celebration! 🚀✨\033[0m\n")

if __name__ == "__main__":
    user_name = "SARMISTHA" # Ekhane thik thak bracket text pass kora ache
    run_animation()