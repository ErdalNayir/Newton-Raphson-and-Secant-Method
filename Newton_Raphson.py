# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:06:51 2021

@author: erdal
"""


from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr

def Newton_Raphson():


    x=int(input("İnitial value of X: "))
    denklem=str(input("Enter equation like (x*x+4*x+10): "))
    itr=int(input("Enter number of steps: "))
    print("\n\n")

    for i in range(1,itr+1):

    ### DEĞİŞKENLERİ OLUŞTURMA ###
        sonuç=0

        x_son=0

        trv_sonuç=0


    ### TÜREVSİZ DENLEMİN SONUCU ###

        sonuç=eval(denklem)

    ### TÜREV ALMA ###

        denklemim = parse_expr(denklem) # string halindeki denklemi parselleme

        trv_denklem=str(diff(denklemim)) # denlemin türevini alıp string halinde depolama

        trv_sonuç=eval(trv_denklem) # eval fonksiyonu ile türev sonucunu hesaplama

        x_son=x-sonuç/trv_sonuç  # Xi+1 i hesaplama

        print("{}.Step Xi+1= {} ".format(i,x_son)) # sonucu basma işlemi

        x=x_son  # x_son u x e atamak



def Secant():

    x=int(input("İnitial value of X0: "))
    x_eksi=int(input("İnitial value of X1: "))

    denklem=str(input("Enter equation like (x*x+4*x+10): "))
    itr=int(input("Enter number of steps: "))
    print("\n\n")



    for i in range(1,itr+1):

    ### DEĞİŞKENLERİ OLUŞTURMA ###

        x_depo=x

        sonuç=0

        sonuç_eksi=0

        x_son=0

    ### TÜREVSİZ DENLEMİN SONUCU ###

        sonuç=eval(denklem)

        x=x_eksi

        sonuç_eksi=eval(denklem)

        x_son= x_depo - sonuç*(x-x_depo)/(sonuç_eksi-sonuç)

        x=x_son

        x_eksi=x_depo

        print("{}.Step: Xi+1= {} ".format(i,x_son))



def Main():
    option = int(input("Secant(1)? or Newton_Raphson?(2)"))

    if option ==1:
        Secant()
    elif option ==2:
        Newton_Raphson()
    else:
        print("this option is not available!")


if __name__ == '__main__':
    Main()
