"""
Чтение данных
"""


def read_bytes(response):
    """
    Преобразовываем значения в словаре с ON/OFF на 0/1
    Соответствующие байты преобразуем в целое число
    """

    data = {}

    for val in response:
        data[val] = '1' if response[val] == 'ON' else '0'

    print(data)


    error_code_bytes = '0b' + ''.join((
        data['DIN96'], data['DIN95'], data['DIN94'], data['DIN93'],
        data['DIN92'], data['DIN91'], data['DIN90'], data['DIN89'],       
    ))

    programm_number_bytes = '0b' + ''.join((
        data['DOUT100'], data['DOUT99'], data['DOUT98'], data['DOUT97']
    ))

    voltage_bytes = '0b' + ''.join((
        data['DIN144'], data['DIN143'], data['DIN142'], data['DIN141'],
        data['DIN140'], data['DIN139'], data['DIN138'], data['DIN137'],
        data['DIN136'], data['DIN135'], data['DIN134'], data['DIN133'],
        data['DIN132'], data['DIN131'], data['DIN130'], data['DIN129'],
    ))

    current_bytes = '0b'+ ''.join((
        data['DIN160'], data['DIN159'], data['DIN158'], data['DIN157'],
        data['DIN156'], data['DIN155'], data['DIN154'], data['DIN153'],
        data['DIN152'], data['DIN151'], data['DIN150'], data['DIN149'],
        data['DIN148'], data['DIN147'], data['DIN146'], data['DIN145'],
    ))

    wire_feed_speed_bytes = '0b' + ''.join((
        data['DIN176'], data['DIN175'], data['DIN174'], data['DIN173'],
        data['DIN172'], data['DIN171'], data['DIN170'], data['DIN169'],
        data['DIN168'], data['DIN167'], data['DIN166'], data['DIN165'],
        data['DIN164'], data['DIN163'], data['DIN162'], data['DIN161'],
    ))

    motor_current_bytes = '0b' + ''.join((
        data['DIN192'], data['DIN191'], data['DIN190'], data['DIN189'],
        data['DIN188'], data['DIN187'], data['DIN186'], data['DIN185'],
        data['DIN184'], data['DIN183'], data['DIN182'], data['DIN181'],
        data['DIN180'], data['DIN179'], data['DIN178'], data['DIN177'],
    ))

    job_number_bytes = '0b' + ''.join((
        data['DOUT112'], data['DOUT111'], data['DOUT110'], data['DOUT109'],
        data['DOUT108'], data['DOUT107'], data['DOUT106'], data['DOUT105'],
    ))

    wire_feed_speed_two_bytes = '0b' + ''.join((
        data['DOUT144'], data['DOUT143'], data['DOUT142'], data['DOUT141'],
        data['DOUT140'], data['DOUT139'], data['DOUT138'], data['DOUT137'],
        data['DOUT136'], data['DOUT135'], data['DOUT134'], data['DOUT133'],
        data['DOUT132'], data['DOUT131'], data['DOUT130'], data['DOUT129'],
    ))

    volt_correction_bytes = '0b' + ''.join((
        data['DOUT160'], data['DOUT159'], data['DOUT158'], data['DOUT157'],
        data['DOUT156'], data['DOUT155'], data['DOUT154'], data['DOUT153'],
        data['DOUT152'], data['DOUT151'], data['DOUT150'], data['DOUT149'],
        data['DOUT148'], data['DOUT147'], data['DOUT146'], data['DOUT145'],
    ))

    dynamics_bytes = '0b' + ''.join((
        data['DOUT176'], data['DOUT175'], data['DOUT174'], data['DOUT173'],
        data['DOUT172'], data['DOUT171'], data['DOUT170'], data['DOUT169'],
        data['DOUT168'], data['DOUT167'], data['DOUT166'], data['DOUT165'],
        data['DOUT164'], data['DOUT163'], data['DOUT162'], data['DOUT161'],
    ))

    error_code = int(error_code_bytes, 0)
    voltage = int(voltage_bytes, 0)
    current = int(current_bytes, 0)
    wire_feed_speed = int(wire_feed_speed_bytes, 0)
    motor_current = int(motor_current_bytes, 0)
    programm_number = int(programm_number_bytes, 0)
    job_number = int(job_number_bytes, 0)
    wire_feed_speed_two = int(wire_feed_speed_two_bytes, 0)
    volt_correction = int(volt_correction_bytes, 0)
    dynamics = int(dynamics_bytes, 0)

    arc_detect =  data["DIN81"]
    wirestick = data["DIN83"]

    print(
        'Data from bytes:\n'
        f'Сварочная дуга\t\t\t\t{ arc_detect }\n'
        f'Залипание сварочн.проволоки\t\t{ wirestick }\n'
        f'error_code:\t\t\t\t{ error_code }\n'
        f'voltage:\t\t\t\t{ voltage }\n'
        f'current:\t\t\t\t{ current }\n'
        f'wire_feed_speed:\t\t\t{ wire_feed_speed }\n'
        f'motor_current:\t\t\t\t{ motor_current }\n'
        f'programm_number:\t\t\t{ programm_number }\n'
        f'job_number:\t\t\t\t{ job_number }\n'
        f'wire_feed_speed_two:\t\t\t{ wire_feed_speed_two }\n'
        f'volt_correction:\t\t\t{ volt_correction }\n'
        f'dynamics:\t\t\t\t{ dynamics }\n'
        )

    return {
        "arc_detect": arc_detect, 
        "wirestick": wirestick,
        "error_code": error_code, 
        "voltage": voltage, 
        "current": current, 
        "wire_feed_speed": wire_feed_speed, 
        "motor_current": motor_current, 
        "programm_number": programm_number, 
        "job_number": job_number, 
        "wire_feed_speed_two": wire_feed_speed_two, 
        "volt_correction": volt_correction, 
        "dynamics": dynamics, 
    }
        
