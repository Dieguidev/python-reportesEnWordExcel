import pandas as pd



NOTAS_ALUMNOS_PATH=r'./inputs/Notas_Alumnos.xlsx'

print(NOTAS_ALUMNOS_PATH)


def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH)

if __name__=='__main__':
    main()










