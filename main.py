import pandas as pd



NOTAS_ALUMNOS_PATH=r'./inputs/Notas_Alumnos.xlsx'
print(NOTAS_ALUMNOS_PATH)


dict_asig = {
    'LENGUA CASTELLANA Y LITERATURA':   'Lengua Castellana y Literatura',
    'BIOLOGIA':                         'Biología',
    'GEOGRAFIA E HISTORIA':             'Geografía e Historia',
    'MATEMATICAS':                      'Matemáticas',
    'INGLES':                           'Inglés',
    'EDUCACION FISICA':                 'Educación Física',
    'ETICA':                            'Ética',
    'CULTURA CLASICA':                  'Cultura clásica',
    'MUSICA':                           'Música',
    'TECNOLOGIA':                       'Tecnología',
    'EDUCACION PLASTICA':               'Educación Plástica',
    'FRANCES':                          'Francés',
}


def main():
    # Lee el archivo Excel y carga los datos en un DataFrame usando pandas
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')

    # Itera sobre cada fila del DataFrame
    for index, row in excel_df.iterrows():
        # Imprime el índice de la fila, el valor de la columna 'NOMBRE' y el valor de la columna 'NOTA T1'
        print(index, row['NOMBRE'], row['NOTA T1'])
        
        
    # Crea una lista de asignaturas únicas en el DataFrame las ordena y la imprime
    asig_list = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))
    print(asig_list)
    
    
    # Crea una lista vacía para almacenar los valores de las columnas 'ASIGNATURA'
    filter_td_asig = []
    
    # Itera sobre cada asignatura en la lista
    for item in asig_list:
        # Obtiene el valor de la columna 'ASIGNATURA' correspondiente a la asignatura actual
        valorTd = dict_asig[item]
        # Agrega el valor a la lista
        filter_td_asig.append(valorTd)
    print(filter_td_asig)
    

if __name__=='__main__':
    main()










