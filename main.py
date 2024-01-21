import pandas as pd



NOTAS_ALUMNOS_PATH=r'./inputs/Notas_Alumnos.xlsx'

print(NOTAS_ALUMNOS_PATH)


def main():
    #* Lee el archivo Excel y carga los datos en un DataFrame usando pandas
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')

    #* Itera sobre cada fila del DataFrame
    for index, row in excel_df.iterrows():
        #* Imprime el índice de la fila, el valor de la columna 'NOMBRE' y el valor de la columna 'NOTA T1'
        print(index, row['NOMBRE'], row['NOTA T1'])
        
    
    asig_list = list(excel_df['ASIGNATURA'].drop_duplicates())
    print(asig_list)
    

if __name__=='__main__':
    main()










