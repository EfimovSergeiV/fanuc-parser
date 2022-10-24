import socket, json, os
from time import sleep

# import pyttsx3
import sqlite3


# engine = pyttsx3.init()
# engine.setProperty('rate', 200)
HOST, PORT = "localhost", 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    try:
        while True:
            
            received = str(sock.recv(24576), "utf-8")
            try:
                response = json.loads(received)
                
                # VOICE
                # engine.say(f"Получен {len( response )} параметр")
                # engine.runAndWait()
                os.system('cls||clear')
                print(f"""
{ response["GIN1"]}\tОшибки
{ response["GIN2"]}\tВольтаж
{ response["GIN3"]}\tТок
{ response["GIN4"]}\tСкорость подачи проволоки
{ response["GIN5"]}\tТок двигателя
{ response["GOUT1"]}\tНомер программы
{ response["GOUT2"]}\tНомер работы
{ response["GOUT3"]}\tСкорость подачи проволоки
{ response["GOUT4"]}\tКоррекция напряжения
{ response["GOUT5"]}\tДинамика
{ response["GOUT8"]}\tPNS
                """)

                # print(f'\n\n{ response }\nLEN RESPONSE: {len( response )} \n{type( response )}')

            except json.decoder.JSONDecodeError:
                pass

    except KeyboardInterrupt:
        print("Exit")