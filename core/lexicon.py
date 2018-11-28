import os
import sys
from plex import *

lexico = Lexicon([
    (Rep1(Any(" \t\n")), IGNORE),
    (Str("file"),      "Result"),
    (Range("09"), IGNORE),
    (Rep1(Any(" \t\n")), IGNORE)
])

def ls(db = '.'):
    dir, subdirs, archivos = next(os.walk(db))
    print('Actual: ', dir)
    print('Subdirectorios: ', subdirs)
    print('Archivos: ', archivos )
    return archivos

def scanFile(dirFile):
    currentFile = open(dirFile,'r')
    scanner = Scanner(lexico, currentFile, file)
    #print scanner.position()
    while 1:
        token = scanner.read()
        print (token)    
        if token[0] is None:
            print ('Archivo descartado')
            break


db = ls('./db/')

for file in db:
    currentFile = open('./db/'+file,'r')
    scanner = Scanner(lexico, currentFile, file)
    #print scanner.position()
    while 1:
        token = scanner.read()
        print (token)     
        if token[0] is None:
            print ('Archivo descartado')
            break
    print(file)

'''
from os import listdir
def ls(ruta = '.'):
    return listdir(ruta)


------
from os import walk

def ls(ruta = '.'):
    return next(walk(ruta))[2]

def ls(ruta = '.'):
    dir, subdirs, archivos = next(walk(ruta))
    print('Actual: ', dir)
    print('Subdirectorios: ', subdirs)
    print('Archivos: ', archivos )
    return archivos

'''