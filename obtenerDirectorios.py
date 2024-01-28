from pathlib import Path

# Obtener path de todas las subcarpetas
carpeta = Path('test2')
# paths = carpeta.glob('**/*')
# for p in paths:
#     print(p)


#Obtener archivos con extension en especifico
# for p in carpeta.glob('**/*.html'):
#     print(p)


# Mostrar solo los que tengan archivos dentro de las carpetas
paths = carpeta.glob('**/*')
for p in paths:
    if p.is_file():
        print(f'el archivo encontrado es {p}')
    else:
        print(p, 'No tiene archivos')