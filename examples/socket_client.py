import socket, json, os
from time import sleep

# import pyttsx3
import sqlite3
from datetime import datetime
from pathlib import Path

# engine = pyttsx3.init()
# engine.setProperty('rate', 200)

from read_data import read_bytes

BASE_DIR = Path(__file__).resolve().parent.parent
HOST, PORT = "localhost", 9000

count = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    conn = sqlite3.connect(f'{ BASE_DIR }/examples/sqlite3.db')
    print(f'{ BASE_DIR }sqlite3.db')
    cursor = conn.cursor()

    try:
        while True:
            count += 1
            
            received = str(sock.recv(24576), "utf-8")
            try:
                response = json.loads(received)
                
                # VOICE
                # engine.say(f"Получен {len( response )} параметр")
                # engine.runAndWait()

                os.system('cls||clear')
                now_time = datetime.now().strftime('%H:%M:%S')
                print(f"""
Счётчик\t\t\t\t\t{ count }
Время\t\t\t\t\t{ now_time }
Ошибки\t\t\t\t\t{ response["GIN1"]}
Вольтаж\t\t\t\t\t{ response["GIN2"]}
Ток\t\t\t\t\t{ response["GIN3"]}
Скорость подачи проволоки\t\t{ response["GIN4"]}
Ток двигателя\t\t\t\t{ response["GIN5"]}
Номер программы\t\t\t\t{ response["GOUT1"]}
Номер работы\t\t\t\t{ response["GOUT2"]}
Скорость подачи проволоки\t\t{ response["GOUT3"]}
Коррекция напряжения\t\t\t{ response["GOUT4"]}
Динамика\t\t\t\t{ response["GOUT5"]}
PNS\t\t\t\t\t{ response["GOUT8"]}
                                    """)

                # print(f'\n\n{ response }\nLEN RESPONSE: {len( response )} \n{type( response )}')

                data_from_bytes = {
                    "arc_detect": "",
                    "wirestick": "",
                }

                try:
                    data_from_bytes = read_bytes(response)
                except:
                    pass


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

                cursor.execute("INSERT INTO welding VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);", data_to_db)
                conn.commit()
                print(BASE_DIR)
                # sleep(3)


            except json.decoder.JSONDecodeError:
                pass
        

    except KeyboardInterrupt:
        print("Exit")
    
    conn.close()
    sock.close()