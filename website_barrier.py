import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
website_list = ["www.facebook.com", "facebook.com"]
redirect = "127.0.0.1"

from_time = 9
to_time = 5

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_time ) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_time):
        print("working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hours")
    time.sleep(5)
