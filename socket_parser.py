import re, requests, json
import configparser, socketserver
from datetime import datetime


config = configparser.ConfigParser()
config.read('CONFIG.cfg')
URL = config.get('DEFAULT', 'URL' )
PATH = config.get('DEFAULT', 'PATH' )
TEST = config.get('DEFAULT', 'TEST' )
TIMEOUT = config.get('DEFAULT', 'TIMEOUT' )



class TCPHandler(socketserver.BaseRequestHandler):

    VALUES = {}
    LATEST_UPDATED = ['0000', '00', '00', '00', '00', '00']

    def handle(self):
        request_data = self.request.recv(1024).strip().decode("utf-8")
        list_request = str(request_data).split(" ")


        if TEST.lower() == 'true':
            response_dict = {}
            for key in list_request:
                response_dict[key] = "OFF"


        else:
            # print(len(self.VALUES))

            # print(self.LATEST_UPDATED)


            # if self.LATEST_UPDATED:
            #     print(f'{self.LATEST_UPDATED}')


            # print(datetime.now().strftime('%Y %m %d %H %M %S').split(" "))
            # self.LATEST_UPDATED = datetime.now().strftime('%Y %m %d %H %M %S').split(" ")

            # if len(LATEST_UPDATED):
            #     LATEST_UPDATED = str(datetime.now().strftime('%Y %m %d %H %M %S')).split(" ")

            # print(len(LATEST_UPDATED))
            # LATEST_UPDATED = str(datetime.now().strftime('%Y %m %d %H %M %S')).split(" ")

            # print(f"Now: { datetime.now().strftime('%Y %m %d %H %M %S') }")



            if True:#len(self.VALUES) == 0:
                # print("CREATE/UPDATE NEW DICT")
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

            response_dict = {}
            for key in list_request:
                response_dict[key] = self.VALUES[key]

        data_send = json.dumps(response_dict, ensure_ascii=False)
        self.request.sendall(bytes(data_send, encoding="utf-8"))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9000

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()
