import pandas as pd
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference

archiv_excel = pd.read_excel('supermarket_sales.xlsx')
# print(archiv_excel[['Gender', 'Product line', 'Total']])

table_pivote = archiv_excel.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

#print(table_pivote)

table_pivote.to_excel('sales_2022.xlsx', startrow=4, sheet_name='Report')



wb = load_workbook('sales_2022.xlsx')
pestania = wb['Report']
min_col = wb.active.min_column
max_col = wb.active.max_column
min_fila = wb.active.min_row
max_fila = wb.active.max_row

print(min_col)
print(max_col)

print(min_fila)
print(max_fila)

#Graficos
barchart = BarChart()


data = Reference(pestania, min_col=min_col+1, min_row=min_fila, max_col=max_col, max_row=max_fila)
categoria = Reference(pestania, min_col=min_col, min_row=min_fila +1, max_col=min_col, max_row=max_fila)

barchart.add_data(data, titles_from_data=True)
barchart.add_data(categoria)

pestania.add_chart(barchart, 'B12')
barchart.title = 'Ventas'
barchart.style = 5
wb.save('sales_2022.xlsx')

