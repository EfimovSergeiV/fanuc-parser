"""
Этот пример принимает данные с сокеет-сервера и записывает их в SQLite базу данных

Всё это немного тормозит, так как база не успевает. Если подумать, то можно улучшить.
"""


import socket, json, os, sqlite3
from datetime import datetime
from pathlib import Path

from read_data import read_bytes

BASE_DIR = Path(__file__).resolve().parent.parent
HOST, PORT = "localhost", 9000

count = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    # conn = sqlite3.connect(f'{ BASE_DIR }/examples/sqlite3.db')
    # cursor = conn.cursor()

    try:
        while True:
            count += 1
            
            received = str(sock.recv(8000000), "utf-8")
            try:
                response = json.loads(received)

                os.system('cls||clear')
                now_time = datetime.now().strftime('%H:%M:%S')
                try:
                    print(
                        f'Счётчик\t\t\t\t\t{ count }'
                        f'Время\t\t\t\t\t{ now_time }'
                        f'Ошибки\t\t\t\t\t{ response["GIN1"]}'
                        f'Вольтаж\t\t\t\t\t{ response["GIN2"]}'
                        f'Ток\t\t\t\t\t{ response["GIN3"]}'
                        f'Скорость подачи проволоки\t\t{ response["GIN4"]}'
                        f'Ток двигателя\t\t\t\t{ response["GIN5"]}'
                        f'Номер программы\t\t\t\t{ response["GOUT1"]}'
                        f'Номер работы\t\t\t\t{ response["GOUT2"]}'
                        f'Скорость подачи проволоки\t\t{ response["GOUT3"]}'
                        f'Коррекция напряжения\t\t\t{ response["GOUT4"]}'
                        f'Динамика\t\t\t\t{ response["GOUT5"]}'
                        f'PNS\t\t\t\t\t{ response["GOUT8"]}'
                        )

                except KeyError:
                    print("Данные не найдены")

                data_from_bytes = {
                    "arc_detect": "",
                    "wirestick": "",
                }

                try:
                    data_from_bytes = read_bytes(response)
                except:
                    pass

                
                try:
                    data_to_db = [
                        data_from_bytes["arc_detect"],
                        data_from_bytes["wirestick"],
                        response["GIN1"],
                        response["GIN2"],
                        response["GIN3"],
                        response["GIN4"],
                        response["GIN5"],
                        response["GOUT1"],
                        response["GOUT2"],
                        response["GOUT3"],
                        response["GOUT4"],
                        response["GOUT5"],
                        response["GOUT8"],
                        str(now_time),
                    ]

                    # cursor.execute("INSERT INTO welding VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);", data_to_db)
                    # conn.commit()

                except KeyError:
                    print("Данные не найдены")

            except json.decoder.JSONDecodeError:
                pass
        

    except KeyboardInterrupt:
        print("Exit")
    
    # conn.close()
    sock.close()