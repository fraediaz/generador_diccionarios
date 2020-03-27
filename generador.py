#-*- coding:utf-8 -*-
#!/usr/bin/python3
import random

numeros     =   '0123456789'
letras      =   'abcdefghijklmnñopqrstuvwxyz'
letrasM     =   'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

conf        = numeros + letrasM + letras

def combinar(ejemplo, veces=1):
    print(ejemplo)
    for y  in range(veces):
        contador=0
        clave = ''
        van = {}
        for x in ejemplo:
            contador = contador+1
            if x != '*':
                van.update(
                    {
                        str(contador):x
                    }
                )
        for x in range(len(ejemplo)):º
            texto = random.choice(conf)
            clave = clave+texto
        for x in van:
            clave=clave.replace((clave[int(x)-1]), van.get(x),1)
        print(clave)
print('\n'*90)
print('\n'*2)
print('Ingresa una palabra, asteriscos serán aleatorios, sino constante.\nE*J*E*M*P*L*O ==> ERJNE9M3PFLTO\nEJEMPLO****** ==> EJEMPLO7HGTEN')
palabra = str(input('Ingresa palabra base : '))
print('\n'*3)
veces   = int(input('Cuantas veces? : '))
combinar(palabra, veces)