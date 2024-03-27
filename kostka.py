#!/usr/bin/env python3
#Kryštofův code

import random
class Kostka:

    def __init__(self, pocet_sten):
        try:
            self.setPocetSten(pocet_sten)
        except:
            print("Chyba v poctu sten")

    def hod(self):
        return random.randint(1, self.__pocetSten)

    def getPocetSten(self):
        return self.__pocetSten

    def setPocetSten(self, pocet_sten):
        if pocet_sten > 0:
            self.__pocetSten = pocet_sten
        else:
            print(f"Pocet sten musí být > 0, ponechavam: {self.__pocetSten}")

k1 = Kostka(6)
print(k1.hod())

k2 = Kostka(12)
print(k2.hod())

print(k1.getPocetSten())
k1.setPocetSten(-5)