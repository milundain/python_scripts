#!/bin/python3

# Importar libreria para capturar argumentos pasados al script.
import subprocess
import os

# Definir la funcion para comprobar si apache esta intalado y su version.
def apache_service():

# Utilizar os.system() para ejecutar el comando de version de apache.
    
    system_code = os.system('systemctl status apache2 > /dev/null 2>&1')
    service_code = os.system('service apache2 status > /dev/null 2>&1')
    
    if system_code == 0:
    # Apache is installed
        system_status = subprocess.check_output(['systemctl','status','apache2']).decode().strip()
        print(system_status)

    elif service_code == 0:
        service_status = subprocess.check_output(['service','apache2','status']).decode().strip()
        print(service_status)

    else:
    # Apache is not installed
        print("El servicio no se esta ejecutando")

apache_service()