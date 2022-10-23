import shutil
import os
#from difflib import SequenceMatcher
from jellyfish import damerau_levenshtein_distance as dldist
import numpy as np

INPUT2=r'C:\temp\DOWNLOAD_GDrive_69Gb-13mai2022_unzip_INPUT2'
INPUT0=r'C:\temp\SYNC_Gdrive_BIN_7out2022_181Gb_INPUT1' # ponto de partida se INPUT 1 começar mais abaixo nas pastas
INPUT1=r'C:\temp\SYNC_Gdrive_BIN_7out2022_181Gb_INPUT1'
#
OUTPUT=r'C:\temp\OUTPUT'
INPUT0=r'C:\temp\INPUT1' # just for reference if INPUT1 is under INPUT0
INPUT1=r'C:\temp\INPUT1'
INPUT2=r'C:\temp\INPUT2'

nameSmallFilesDirectory='SmallGFiles'
K=500 # kb
# log:
newFolders=[]
nonminMatches=[]
tooLong=[]
# all folders from INPUT1 and INPUT2
ALLFOLDERSINPUT1=[os.path.split(x[0])[1] for x in os.walk(INPUT1)] # just folder names, no path
ALLFOLDERSINPUT1FULL=[x[0] for x in os.walk(INPUT1)] # folder names with path
ALLFOLDERSINPUT2=[os.path.split(x[0])[1] for x in os.walk(INPUT2)] # just folder names, no path
ALLFOLDERSINPUT2FULL=[x[0] for x in os.walk(INPUT2)] # folder names with path
#substituir:
oldS='MANUEL_LAMEIRAS_DE_FIGUEIREDO_Campagnolo'
newS='MLC'
def myrepl(f):
  return f.replace(oldS,newS)

COPIAR=False # INPUT1 to OUTPUT
COPIAR2=False # INPUT2 to OUTPUT

# copy files from INPUT1 to OUTPUT
count=0
for FIN1, dirnames, files in os.walk(INPUT1):
  print(count)
  count+=1
  #print('FIN1',FIN1)
  FOUT=os.path.join(OUTPUT,os.path.relpath(FIN1,start=INPUT0))
  # create FOUT and identify FIN2 (if it exists)
  if not os.path.exists(FOUT) and len(dirnames)+len(files)>0 : 
    os.makedirs(FOUT)
    newFolders.append(FOUT)
    #print('create FOUT ', FOUT)
  # list all files in FIN1 smaller than K kb
  L=[f for f in files if os.path.getsize(os.path.join(FIN1, f)) < 500]
  #print(L)
  # move those files to new subfolder
  if len(L) >0:
    SF=os.path.join(FOUT, nameSmallFilesDirectory)
    if not os.path.exists(SF):
      os.mkdir(SF)
      newFolders.append(SF)
    for f in L:
      # copy2 preserves metadata
      if COPIAR: shutil.copy2(os.path.join(FIN1, f),os.path.join(FOUT, nameSmallFilesDirectory, myrepl(f)))
  # Copy remaining files from FIN1 to FOUT
  #FIN1files=[f for f in os.listdir(FIN1) if os.path.isfile(os.path.join(FIN1,f))]
  MINUSL=list(set(files).difference(set(L)))
  for f in MINUSL:
    if COPIAR: shutil.copy2(os.path.join(FIN1, f),os.path.join(FOUT, myrepl(f)))
  
  
