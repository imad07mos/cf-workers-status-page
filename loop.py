import requests
import time
import urllib.parse
import logging

# Setup logging
logging.basicConfig(filename='signup_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

url = "https://aadl3inscription2024.dz/AR/Inscription-AndroidiOS.php"

headers = {
    "accept-encoding": "gzip",
    "content-length": "81",
    "content-type": "application/x-www-form-urlencoded; charset=utf-8",
    "host": "aadl3inscription2024.dz",
    "user-agent": "Dart/3.4 (dart:io)"
}

# List of dictionaries with different combinations of data
data_list = [
    {
        "P1": "24",
        "P2": "100000751039610007",
        "P3": "201903047094",
        "P4": "0541405038",
        "P5": "qaLYa*wMw)4A.FxM"
    },
    {
        "P1": "28",
        "P2": "100020984005890008",
        "P3": "202303003779",
        "P4": "‏0675222848",
        "P5": "qaLYa*wMw)4A.FxM"
    },
    {
        "P1": "17",
        "P2": "109920558003790006",
        "P3": "920379001150",
        "P4": "0550279242",
        "P5": "qaLYa*wMw)4A.FxM"
    },
    {
    "P1": "17",
    "P2": "109910917008010004",
    "P3": "910801014854",
    "P4": "0542309017",
    "P5": "qaLYa*wMw)4A.FxM"
    },
    {
    "P1": "10",
    "P2": "109940568014490005",
    "P3": "941449004541",
    "P4": "0540609206",
    "P5": "qaLYa*wMw)4A.FxM"
    },
    {
    "P1": "17",
    "P2": "109850951000960009",
    "P3": "850096066036",
    "P4": "0541650855",
    "P5": "qaLYa*wMw)4A.FxM"
    },
    {
    "P1": "32",
    "P2": "109971110005420006",
    "P3": "970542005841",
    "P4": "0561122247",
    "P5": "qaLYa*wMw)4A.FxM"
    },
    {
    "P1": "10",
    "P2": "109910291004830009",
    "P3": "910483006342",
    "P4": "0772382975",
    "P5": "qaLYa*wMw)4A.FxM"
    }, 
    {
    "P1": "17",
    "P2": "109830599005540006",
    "P3": "830554014250",
    "P4": "0553173035",
    "P5": "qaLYa*wMw)4A.FxM"
    },
     {
    "P1": "36",
    "P2": "109941432000680005",
    "P3": "940068005443",
    "P4": "0559025746",
    "P5": "qaLYa*wMw)4A.FxM"
    },
    {
    "P1": "17",
    "P2": "219740947002940206",
    "P3": "700294030850",
    "P4": "0657522942",
    "P5": "qaLYa*wMw)4A.FxM"
    },
    {
    "P1": "03",
    "P2": "100030059000350007",
    "P3": "202103048600",
    "P4": "0659904611",
    "P5": "qaLYa*wMw)4A.FxM"
    },
    {
    "P1": "03",
    "P2": "100030059000350007",
    "P3": "202103048600",
    "P4": "0659904611",
    "P5": "qaLYa*wMw)4A.FxM"
    }, 
    {
    "P1": "17",
    "P2": "119900581010780102",
    "P3": "901078004742",
    "P4": "0540048718",
    "P5": "qaLYa*wMw)4A.FxM"
    },
     {
    "P1": "27",
    "P2": "109911017012140001",
    "P3": "911214009745",
    "P4": "0795928685",
    "P5": "qaLYa*wMw)4A.FxM"
    }, {
    "P1": "17",
    "P2": "509780087000010101",
    "P3": "780001078845",
    "P4": "0557341118",
    "P5": "qaLYa*wMw)4A.FxM"
    }

]

bot_token = "7006700525:AAH3U8JYEHrmu3vvpL4xAQ80H66bpm15g3s"
channel_id = "@testimdimd"

# Path to your .crt file
crt_file_path = "_.aadl3inscription2024.dz.crt"

def send_telegram_message(message):
    telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': channel_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(telegram_api_url, data=payload)
        if response.status_code == 200:
            logging.info("Telegram message sent successfully.")
        else:
            logging.error(f"Failed to send Telegram message. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Telegram request failed: {e}")

def send_request(data):
    while True:
        try:
            encoded_data = urllib.parse.urlencode(data)
            response = requests.post(url, headers=headers, data=encoded_data, verify=False, timeout=10)
            if response.status_code == 200:
                response_content = f"Headers:\n{response.headers}\n\nBody:\n{response.text}"
                filename = f"response_{data['P4']}.txt"
                with open(filename, "w") as file:
                    file.write(response_content)
                logging.info(f"Response received and recorded in {filename}.")
                print(f"Response received and recorded in {filename}.")
                send_telegram_message(f"Response received and recorded successfully for {data['P4']}.")
                return True
            else:
                logging.warning(f"Received status code {response.status_code}. Retrying...")
                print(f"Received status code {response.status_code}. Retrying...")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}. Retrying...")
        time.sleep(3)  # wait for 3 seconds before retrying

while data_list:
    for data in data_list[:]:
        if send_request(data):
            data_list.remove(data)
            logging.info(f"Successfully processed and removed data: {data}")
