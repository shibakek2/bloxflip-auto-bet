import requests
import json
import gzip
import zlib
from io import BytesIO
import brotlicffi
import time

token = ""
xtoken = ""

def fetch_balance():
    url = f"https://beta.bgaming-network.com/api/FourLuckyDiamonds/1919086/{token}"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Length": "45",
        "Content-Type": "application/json",
        "Origin": "https://beta.bgaming-network.com",
        "Priority": "u=1, i",
        "Referer": f"https://beta.bgaming-network.com/games/FourLuckyDiamonds/VRBX?play_token={token}",
        "Sec-CH-UA": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "X-CSRF-Token": xtoken
    }
    
    payload = {
        "command": "init",
        "options": {
            "balance": True
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    def handle_response(response):
        content_encoding = response.headers.get('Content-Encoding')
        try:
            if content_encoding == 'gzip':
                buf = BytesIO(response.content)
                with gzip.GzipFile(fileobj=buf) as f:
                    decompressed_data = f.read()
            elif content_encoding == 'deflate':
                decompressed_data = zlib.decompress(response.content)
            elif content_encoding == 'br':
                try:
                    decompressed_data = brotlicffi.decompress(response.content)
                except Exception:
                    decompressed_data = response.content
            else:
                decompressed_data = response.content
            try:
                data = decompressed_data.decode('utf-8')
                json_data = json.loads(data)
                balance = json_data.get('balance', 0)
                if balance < 100:
                    formatted_balance = f"0.{balance}"
                else:
                    formatted_balance = str(balance)
                
                print(f"Balance: {formatted_balance}")
            except json.JSONDecodeError:
                print("Failed to decode JSON response")
            except UnicodeDecodeError:
                print("Binary or unreadable data")
        except Exception as e:
            print(f"An error occurred: {e}")
    handle_response(response)


def main_function(bet_amount):
    fetch_balance()
    try:
        bet_amount = float(bet_amount)
    except ValueError:
        print("Invalid bet amount. Must be a numeric value.")
        return

    url = f"https://beta.bgaming-network.com/api/FourLuckyDiamonds/1919086/{token}"
    
    payload = {
        "command": "spin",
        "options": {
            "bets": {
                "0": bet_amount,
                "1": bet_amount,
                "2": bet_amount,
                "3": bet_amount,
                "4": bet_amount,
                "5": bet_amount,
                "6": bet_amount,
                "7": bet_amount,
                "8": bet_amount,
                "9": bet_amount
            }
        }
    }
    
    url = f"https://beta.bgaming-network.com/api/FourLuckyDiamonds/1919086/{token}"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Length": "109",
        "Content-Type": "application/json",
        "Origin": "https://beta.bgaming-network.com",
        "Priority": "u=1, i",
        "Referer": f"https://beta.bgaming-network.com/games/FourLuckyDiamonds/VRBX?play_token={token}",
        "Sec-CH-UA": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "X-CSRF-Token": xtoken
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    def handle_response(response):
        content_encoding = response.headers.get('Content-Encoding')
        try:
            if content_encoding == 'gzip':
                buf = BytesIO(response.content)
                with gzip.GzipFile(fileobj=buf) as f:
                    decompressed_data = f.read()
            elif content_encoding == 'deflate':
                decompressed_data = zlib.decompress(response.content)
            elif content_encoding == 'br':
                try:
                    decompressed_data = brotlicffi.decompress(response.content)
                except Exception as e:
                    decompressed_data = response.content
            else:
                decompressed_data = response.content

            try:
                data = decompressed_data.decode('utf-8')
                json_data = json.loads(data)
                if 'errors' in json_data:
                    error_code = json_data['errors'][0]['code']
                    if error_code == 301:
                        print("Not enough money")
                    elif error_code == 203:
                        print("Wrong token or api error")    
                    else:
                        print(f"Error code {error_code}: {json_data['errors'][0]['desc']}")
                elif response.status_code in {400, 401, 403, 404}:
                    print("Account information incorrect")
                elif response.status_code == 200:
                    print("Placed bet")
                else:
                    print(f"Unexpected status code: {response.status_code}")
            except json.JSONDecodeError:
                print("Failed to decode JSON response")
            except UnicodeDecodeError:
                print("Binary or unreadable data")
        except Exception as e:
            print(f"An error occurred: {e}")
    handle_response(response)

def launch_code():
    bet_amount = input("10 = 1RBX > ")  
    print("Starting Bloxflip Auto Player") 
    while True:
        main_function(bet_amount)
        time.sleep(15)

launch_code()
