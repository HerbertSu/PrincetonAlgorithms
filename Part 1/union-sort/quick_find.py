class QuickFindUF():
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, newId):
        self.__id = newId
        return

    def quickFindUF(self, N):
        self.__id = ([None]*N)
        i = 0
        for element in self.__id:
            self.__id[i] = i
            i += 1

    def connected(self, p, q):
        if self.__id[p] == self.__id[q]:
            return True
        else:
            return False
    
    def union(self, p, q):
        pid = self.__id[int(p)]
        i = 0
        for element in self.__id:
            print(pid)
            print(element)
            if element == pid:
                print("inside")
                self.__id[i] = self.__id[int(q)]
                print(self.__id[int(q)])
            else:
                pass
            i += 1

obj = QuickFindUF([])
obj.quickFindUF(10)
obj.connected(1,2)
obj.union(1,2)
obj.connected(1,2)




print(obj.get_id())


# class Phone():

#     def __init__(self, brand, price, camera):
#         self.__brand = brand
#         self.__price = price
#         self.__camera = camera
    
#     def buy(self):
#         print("bought")
    
#     def refund(self):
#         pass

# class SmartPhone(Phone):

#     def __init__(self, brand, price, camera, os, ram, battery):
#         self.__os = os
#         self.__ram = ram
#         self.__battery = battery
#         super().__init__(brand, price, camera)
    
#     def insure(self):
#         pass


# class RegularPhone(Phone):

#     def __init__(self, brand, price, camera, type):
#         self.__type = type
#         super().__init__(brand, price, camera)

#     def buy(self):
#         super().buy()
#         print("bought again!")

#     def exchange(self):
#         pass

