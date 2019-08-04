import os
import re
import time
from io import BytesIO
from itertools import count
from os.path import split

import requests
from bs4 import BeautifulSoup
from django.core import files

from parlamento.admin import Iniciativa
from parlamento.models import Diputado, Entidad, Iniciativa, Partido

url_partidos = 'http://sitl.diputados.gob.mx/LXIV_leg/listado_diputados_gpnp.php?tipot=%s'
url_diputado = 'http://sitl.diputados.gob.mx/LXIV_leg/curricula.php?dipt=%s'

partidos = {
    "Morena": 14,
    "Pan": 3,
    "Pri": 1,
    "Encuentro Social": 15,
    "Partido del Trabajo": 4,
    "Movimiento Ciudadano": 6,
    "PRD": 2,
    "Partido Verde": 5,
    "Sin Partido": 16
}

def init_scraper():

    for partido in Partido.objects.all():
        req_list_diputados = requests.get(
            url_partidos % (str(partido.tipot)))
        html_diputados = BeautifulSoup(req_list_diputados.text,  'html.parser')

        for dip_perdon in html_diputados.find_all('tr'):
            if len(dip_perdon.findChildren()) == 4:
                id_dip = dip_perdon.find('a').get('href').split('=').pop()
                distrit = dip_perdon.find_all('td')[2].text.strip()

                entidad, created = Entidad.objects.get_or_create(
                    name=dip_perdon.find_all('td')[1].text)

                request_dip = requests.get(url_diputado % (id_dip))

                html_diputado = BeautifulSoup(request_dip.text,  'html.parser')

                foto = html_diputado.find(
                    'img', {'class': 'fotodip'}).get('src')
                d_dip = [i for i in html_diputado.find(
                    'table', {'class': 'fondoimg2'}).find_all('td')]
                arr_dip = [i.text for i in html_diputado.find_all(
                    'td', {'class': 'textocurri'})]
                name = html_diputado.find(
                    'td', {'class': 'textocurrienc'}).text.replace('Dip.', '').strip()

                img_url = 'http://sitl.diputados.gob.mx/LXIV_leg/' + foto.replace('./', '')
               
                # request_img = requests.get(img_url)
                # fp = BytesIO()
                # fp.write(request_img.content)

                # diputado_obj, c = Diputado.objects.get_or_create(
                #     name=name,
                #     type_lection=arr_dip[1],
                #     email=arr_dip[5],
                #     suplente=arr_dip[9],
                #     distrit=distrit,
                #     entidad=entidad,
                #     partido=partido
                # )
                # # if not c :
                # name_iamge = name.lower().replace(
                #     ' ', '_')+img_url.split("/")[-1]
                # diputado_obj.image.save(name_iamge, files.File(fp))
                
                # tipos de iniciativas
                # De Grupo
                # Adherente
                # Iniciante
                # Diversos Grupos Parlamentarios
                
                # ('GROUP', 'De grupo'),
                # ('ADHERENT', 'Adherente'),
                # ('INITIATOR', 'Iniciante'),
                # ('DIVGROUP', 'Diversos grupos parlamentarios'),                
                print(name)
                iniciativas = html_diputado.find('div', {'class': 'iniciativas'}).find_all('table')[2]
                print(iniciativas)
                # for i in iniciativas:
                    # print(i)

                # if len(iniciativas)>0:
                #     for iniciativa in iniciativas:
                #         print(iniciativa.text)
                #         print('--------------------------------------')
                #         if 'De grupo' in iniciativa.text:
                #             type_presentation = 'GROUP'
                #         if 'Adherente' in iniciativa.text:
                #             type_presentation = 'ADHERENT'
                #         if 'Iniciante' in iniciativa.text:
                #             type_presentation = 'INITIATOR'
                #             print(type_presentation)
                #         if 'Diversos Grupos Parlamentarios' in iniciativa.text:
                #             type_presentation = 'DIVGROUP'
                #             print(type_presentation)
                #         else:
                #             type_presentation = ''
                        
                #         print(type_presentation)







# req = requests.get('http://sitl.diputados.gob.mx/LXIV_leg/info_diputados.php')
# html_soup = BeautifulSoup(req.text,  'html.parser')


# def create_partido():
#     for a in html_soup.find('map', {'name': 'mapacintillo'}).find_all('area'):
#         tipot = a.get('href').split('=').pop()
#         print(tipot)
#         name = [p for p in partidos if partidos[p] == int(tipot)][0]

#         p, created = Partido.objects.get_or_create(
#             tipot=a.get('href').split('=').pop(),
#             name=name
#         )
#         print(created)


# create_partido()
# init_scraper()

