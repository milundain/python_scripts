#!/bin/python3
 
# Importar libreria para capturar argumentos pasados al script.
 
import sys
import subprocess
import os

# Definir la funcion para comprobar si el servicio de apache esta corriendo.
def apache_service():

# Utilizar os.system() para ejecutar el comando de estado de servicio.
    
    system_code = os.system('systemctl status apache2 > /dev/null 2>&1')
    service_code = os.system('service apache2 status > /dev/null 2>&1')
    
    if system_code == 0:

# Revisar si el servicio esta en ejecucion con systemctl o service.
        system_status = subprocess.check_output(['systemctl','status','apache2']).decode().strip()
        return system_status

    elif service_code == 0:
        service_status = subprocess.check_output(['service','apache2','status']).decode().strip()
        return service_status

    else:
 # Si no responde con ninguno de los comandos anteriores no esta en ejecucion.
        print("El servicio no se esta ejecutando")
        sys.exit()




# Definir la funcion para comprobar si el directorio de sitios por default existe.
def check_apache_sites_directory(apache_sites_directory):

# Verificar si el directorio existe o no.
    if os.path.exists(apache_sites_directory) and os.path.isdir(apache_sites_directory):
        return True
    else:
        return False



# Definir la funcion para listar los sitios que existen en el directorio por default.
def list_apache_sites():
    path = '/etc/apache2/sites-available'

    if check_apache_sites_directory(path):
        
# Obtener la lista de archivos en el directorio de sitios por default.
        site_files = os.listdir(path)

        if site_files:
            print("Los sitios disonibles son:")

            for file_name in site_files:
                if file_name.endswith('.conf'):
                    site_name = file_name[:-5]
                    print("- ", site_name)
        else:
            print("No se encontraron sitios disponibles en Apache.")
    else:
        print("El directorio de sitios de Apache no existe.")
        sys.exit()



# Diccionario con mensajes de error
 
mensajes_error = {
 
    "err_no_command":"Debe ingresar un comando.",
    "err_invalid_command":"Debe ingresar un comando valido.",
    "err_no_servername":"Debe ingresar un nombre para el vhost."
 
 
}
 
 
 
# Lista con los comandos que utiliza este programa
 
 
comandos = [ 'newhost', 'modhost', 'delhost' ]
 
argumentos = sys.argv
 
# Validar que haya al menos un argumento pasado al script
 
if len(argumentos) < 2:
 
    print(mensajes_error["err_no_command"])
    exit(1)
 
if argumentos[1] in comandos:
    service_status = apache_service()
    print (service_status)

    list_apache_sites()

else:
 
    print(mensajes_error["err_invalid_command"])

if argumentos[1] == comandos[0]:
    
    if len(argumentos) < 3:
 
        print(mensajes_error["err_no_servername"])
        exit(1)
 
 
    # newhost
    #<VirtualHost *:80>
    #DocumentRoot /ruta/al/document/root
    #ServerName <servername>
    #</VirtualHost> 
    # Paramentros predeterminados
 
    puerto = 80
 
    server_name = argumentos[-1]
 
    document_root = f"/var/www/{server_name}"
 
 
    # Procesar parametros
 
    contador = 0
 
    for arg in argumentos:
 
        if arg == "-p":
 
            puerto = argumentos[contador + 1] 
 
 
        elif arg == "-d":
 
            document_root = argumentos[contador + 1]
 
        contador += 1
 
 
    output = f"<VirtualHost *:{puerto}>\n\n\tDocumentRoot {document_root}\n\tServerName {server_name}\n\n</VirtualHost>"
    
    print(output)
 
 
 
 
elif argumentos[1] == comandos[1]:
 
    print(argumentos[1])
 
else:
    print(argumentos[1])
 

 