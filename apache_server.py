import os
import re

def list_apache_sites():
    apache_sites_directory = '/etc/apache2/sites-available'  # Ruta del directorio de sitios de Apache en Linux

    regex = re.compile(r'^\tServerName')

    if os.path.exists(apache_sites_directory) and os.path.isdir(apache_sites_directory):
        # Obtener la lista de archivos en el directorio de sitios de Apache
        site_files = os.listdir(apache_sites_directory)

        if site_files:
            print("Sitios disponibles en Apache:\n")

            for file_name in site_files:
                # Mostrar solo los archivos de configuración de sitios de Apache
                if file_name.endswith('.conf'):
                    site_name = file_name[:-5]  # Eliminar la extensión .conf
                    print("Sitio:", site_name)

                    # Leer el archivo de configuración del sitio
                    site_path = os.path.join(apache_sites_directory, file_name)
                    with open(site_path, 'r') as f:
                        for line in f:
                            if regex.search(line):
                                server_name = line.strip().split()[1]
                                print("ServerName:", server_name)

                            if 'Listen' in line:
                                port = line.strip().split()[1]
                                print("Puerto:", port)

                    print()  # Agregar línea en blanco para separar los sitios
        else:
            print("No se encontraron sitios disponibles en Apache.")
    else:
        print("El directorio de sitios de Apache no existe.")

list_apache_sites()
