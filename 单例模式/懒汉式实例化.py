#coding:utf-8

class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("init方法被调用")
        else:
            print("实例对象已经被创建",self.getinstancec())

    @staticmethod
    def getinstance(cls):
        if not Singleton.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton() # 类实例化，但不创建类对象
print(s.getinstance())
s1 = Singleton()
