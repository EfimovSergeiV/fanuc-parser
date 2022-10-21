# Fanuc web interface data parser

Install:
```text
get PYTHON  https://www.python.org/
get GIT     https://git-scm.com/

git clone https://github.com/EfimovSergeiV/fanuc-parser.git
cd fanuc-parser

python socket_parser.py
python socket_client.py

Автозагрузка:
(Путь до терминала, с параметрами: /k python <absolute\path\to\script>)
cmd /k python <absolute_path_to_script>
```


Client example:
```python
import socket, json


HOST, PORT = "localhost", 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    try:
        while True:

            received = str(sock.recv(24576), "utf-8")
            response = json.loads(received)
            print(f'\n\n{ response }\nLEN RESPONSE: {len( response )} \n{type( response )}')

    except KeyboardInterrupt:
        print("Exit")
```

Config:

```cfg
[DEFAULT]
URL     = http://127.0.0.1/
PATH    = MD/IOSTATE.DG
TEST    = true
TIMEOUT = 1

# LOCALHOST = http://127.0.0.1/
# FANUCHOST = http://192.168.0.1/
```