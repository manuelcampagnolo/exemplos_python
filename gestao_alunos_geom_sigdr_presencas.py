import pandas as pd
import os
import numpy as np
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime


########################################################################### functions (não usado)

def df_to_excel(df, ws, header=True, index=True, startrow=0, startcol=0):
    """Write DataFrame df to openpyxl worksheet ws"""
    rows = dataframe_to_rows(df, header=header, index=index)
    for r_idx, row in enumerate(rows, startrow + 1):
        for c_idx, value in enumerate(row, startcol + 1):
             ws.cell(row=r_idx, column=c_idx).value = value

############################################################################ inputs
xls_alunos_geom="students_1696_Geomática.2023-04-07_06-45-03_472.xlsx"
xls_alunos_sigdr="students_1761_Sistemas_de_Informação_Geográfica_e_Detecção_Remota.2023-04-07_06-45-28_144.xlsx"
xls_presencas="presencas_2022_2023_v2.xlsx"

# resultados 2022
df_2022=pd.read_csv('Pauta_apos_3a_chamada_6_julho_2022.csv',delimiter=';', encoding = 'unicode_escape')
df_2022.columns
vars_2022=['Número', 'Trab_2019-2020', 'Trab_2020-2021','Trab_2021_2022', 'Frequência']

# presenças/frequência 2022-2023
x1 = openpyxl.load_workbook(xls_presencas)
data = x1.active.values
columns = next(data)[0:]
df_pres=pd.DataFrame(data, columns=columns)
#df_pres=pd.read_csv('presencas_2022_2023_v2_10mar.csv',delimiter=';', encoding = 'unicode_escape')
df_pres.columns
vars_pres=['Número', 'Turma', 'GRUPO','Unidade 1', 'unidade 2', 'unidade 3']
df_pres['Unidade 1'].fillna('0', inplace=True)
print('unique values: ',df_pres['Unidade 1'].unique())
vals_unidade_sim=['sim', 'Sim','1']
[x for x in df_pres['Unidade 1'] if x in vals_unidade_sim]
vals_unidade_nao=['\xa0','0']
[x for x in df_pres['Unidade 1'] if x in vals_unidade_nao]

# ler lista alunos fenix 2022-2023
x1 = openpyxl.load_workbook(xls_alunos_geom) #, encoding='iso-8859-1')
x2 = openpyxl.load_workbook(xls_alunos_sigdr) #, encoding='iso-8859-1')
# converter para dataframe
data = x1.active.values
# Get the first line in file as a header line
columns = next(data)[0:]
# Create a DataFrame based on the second and subsequent lines of data
df1=pd.DataFrame(data, columns=columns)
data = x2.active.values
columns = next(data)[0:]
df2=pd.DataFrame(data, columns=columns)
df_insc=pd.concat([df1, df2], axis=0) 
df_insc['Número'] = df_insc['Número'].astype('int')
vars_insc=['Número', 'Nome','Estatutos']

############################################################################################
# criar tabela com todos os alunos inscritos com colunas:
# ['Número', 'Nome','Estatutos',"ano_frequencia", "nota_trabalho", unidade1, unidade2, unidade3, turma, grupo]
df_insc.columns
df_2022.columns
df=df_insc[vars_insc].merge(df_2022[vars_2022], how='left',on='Número')
df=df.merge(df_pres[vars_pres], how='left',on='Número')
df['Turma']=df['Turma'].astype('string')
# exportar para Excel
df.sort_values(by='Turma').to_excel('alunos_estado_'+datetime.today().strftime('%Y-%m-%d')+'nao_editar.xlsx')

'''
# alunos 2022-2023
#print(df_geom.head()) # Número       Nome     Email   Email Institucional  ... Nº Inscrições  Tipo Inscrição
df_geom=pd.read_csv(os.path.join(path,'students_1696_Geomatica.2023-03-10_07-20-18_469_10mar.csv'),delimiter=';', encoding = 'unicode_escape')
df_sigdr=pd.read_csv(os.path.join(path,'students_SIGDR_2023-03-10_07-20-51_162.csv'),delimiter=';', encoding = 'unicode_escape')
print('número inscritos: ',df_geom.shape[0], df_sigdr.shape[0])
df_insc=pd.concat([df_geom,df_sigdr])


print(df_2022.head()) # Número GrupoTurma  Trab_2019-2020  Trab_2020-2021  Trab_2021_2022  Nota trabalho ... Frequência ... Resultado
print(df_2022.isna().sum())
sum(df_2022.Frequência=='Frequência') # 170

#Criar lista de alunos de 2022_2023 que ainda não têm frequência
# Alunos de 2023 - os que têm frequência de 2022

df=df_insc[vars_insc].copy()
# alunos inscritos com estatuto especial
df[~df.Estatutos.isna()]

L=[]
for i in range(df.shape[0]):
    if df['Número'].iloc[i] not in df_2022[df_2022.Frequência=='Frequência']['Número']: 
        L.append(df['Número'].iloc[i])

print(len(L), df.shape[0])
'''
