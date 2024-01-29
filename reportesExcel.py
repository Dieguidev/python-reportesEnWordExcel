import pandas as pd
import openpyxl


archiv_excel = pd.read_excel('supermarket_sales.xlsx')
# print(archiv_excel[['Gender', 'Product line', 'Total']])

table_pivote = archiv_excel.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

print(table_pivote)

table_pivote.to_excel('sales_2022.xlsx', startrow=4, sheet_name='Report')