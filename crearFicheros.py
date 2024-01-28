from pathlib import Path


numeros = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

# for i in numeros:
#     with open(f'test{i}.txt', 'w') as file:
#         file.write(f'Test {i}')


#Eliminar todos los archivos txt
# for path in Path('.').glob('*.txt'):
#     path.unlink()



#Eliminar todos los archivos txt a excepcion ade uno
for path in Path('.').glob('test[1-9].txt'):
    path.unlink()