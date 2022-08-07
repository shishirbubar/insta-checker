import requests, random, time
import colorama
while True:
    user = ""

    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=4):
        user = user + character

    response = requests.get(f"https://www.instagram.com/{user}/")

    if (response.status_code == 200):
        print(colorama.Fore.RED + f"NOT FOUND: {user}" + colorama.Fore.RESET)
    elif (response.status_code == 404):
        print(colorama.Fore.GREEN + f"USER FOUND: {user}" + colorama.Fore.RESET)
    else:
        print("BLOCKED FROM INSTAGRAM")
        time.sleep(120)
