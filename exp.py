import json


with open('data.json', 'r') as file:
    data = json.load(file)

    for val in data:
        data[val] = '1' if data[val] == 'ON' else '0'


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

    print(
        'Data:\n'
        f'programm_number: { programm_number }\n'
        f'error_code: { error_code }\n'
        )