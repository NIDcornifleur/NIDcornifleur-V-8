#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import time
import subprocess
reader = SimpleMFRC522()

#NIDrfidV8.py


#6 décembre 2022

#Ce script fonctionne sur le NIDcornifleur Version 8 qui est piloté par un Raspberry Pi
#Zero 2 WiFi.  L'appareil et le script ont été créés par Roméo St-Cyr à l'automne 2022.


#En entrant la caméra dans l'ouverture du nichoir, le tag RFID est lu et l'identification
#est imprimée à droite de la date et heure sur la vidéo.

#La seconde d'après, les leds infrarouges s'allument  et une seconde plus tard,
#l'enrégistrement débute pour une période de 15 secondes. Finalement, les leds s'éteignent
#après 5 secondes.



try:
    while True:




        id, text = reader.read()
        print(text)
        annotate = open("/dev/shm/mjpeg/user_annotate.txt", 'w')
        annotate.write(text)
        annotate.close()
        time.sleep(1)

        subprocess.call(["sh", "/var/www/html/macros/led_ir_full.sh"])
        time.sleep(1)

        cmdpipe = open("/var/www/html/FIFO", 'w')
        cmdpipe.write('ca 1 15')
        cmdpipe.close()
        time.sleep (20)


        subprocess.call(["sh", "/var/www/html/macros/led_all_off.sh"])


except Exception as e:
    print(e)
