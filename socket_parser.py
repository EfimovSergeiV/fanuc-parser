import socketserver
import re, requests, json
from time import sleep


URL = 'http://127.0.0.1/'   # FANUCHOST : http://192.168.0.1/
PATH = 'MD/IOSTATE.DG'
TEST = False                # Or False for production
TIMEOUT = 1

class TCPHandler(socketserver.BaseRequestHandler):

    VALUES = {}

    def handle(self):
        try:
            while True:
                print("GET DATA")

                if TEST:
                    self.VALUES = {'FLG964': 'OFF', 'FLG453': 'OFF', 'FLG965': 'OFF'}

                else:

                    response = requests.get(f'{ URL }{ PATH }')
                    server_data = re.findall(r'\w{0,5}[A-Z]+\[[\s{0,4}\d{0,4}]+\]+\s{0,6}\w{0,10}', response.text)
                    
                    for string in server_data:
                        name_value = str(string).split("]")
                        name = name_value[0].split("[")
                        reg, sec, str_val = name[0], name[1].strip(), name_value[1].strip()

                        try:
                            val = float(str_val)
                        except ValueError:
                            val = str_val

                        self.VALUES[f'{reg}{sec}'] = val

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