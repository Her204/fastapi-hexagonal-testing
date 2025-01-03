# crea un script que lea linea por linea el archivo requirements.txt y ejecute el comando pip3 install linea 
# si da error la linea debe continuar con la siguiente
# si no hay error debe imprimir un mensaje de exito
# si la linea no da error debe añadirse a un archivo requirements_instaladas.txt
# si la linea da error debe añadirse a un archivo requirements_no_instaladas.txt 
import os

def instalar_dependencias():
    with open('requirements.txt') as f:
        for linea in f:
            linea = linea.strip()
            try:
                result = os.system(f'pip3 install {linea}')
                if result == 0:
                    with open('requirements_instaladas.txt', 'a') as f_instaladas:
                        f_instaladas.write(linea + '\n')
                    print(f'{linea} instalada con exito')
                else:
                    with open('requirements_no_instaladas.txt', 'a') as f_no_instaladas:
                        f_no_instaladas.write(linea + '\n')
            except Exception as e:
                with open('requirements_no_instaladas.txt', 'a') as f_no_instaladas:
                    f_no_instaladas.write(linea + '\n')
                print(f'Error al instalar {linea}: {e}')


if __name__ == '__main__':
    instalar_dependencias()