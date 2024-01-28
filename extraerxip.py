from pathlib import Path
import zipfile


directorio_actual = Path('.')
directorio_objetivo = Path('temp')

for path in directorio_actual.glob('*.zip'):
    with zipfile.ZipFile(path, 'r') as zipObj:
        zipObj.extractall(path=directorio_objetivo)
        print(f'Se ha extraido el archivo {path.name}')