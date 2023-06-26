#!/bin/python3

# Importar libreria para capturar argumentos pasados al script.
import os

def check_apache_installed():
    # Use the os.system() function to execute the apache2 command
    exit_code = os.system('apache2 -v > /dev/null 2>&1')

    if exit_code == 0:
        # Apache is installed
        os.system('apache2 -v')
    else:
        # Apache is not installed
        print("Apache is not installed.")

check_apache_installed()
