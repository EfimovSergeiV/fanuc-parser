# Fanuc web interface data parser

Install:
```text
get PYTHON  https://www.python.org/
get GIT     https://git-scm.com/

git clone https://github.com/EfimovSergeiV/fanuc-parser.git
pip install requests

cd fanuc-parser

python socket_parser.py
python socket_client.py

Автозагрузка:
(Путь до терминала, с параметрами: /k python <absolute\path\to\script>)
cmd /k python <absolute_path_to_script>
```

## Examples:
Client example
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

Read data from bytes
```python
    error_code_bytes = ''.join((
        data['DIN96'],
        data['DIN95'],
        data['DIN94'],
        data['DIN93'],
        data['DIN92'],
        data['DIN91'],
        data['DIN90'],
        data['DIN89'],
    ))

    programm_number_bytes = ''.join((
        data['DOUT100'],
        data['DOUT99'],
        data['DOUT98'],
        data['DOUT97']
    ))

    programm_number = int(f"0b{ programm_number_bytes }", 0) * 0.2
    error_code = int(f"0b{ error_code_bytes }", 0) * 0.5 
```

Config to socket_parser.py:

```python
URL     = 'http://127.0.0.1/'
PATH    = 'MD/IOSTATE.DG'
TEST    = False                # Or False for production
TIMEOUT = 1

# LOCALHOST : http://127.0.0.1/
# FANUCHOST : http://192.168.0.1/
```

Talking client
```
Get ESpeak  https://espeak.sourceforge.net/

pip install pyttsx3
```

Models
```
    time = models.DateField(verbose_name="Дата создания", default=timezone.now)
    error_code = models.FloatField(verbose_name="Ошибки")
    voltage = models.FloatField(verbose_name="Вольтаж")
    current = models.FloatField(verbose_name="Ток")
    wire_feed_speed = models.FloatField(verbose_name="Скорость подачи проволоки")
    motor_current = models.FloatField(verbose_name="Ток двигателя")
    program_number = models.FloatField(verbose_name="Номер программы")
    job_number = models.FloatField(verbose_name="Номер работы")
    wire_feed_speed = models.FloatField(verbose_name="Скорость подачи проволоки")
    volt_correction = models.FloatField(verbose_name="Коррекция напряжения")
    dynamics = models.FloatField(verbose_name="Динамика")
```