# 在一个类里，实现了__enter__和__exit__的方法，这个类的实例就是一个上下文管理器

class Resource:
    def __enter__(self):
        print('===connect to resource===')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('===close resource connection===')

    def operate(self):
        print('===in operation===')


with Resource() as res:
    res.operate()
