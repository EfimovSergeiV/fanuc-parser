"""
To debug the parser
"""
import socket, json, os
from time import sleep

from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
HOST, PORT = "localhost", 9000

count = 0

data = {}
old_array = ()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    print(f'\t\t\t\tDOUT315')

    while True:
        count += 1
        
        try:
            received = str(sock.recv(8000000), "utf-8")
        except KeyboardInterrupt:
            try:
                print('Остановлен на 30 сек.')
                sleep(15)
            except KeyboardInterrupt:
                try:
                    print('Остановлен на 2 минуты.')
                    sleep(120)
                except KeyboardInterrupt:
                    print('Завершение.')
                    break

        try:
            response = json.loads(received)

            data = {}

            for val in response:
                data[val] = '1' if response[val] == 'ON' else '0'


            array_bytes = (
                data['DIN144'], data['DIN143'], data['DIN142'], data['DIN141'],
                data['DIN140'], data['DIN139'], data['DIN138'], data['DIN137'],
                data['DIN136'], data['DIN135'], data['DIN134'], data['DIN133'],
                data['DIN132'], data['DIN131'], data['DIN130'], data['DIN129'],                
            )

            """
                Для боевого теста
            """
            # error_number_bytes = (
            #     data['DOUT315'], data['DOUT314'], data['DOUT313'], data['DOUT312'],
            #     data['DOUT310'], data['DOUT309'], data['DOUT308'], data['DOUT307'],
            #     data['DOUT306'], data['DOUT305'], data['DOUT304'], data['DOUT303'],
            #     data['DOUT302'], data['DOUT301'], data['DOUT300'],
            # )
            # error_id_bytes = (
            #     data['DOUT333'], data['DOUT332'], data['DOUT331'], data['DOUT330'],
            #     data['DOUT329'], data['DOUT328'], data['DOUT327'], data['DOUT326'],
            #     data['DOUT325'], data['DOUT324'], data['DOUT323'], data['DOUT322'],
            #     data['DOUT321'], data['DOUT320'], data['DOUT319'], data['DOUT318'],
            #     data['DOUT317'], data['DOUT316'],
            # )
            

            value_bytes = '0b' + ''.join(array_bytes)

            # error_id = '0b' + ''.join(array_bytes)
            # error_number = '0b' + ''.join(array_bytes)
            # id = int(error_id, 0)
            # error = int(error_number, 0)


            value = int(value_bytes, 0)

            if count % 30 == 0:
                os.system('cls||clear')
                print(f'NumberErr: {value}\tErr: {value}')

            now_time = datetime.now().strftime('%H:%M:%S:%f')


            changed = '' if array_bytes == old_array else 'changed'


            # print(f'{now_time} cnt: { count } val: { value } byte: {array_bytes} {changed}')
            print(f'{now_time} cnt: { count } val: { value } byte: {array_bytes} {changed}')

            old_array = array_bytes

        except:
            print("Err")