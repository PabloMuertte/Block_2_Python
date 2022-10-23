from user_interface import temperature_view
from user_interface import preassure_view
from user_interface import wind_speed_view

def create(device =1):
    xml = '<xml>\n'
    xml += '    <temperature_view units = "c">{}</temperature_view>\n'\
        .format(temperature_view(device))
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml += '    <preassure_view units = "mmHg">{}</prassure_view>\n'\
        .format(preassure_view(device))
    xml += '</xml>'


    with open('/home/pablo/Documents/Python GB/Block_2_Python/siminar_1_2_3/siminar_4_task_2/data.xml', 'w') as page:
        page.write(xml)
    
    return xml

def new_create(data ,device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '    <temperature_view units = "f">{}</temperature_view>\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w)
    xml += '    <preassure_view units = "mmHg">{}</prassure_view>\n'\
        .format(p)
    xml += '</xml>'


    with open('/home/pablo/Documents/Python GB/Block_2_Python/siminar_1_2_3/siminar_4_task_2/new_data.xml', 'w') as page:
        page.write(xml)
    
    return data