# insert remaining files in INPUT2 in OUTPUT
count=0
FIN2=r'C:\temp\DOWNLOAD_GDrive_69Gb-13mai2022_unzip_INPUT2\pessoal\administrativo-casas-docs-impostos-bolsas-saude-escolas\administrativo-casa-bicas-carro\obras_casa'
# Determine existing folders in OUTPUT
ALLFOLDERSOUTPUT=[os.path.split(x[0])[1] for x in os.walk(OUTPUT)] # just folder names, no path
ALLFOLDERSOUTPUTFULL=[x[0] for x in os.walk(OUTPUT)] # folder names with path
# cycle through INPUT2
for FIN2, dirnames, FIN2files in os.walk(INPUT2):
  print(count)
  count+=1
  #print('FIN2',FIN2)
  # Determine FOUT where to insert files in FIN2
  shortFIN2=os.path.relpath(FIN2,start=INPUT2)
  #ratiosMatch=[SequenceMatcher(a=shortFIN2, b=os.path.relpath(FN,start=INPUT0)).ratio()  for FN in ALLFOLDERSINPUT1FULL]
  # determine folder in OUTPUT that is more similar to FIN2
  ratiosMatch=[dldist(shortFIN2, os.path.relpath(FN,start=OUTPUT))  for FN in ALLFOLDERSOUTPUTFULL]
  argminMatch=np.argmin(np.array(ratiosMatch))
  minMatch=np.min(np.array(ratiosMatch))
  if minMatch==0: 
    # FOUT exists
    FOUT=ALLFOLDERSOUTPUTFULL[argminMatch]
  if minMatch>0:
    FOUT=os.path.join(OUTPUT,shortFIN2) # main issue: it could be a different choice of FOUT
    FN=ALLFOLDERSOUTPUTFULL[argminMatch]
    shortFN=os.path.relpath(FN,start=OUTPUT)
    # if dldist(shortFIN2,shortFN)>0:
    #   print('diff',shortFIN2)
    #   print('diff',shortFN)
    #   print('diff',dldist(shortFIN2,shortFN))
    #   print('diff',FIN2)
    #   print('diff',FOUT)
    nonminMatches.append({shortFIN2: (minMatch ,shortFN)})
    if not os.path.exists(FOUT) and len(dirnames)+len(FIN2files)>0 : 
      os.makedirs(FOUT)
      newFolders.append(FOUT)
      #print('FOUT ', FOUT)
  # copy files if there are files to be copied (otherwise FOUT is not created) 
  if os.path.exists(FOUT):
    FOUTfiles=[f for f in os.listdir(FOUT) if os.path.isfile(os.path.join(FOUT,f))]
    MINUS=list(set(FIN2files).difference(set(FOUTfiles)))
    for f in MINUS:
      if len(os.path.join(FIN2, f))>259 or len(os.path.join(FOUT, f))>259: 
        # print('too long', FIN2)
        # print('too long', FOUT)
        tooLong.append(os.path.join(FIN2, f))
        tooLong.append(os.path.join(FOUT, f))
      else:
        #print('len minus',len(MINUS))
        if COPIAR2: shutil.copy2(os.path.join(FIN2, f),os.path.join(FOUT, myrepl(f)))

print('nonminMatches',nonminMatches)
print('tooLong',tooLong)

# 
# with open(r'C:\temp\newFolders.txt', 'w') as fp:
#   for item in newFolders:
#     fp.write('%s\n' % item)
# 
# len('C:\temp\OUTPUT\aulas\geomatica-sigdr-E-qgis3-em-portugues-E-PyQGIS\QGIS 3 em português\Dados para exercícios\Secção 6.2 - Representação cartográfica do relevo e modelos digitais de elevação\SmallGFiles')

# #len('C:\\temp\\INPUT2\\pessoal\\administrativo-casas-docs-impostos-bolsas-saude-escolas\\emma-isabel-henri-schools-grants\\emma-estudos-bolsas\\Crous-DSE\\demande-mars-2020\\copias-docs-isabel\\Copy of Bulletin_CAMPAGNOLO_Henri_T1-08-02-2007_MANUEL_LAMEIRAS_DE_FIGUEIREDO_Campagnolo__29965.pdf')
# a='pessoal\\documentos mo familiares\\livros-mo-h-portugal-paris\\alcobaca-apartamento-2021\\lombadas'
# b='pessoal\\documentos mo familiares\\livros-mo-h-portugal-paris\\alcobaca-apartamento-2021\\lombadas'
# dldist(a,b)
# 
# [len(x) for x in tooLong]
# before='administrativo-casas-docs-impostos-bolsas-saude-escolas\\emma-isabel-henri-schools-grants'
# after='oficial-HEMKI\\EIH-schools-grants\\LFCL'
# [len(x.replace(before,after)) for x in tooLong]
