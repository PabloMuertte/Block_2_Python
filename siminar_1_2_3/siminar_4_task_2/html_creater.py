from user_interface import temperature_view
from user_interface import preassure_view
from user_interface import wind_speed_view

def create(device =1):
    style = 'style ="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Prassure: {} c</p>\n'\
        .format(style, preassure_view(device))
    html += '   <p {}>Wind_speed: {} c</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   </body>\n<html>'

    with open('/home/pablo/Documents/Python GB/Block_2_Python/siminar_1_2_3/siminar_4_task_2/index.html', 'w') as page:
        page.write(html)
    
    return html

def new_create(data,device =1):
    t, p, w = data
    style = 'style ="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '   <p {}>Prassure: {} c</p>\n'\
        .format(style, p)
    html += '   <p {}>Wind_speed: {} c</p>\n'\
        .format(style, w)
    html += '   </body>\n<html>'

    with open('/home/pablo/Documents/Python GB/Block_2_Python/siminar_1_2_3/siminar_4_task_2/new_index.html', 'w') as page:
        page.write(html)
    
    return data