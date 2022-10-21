# Fanuc web interface data parser

Install:
```text
git clone https://github.com/EfimovSergeiV/fanuc-parser.git

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