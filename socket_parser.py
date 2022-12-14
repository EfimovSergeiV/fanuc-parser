"""
Сервер с парсером по регулярному выражению. 

Можно настроить URL, TEST и TIMEOUT
"""


import socketserver
import re, requests, json
from time import sleep
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PATH = 'MD/IOSTATE.DG'

URL = 'http://127.0.0.1/'   # fanuc : http://192.168.0.1/ or local : http://127.0.0.1/
TEST = True                 # True or False
TIMEOUT = 1                 # Таймауты запросов к fanuc

class TCPHandler(socketserver.BaseRequestHandler):

    VALUES = {}

    def handle(self):
        try:
            while True:
                print("GET DATA")

                if TEST:                    
                    with open(f'{ BASE_DIR }/examples/data.json', 'r') as file:
                        data = json.load(file)
                        self.VALUES = data

                else:

                    try:
                        response = requests.get(f'{ URL }{ PATH }')
                        text = response.text
                    except requests.exceptions.ConnectionError:
                        text = 'ERR[1000]  ConnectErr'

                    server_data = re.findall(r'\w{0,5}[A-Z]+\[[\s{0,4}\d{0,4}]+\]+\s{0,6}\w{0,10}', text)
                    
                    for string in server_data:
                        name_value = str(string).split("]")
                        name = name_value[0].split("[")
                        reg, sec, str_val = name[0], name[1].strip(), name_value[1].strip()

                        self.VALUES[f'{reg}{sec}'] = str_val

                data_send = json.dumps(self.VALUES, ensure_ascii=False)
                self.request.sendall(bytes(data_send, encoding="utf-8"))
                sleep(TIMEOUT)

        except ConnectionAbortedError:
            print("Connection aborted")


if __name__ == "__main__":
    HOST, PORT = "localhost", 9000

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        try:
            print("Server started")
            server.serve_forever()
        except KeyboardInterrupt:
            print("Close server")