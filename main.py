import pandas as pd
import sys
from docxtpl import DocxTemplate

#excel 
NOTAS_ALUMNOS_PATH=r'./inputs/Notas_Alumnos.xlsx'

#word
NOTAS_ALUMNOS_PATH_WORD=r'./inputs/Plantilla_Notas.docx'
PATH_OUTPUT_WORD=r'./outputs'


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


# Función que realiza la detección de errores en un DataFrame
def deteccionErrores(df):
    
    err1, err2, err3 = False, False, False
    
    # Obtén la lista de nombres de alumnos ordenada y sin duplicados
    alumnos_list = sorted(list(df['NOMBRE'].drop_duplicates()))

    # Obtén la lista de asignaturas ordenada y sin duplicados
    asignatura_list = sorted(list(df['ASIGNATURA'].drop_duplicates()))

    # Itera sobre cada alumno y asignatura
    for alum in alumnos_list:
        for asig in asignatura_list:
            # Filtra el DataFrame para obtener las filas correspondientes al alumno y asignatura actual
            filt_al_as_df = df[(df['NOMBRE'] == alum) & (df['ASIGNATURA'] == asig)]

            

            # Verifica si no hay notas para el alumno y asignatura actual
            if len(filt_al_as_df) == 0:
                print(f'No hay notas para el alumno {alum} y la asignatura {asig}')
                err1 = True
            # Verifica si hay más de una nota para el alumno y asignatura actual
            elif len(filt_al_as_df) > 1:
                print(f'Hay más de una nota para el alumno {alum} y la asignatura {asig}')
                err2 = True
        
        
        # Itera sobre cada fila del DataFrame
        for index, row in df.iterrows():
            trimestre_list = ['NOTA T1', 'NOTA T2', 'NOTA T3']
            # Itera sobre cada trimestre
            for trimestre in trimestre_list:
                # Verifica si la nota para el trimestre actual no está en el rango [0.0, 10.0]
                if not((row[trimestre] >= 0.0) and (row[trimestre] <= 10.0)):
                    print(f'La nota {row[trimestre]} no es válida para el trimestre {trimestre}')
                    err3 = True

        if err1 or err2 or err3:
            print('')
            print('Se encontraron errores en el DataFrame:')
            sys.exit(1)
        else:
            print('')
            print('No se encontraron errores en el DataFrame.')
            sys.exit(0)



def main():
    
    #Cargar documento
    docs_tpl = DocxTemplate(NOTAS_ALUMNOS_PATH_WORD)
    
    #Context
    context = {
        'curso': '2021/2022',
        'nombre_alumno': 'Juan Pérez',
        'clase': '4-C'
    }
    #Renderizar el word
    docs_tpl.render(context)
    #Guardar el word
    docs_tpl.save(f'{PATH_OUTPUT_WORD}/Notas_Alumnos.docx')
        
    
    
    
    # Lee el archivo Excel y carga los datos en un DataFrame usando pandas
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')

    # Itera sobre cada fila del DataFrame
    for index, row in excel_df.iterrows():
        # Imprime el índice de la fila, el valor de la columna 'NOMBRE' y el valor de la columna 'NOTA T1'
        print(index, row['NOMBRE'], row['NOTA T1'])
        
        
    # Crea una lista de asignaturas únicas en el DataFrame las ordena y la imprime
    asig_list = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))
    # print(asig_list)
    
    
    # Crea una lista vacía para almacenar los valores de las columnas 'ASIGNATURA'
    filter_td_asig = []
    
    # Itera sobre cada asignatura en la lista
    for item in asig_list:
        # Obtiene el valor de la columna 'ASIGNATURA' correspondiente a la asignatura actual
        valorTd = dict_asig[item]
        # Agrega el valor a la lista
        filter_td_asig.append(valorTd)
    print('')
    
    deteccionErrores(excel_df)
    

if __name__=='__main__':
    main()










