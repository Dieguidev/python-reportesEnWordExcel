from pathlib import Path



folder = Path('extensiones')

#Pasar de txt a csv
# for path in list(folder.iterdir()):
#     if path.suffix == '.txt':
#         new_path = path.with_suffix('.csv')
#         path.rename(new_path)



#Pasar de csv a txt
for path in folder.glob('**/*.csv'):
    new_path = path.with_suffix('.txt')
    path.rename(new_path)