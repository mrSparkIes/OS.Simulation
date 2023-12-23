class Disk():
    def __init__(self,price,space,type):
        self.price = price
        self.space = space
        self.type = type

class GPU():
    def __init__(self,name,price,brand,tracing,memory):
        self.name = name
        self.price = price
        self.brand = brand
        self.tracing = tracing
        self.memory = memory

class CPU():
    def __init__(self,name,brand,price, cores, hz):
        self.name = name
        self.brand = brand
        self.price = price
        self.cores = cores
        self.hz = hz

class Ram():
    def __init__(self,name,brand,price,memory):
        self.name = name
        self.brand = brand
        self.price = price
        self.memory = memory

#  ----------------------------------------------------------------------------  #

class D1(Disk):
    def __init__(self, price,space,type):
        super().__init__(price,space,type)
        self.price = 49
        self.space = 64000
        self.type = 'M.2'
class D2(Disk):
    def __init__(self, price, space, type):
        super().__init__(price, space, type)
        self.price = 92
        self.space = 128000
        self.type = 'M.2'
class D3(Disk):
    def __init__(self, price, space, type):
        super().__init__(price, space, type)
        self.price = 170
        self.space = 940000
        self.type = 'M.3'

#  ----------------------------------------------------------------------------  #

class G1(GPU):
    def __init__(self, price, name, brand, tracing, memory):
        super().__init__(price, name, brand, tracing, memory)
        self.name = 'NVIDIA GTX 1660'
        self.price = 130
        self.brand = 'NVidia'
        self.tracing = 'Partial'
        self.memory = 6400
class G2(GPU):
    def __init__(self, name, price, brand, tracing, memory):
        super().__init__(name, price, brand, tracing, memory)
        self.name = 'NVIDIA RTX 2080 Super'
        self.price = 170
        self.brand = 'NVidia'
        self.tracing = 'Full'
        self.memory = 8200
class G3(GPU):
    def __init__(self, name, price, brand, tracing, memory):
        super().__init__(name, price, brand, tracing, memory)
        self.name = 'NVIDIA RTX 3090 Ti'
        self.price = 240
        self.brand = 'Nvidia'
        self.tracing = 'Full'
        self.memory - 12800

#  ----------------------------------------------------------------------------  #

class C1(CPU):
    def __init__(self, name, brand, price, cores, hz):
        super().__init__(name, brand, price, cores, hz)
        self.name = 'Intel Core i5 13600K'
        self.brand = 'Intel'
        self.price = 70
        self.cores = 12
        self.hz = 3.8
class C2(CPU):
    def __init__(self, name, brand, price, cores, hz):
        super().__init__(name, brand, price, cores, hz)
        self.name = 'Intel Core i7 13400K'
        self.brand = 'Intel'
        self.price = 114
        self.cores = 14
        self.hz = 4.2
class C3(CPU):
    def __init__(self, name, brand, price, cores, hz):
        super().__init__(name, brand, price, cores, hz)
        self.name = 'Intel Core i9 13200KF'
        self.brand = 'Intel'
        self.price = 144
        self.cores = 16
        self.hz = 4.6

#  ----------------------------------------------------------------------------  #

class M1(Ram):
    def __init__(self, name, brand, price, memory):
        super().__init__(name, brand, price, memory)
        self.name = 'Ramify | DDR4 8Gb RAM'
        self.brand = 'Ramify'
        self.price = 32
        self.memory = 8196
class M2(Ram):
    def __init__(self, name, brand, price, memory):
        super().__init__(name, brand, price, memory)
        self.name = 'Ramify | DDR4 16Gb RAM'
        self.brand = 'Ramify'
        self.price = 48
        self.memory = 16382
class M3(Ram):
    def __init__(self, name, brand, price, memory):
        super().__init__(name, brand, price, memory)
        self.name = 'Ramify | DDR4 32Gb RAM'
        self.brand = 'Ramify'
        self.price = 64
        self.memory = 32764


#  ----------------------------------------------------------------------------  #

#  ----------------------------------------------------------------------------  #

d1S = 'Disk Name: XMPLv1 M.2 Data Drive\nDisk Type: M.2\nPrice: 49$\nDisk Space: 64 GB'
d2S = 'Disk Name: XMPLv2 M.2 Data Drive\nDisk Type: M.2\nPrice: 92$\nDisk Space: 128 GB'
d3S = 'Disk Name: XMPLv2.5 M.3 Data Drive\nDisk Type: M.3\nPrice: 170$\nDisk Space: 940 GB'