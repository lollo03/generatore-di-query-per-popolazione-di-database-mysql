from random import randint, uniform, randrange
from datetime import timedelta, datetime
nomi = open("nomi.txt").read().split()
cognomi = open("cognomi.txt").read().split("\n")
vie =  open("vie.txt").read().split("\n")

class intero:
    def __init__(self, max, min=0):
        self.max = max
        self.x = 0
        self.min = min
    
    def genera(self):
        self.x = randint(self.min, self.max+1)
        return self.x
    
class decimale:
    def __init__(self, max, min=0,decimali=2):
        self.max = max
        self.x = 0
        self.decimali = decimali
        self.min = min
    
    def genera(self):
        self.x = round(uniform(self.min, self.max+1), self.decimali)
        return self.x

class nome:    
    def genera(self):
        self.valore = nomi[randint(0, len(nomi)-1)].split(",")[0].lower()
        return '"' + self.valore + '"'

class cognome:    
    def genera(self):
        self.valore = cognomi[randint(0, len(cognomi)-1)]
        return '"' + self.valore + '"'

class data:
    def __init__(self, min=2019, max=2021):
        self.max = str(max)
        self.min = str(min)

    def genera(self):
        mass = datetime.strptime(self.max, '%Y') #codice che gentilmente preso in prestito da stackoverflow
        minim = datetime.strptime(self.min, '%Y') 
        delta = mass - minim
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        self.valore = minim + timedelta(seconds=random_second)
        self.valore = self.valore.strftime("%Y-%m-%d")
        return '"' + self.valore + '"'

class dataora:
    def __init__(self, min=2019, max=2021):
        self.max = str(max)
        self.min = str(min)

    def genera(self):
        mass = datetime.strptime(self.max, '%Y') 
        minim = datetime.strptime(self.min, '%Y') 
        delta = mass - minim
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        self.valore = minim + timedelta(seconds=random_second)
        self.valore = self.valore.strftime("%Y-%m-%d %H:%M:%S")
        return '"' + self.valore + '"'
    
class sequenzaInteri:
    def __init__(self, max, min=0):
        self.max = max
        self.min = min
        self.x = min-1

    def genera(self):
        self.x += 1
        if self.x > self.max:
            self.x = self.min
        return self.x
    
class sequenzaStringhe:
    def __init__(self, arr):
        self.arr = arr
        self.x = -1

    def genera(self):
        self.x += 1
        if self.x > len(self.arr)-1:
            self.x = 0
        return '"' + self.arr[self.x] + '"'

class randomStringhe:
    def __init__(self, arr):
        self.arr = arr

    def genera(self):
        return '"' + self.arr[randint(0, len(self.arr)-1)] + '"'

class indirizzo:
    def genera(self):
        casi = ["Via ", "Viale ", "Piazza "]
        return casi[randint(0, len(casi)-1)] + vie[randint(0, len(vie)-1)]

class telefono:
    def __init__(self, fisso=False):
        self.fisso = fisso

    def genera(self):
        if self.fisso == False:
            return str(randint(320, 396)) + str(randint(1000000, 9999999))
        else:
            return "0" + str(randint(10000000, 99999999))



def generaQuery(struttura, iterazioni, tabella, campi):
    query = "insert into " + tabella + " (" + campi + ") values"
    for x in range(iterazioni):
        query += "("
        for i in struttura:
            if i == struttura[-1]:
                query += str(i.genera()) + ""
            else:
                query += str(i.genera()) + ", "
        if x == iterazioni-1:
            query += ");"
        else:
            query += "), "
    return query

