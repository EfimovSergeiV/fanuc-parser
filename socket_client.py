import socket, json

HOST, PORT = "localhost", 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    data = 'DIN70 DIN65 DIN66 DIN67 DIN68 DIN69'    # MAX 60

    print(f'DATA LENGT: {len(data)}')
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    received = str(sock.recv(1024), "utf-8")
    response = json.loads(received)

    print(f'{response} \n{type(response)}')
