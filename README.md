# Fanuc web interface data parser

Client example:
```python
import socket, json


HOST, PORT = "localhost", 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    
    # Send request
    data = 'DIN70 DIN65 DIN66 DIN67 DIN68'    # MAX 60
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Get response as JSON(Dict)
    received = str(sock.recv(1024), "utf-8")
    response = json.loads(received)

    print(f'{response} \n{type(response)}')
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