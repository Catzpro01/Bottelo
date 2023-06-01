import requests
import json
import time
import schedule

def ambil_data_website():
    url = "https://api.im2019.com/api/game/guess_odd?page=1&limit=50"
    headers = {
        "Host": "api.im2019.com",
        "sec-ch-ua": "\"Not;A-Brand\";v=\"99\", \"Chromium\";v=\"90\"",
        "accept": "application/json, text/plain, */*",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuaW0yMDE5LmNvbSIsImF1ZCI6ImFwaS5pbTIwMTkuY29tIiwiaWF0IjoxNjgzOTUxNjQwLCJuYmYiOjE2ODM5NTE2NDAsImV4cCI6MTY4NDU1NjQ0MCwianRpIjp7ImlkIjoxNjgyODk2LCJ0eXBlIjoidXNlciJ9fQ.06mmq-9K1c68QFH8MuigaIDleXUKW1TMR70TBxaalYs",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.im2021.com/",
        "accept-language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data['data']

def simpan_data_ke_file(data):
    with open("luwe.json", "r+") as file:
        try:
            existing_data = json.load(file)
        except json.JSONDecodeError:
            existing_data = []
        new_data = existing_data + data
        unique_data = [dict(t) for t in {tuple(d.items()) for d in new_data}]
        sorted_data = sorted(unique_data, key=lambda x: x['time'], reverse=True)
        file.seek(0)
        json.dump(sorted_data, file, indent=4)
        file.truncate()

def update_data():
    data_website = ambil_data_website()
    simpan_data_ke_file(data_website)
    print("Data berhasil diperbarui pada:", time.ctime())

# Inisialisasi data pertama kali saat menjalankan skrip
data_pertama = ambil_data_website()
simpan_data_ke_file(data_pertama)

# Jadwalkan pembaruan data setiap 1 menit
schedule.every(0.25).minutes.do(update_data)

while True:
    schedule.run_pending()
    time.sleep(1)
    print('running')
