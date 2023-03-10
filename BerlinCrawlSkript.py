# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 20:16:35 2023

@author: Florian
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates 
import os, sys
import numpy as np
import time
import random
import datetime


data = {
        "10555-10557": "Hansaviertel",
        "10557-10963": "Tiergarten",
        "10585-14059": "Charlottenburg",
        "10555-10557": "Hansaviertel",
        "10557-10963": "Tiergarten",
        "10585-14059": "Charlottenburg",
        "10115-10435": "Mitte",
        "10119-10439": "Prenzlauer Berg",
        "10243-10249": "Friedrichshain",
        "10315-10319": "Friedrichsfelde",
        "10315-10369": "Lichtenberg",
        "10317": "Rummelsburg",
        "10318": "Karlshorst",
        "10367-10369": "Fennpfuhl",
        "10439-13189": "Pankow",
        "10551-10559": "Moabit",
        "10585-14059": "Charlottenburg",
        "10589-13629": "Charlottenburg-Nord",
        "10707-14199": "Wilmersdorf",
        "10709-10713": "Halensee",
        "10711-14199": "Grunewald",
        "10777-12159": "Schöneberg",
        "10785-10999": "Kreuzberg",
        "10827-14197": "Friedenau",
        "10965-12099": "Neukölln",
        "10965-12279": "Tempelhof",
        "12099-12277": "Mariendorf",
        "12099-12359": "Britz",
        "12107-12307": "Marienfelde",
        "12107-12309": "Lichtenrade",
        "12107-12359": "Buckow",
        "12157-14195": "Steglitz",
        "12203-14195": "Lichterfelde",
        "12247-12249": "Lankwitz",
        "12351-12357": "Gropiusstadt",
        "12351-12359": "Rudow",
        "12435": "Alt-Treptow",
        "12435-12437": "Plänterwald",
        "12437-12439": "Niederschöneweide",
        "12437-12487": "Baumschulenweg",
        "12437-12489": "Johannisthal",
        "12459": "Oberschöneweide",
        "12459-12587": "Köpenick",
        "12487-12489": "Adlershof",
        "12524": "Altglienicke",
        "12526": "Bohnsdorf",
        "12527": "Grünau",
        "12527": "Schmöckwitz",
        "12559": "Müggelheim",
        "12587": "Friedrichshagen",
        "12589": "Rahnsdorf",
        "12619-12623": "Kaulsdorf",
        "12619-12629": "Hellersdorf",
        "12623": "Mahlsdorf",
        "10555-10557": "Hansaviertel",
        "10557-10963": "Tiergarten",
        "10585-14059": "Charlottenburg",
        "12679-12689": "Marzahn",
        "12683": "Biesdorf",
        "13051": "Malchow",
        "13051-13055": "Alt-Hohenschönhausen",
        "13051-13059": "Neu-Hohenschönhausen",
        "13051-13059": "Wartenberg",
        "13051-13129": "Blankenburg",
        "13051-13129": "Stadtrandsiedlung Malchow",
        "13057": "Falkenberg",
        "13086-13088": "Weißensee",
        "13088-13129": "Heinersdorf",
        "13125": "Buch",
        "13125": "Karow",
        "13127-13156": "Französisch Buchholz",
        "13127-13159": "Blankenfelde",
        "13156-13158": "Niederschönhausen",
        "13156-13158": "Rosenthal",
        "13158": "Wilhelmsruh",
        "13347-13409": "Gesundbrunnen",
        "13347-13409": "Wedding",
        "13403-13509": "Reinickendorf",
        "13403-13509": "Wittenau",
        "13403-13629": "Tegel",
        "13435-13439": "Märkisches Viertel",
        "13465": "Frohnau",
        "13465-13467": "Hermsdorf",
        "13469": "Lübars",
        "13469": "Waidmannslust",
        "13503-13505": "Heiligensee",
        "13505": "Konradshöhe",
        "13509": "Borsigwalde",
        "13581-13593": "Staaken",
        "13581-13597": "Wilhelmstadt",
        "13581-14052": "Spandau",
        "13583-13591": "Falkenhagener Feld",
        "13585-13589": "Hakenfelde",
        "13599": "Haselhorst",
        "13599-13629": "Siemensstadt",
        "14050-14059": "Westend",
        "14089": "Gatow",
        "14089": "Kladow",
        "14109": "Wannsee",
        "14109-14193": "Nikolassee",
        "14129-14169": "Zehlendorf",
        "14169-14195": "Dahlem",
        "14193-14199": "Schmargendorf"
}

df = pd.DataFrame.from_dict(data, orient='index', columns=['Bezirk'])
df.reset_index(inplace=True)
df.rename(columns={'index': 'Postleitzahl'}, inplace=True)


'''while True:
    random_row = df.sample()
    print(random_row)
    time.sleep(5)'''
    
while True:
    now = datetime.datetime.now()
    #Saturday = 5
    if now.weekday() == 5 and now.hour == 21 and now.minute == 10:
        random_row = df.sample()
        print(random_row)
        time.sleep(60)
    else:
        time.sleep(1)

    
    
    

