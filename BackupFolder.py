import subprocess
import os
import datetime

def move(in_dir,out_dir): #mover o diretório de backup
    rotina = ["mv",in_dir,out_dir]# usando Bash
    processo = subprocess.run(rotina)

def rename(in_dir):
    week = datetime.date.today().strftime("%W") #recebendo a semana
    newName_dir = "<Informando caminho com o novo nome da pasta>" + week #renomeando adicionando a semana
    rename = ["mv",in_dir,newName_dir]# usando Bash
    processo = subprocess.run(rename)
    return newName_dir #retornando o novo nome da pasta

def newBackup():
    path = "<informar o caminho com o nome da pasta>" #Criando uma nova pasta backup
    try:
        os.mkdir(path) #criando a pasta se não existir
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)


in_dir = "<caminho da pasta de origem>"#"pasta a copiar"
newDir = rename(in_dir)

out_dir = "<informar o caminho de destino>"#"local de destino"
move(newDir,out_dir)

newBackup()
