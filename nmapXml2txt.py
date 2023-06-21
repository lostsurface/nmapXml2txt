#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET

# Obtener el nombre del archivo XML como argumento de línea de comandos
if len(sys.argv) < 2:
    print("Debe proporcionar el nombre del archivo XML como argumento.")
    sys.exit(1)

xml_file = sys.argv[1]

# Cargar el archivo XML
try:
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Recorrer los elementos 'host' en el XML
    for host in root.findall('.//host'):
        # Obtener la dirección IP del host
        ip = host.find('.//address').get('addr')

        # Recorrer los elementos 'port' dentro del host
        for port in host.findall('.//port'):
            # Obtener el número de puerto y el estado
            port_number = port.get('portid')
            state = port.find('state').get('state')

            # Si el estado es 'open', imprimir la combinación de IP y puerto
            if state == 'open':
                print(f'{ip}:{port_number}')

except IOError:
    print(f"No se pudo abrir el archivo '{xml_file}'. Verifica el nombre y la ruta.")
