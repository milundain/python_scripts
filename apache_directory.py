import os

def check_apache_sites_directory():
    apache_sites_directory = '/etc/apache2/sites-available'  # Ruta del directorio de sitios de Apache en Linux

    if os.path.exists(apache_sites_directory) and os.path.isdir(apache_sites_directory):
        print("El directorio de sitios de Apache existe.")
    else:
        print("El directorio de sitios de Apache no existe.")

check_apache_sites_directory()
