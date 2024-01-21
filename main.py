import pandas as pd



NOTAS_ALUMNOS_PATH=r'./inputs/Notas_Alumnos.xlsx'

print(NOTAS_ALUMNOS_PATH)


def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')
    for index, row in excel_df.iterrows():
        print(index, row['NOMBRE'], row['NOTA T1'])
    

if __name__=='__main__':
    main()










