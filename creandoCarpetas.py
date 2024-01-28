from pathlib import Path
import calendar

#Creando una carpeta
# Path('nueva_carpeta').mkdir()
# Path('nueva_carpeta').mkdir(exist_ok=True)

#Path('carpeta1/carpeta2/carpeta3').mkdir(parents=True, exist_ok=True)

meses_anio = list(calendar.month_name[1:])
dias_semana = ['Dia 1', 'Dia 10', 'Dia 20', 'Dia 30']

for i, mes in enumerate(meses_anio):
    for dia in dias_semana:
        Path(f'2022/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)




def main():
    pass




if __name__=='__main__':
    main()