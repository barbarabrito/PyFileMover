import os
import sys
import os.path
import shutil

print("Você está no diretório "+os.getcwd())

nomepasta = input("Digite o nome da pasta que contém os arquivos .py: ")
pastafinal = input("Digite o nome da pasta destino: ")
print("")

if os.path.isdir(pastafinal) == False:
   os.mkdir(pastafinal)
else:
   print("")
   print("Diretório já existe. Nenhum diretório novo foi criado.\n")
   
cont =0
for root, dirs, files in os.walk(nomepasta):
   for name in files:
      if ".py" in name:
         cont = cont + 1
         sdir = os.path.abspath(os.path.join(root, name))
         shutil.move(sdir, pastafinal)
         print(sdir)
         print("")         
print("Os %d arquivos acima foram removidos deste diretorio" % cont)


