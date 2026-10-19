# Todo пропаристь 2ip - https://2ip.io/ru/ и узнать ip

import  requests
class IP:
    BASE_URL ="http://ip-api.com/json/"
    def persons(self):
        ip = (input("Введите ip:"))
        poisk = f"{self.BASE_URL}{ip}"
        reserg =requests.get(poisk)
        per = reserg.json()
        country = per["country"]
        region = per["regionName"]
        timezone = per["timezone"]
        provaider = per["as"]
        user_data = {
            "country" : country,
            "region" : region,
            "timezone" : timezone,
            "provaid" : provaider
        }
        print(user_data)


ip = IP()
print(ip.persons())
