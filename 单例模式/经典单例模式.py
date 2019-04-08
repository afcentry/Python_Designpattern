#coding:utf-8

class Singleton(object):

    def __new__(cls, *args, **kwargs):
        # 查看对象cls是否具有instance属性
        if not hasattr(cls, "instance"):
            # 创建当前类的实例对象
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created:",s)

s1 = Singleton()
print("Object created:",s1)