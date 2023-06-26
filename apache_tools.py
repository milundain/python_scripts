#!/bin/python3
 
# Importar libreria para capturar argumentos pasados al script.
 
import sys
 
 
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
 
 
if argumentos[1] == comandos[0]:
    
    if len(argumentos) < 3:
 
        print(mensajes_error["err_no_servername"])
        exit(1)
    # newhost
 
    #<VirtualHost *:80>
 
    #   DocumentRoot /ruta/al/document/root
    #   ServerName <servername>
 
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
 
elif argumentos[1] == comandos[2]:
 
    print(argumentos[1])
 
else:
 
    print(mensajes_error["err_invalid_command"])
 