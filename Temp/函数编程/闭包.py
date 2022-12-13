# 嵌套函数中，内部函数可以访问外部函数的局部变量、参数，被外部函数之外调用时，就会形成闭包
# 闭包的意义，返回的函数对象，不仅仅是一个函数对象，在该函数之外还包裹了一层作用域，使得该函数无论在何处调用。优先使用自己外层包裹的作用域

def outer():
    name = "哈哈哈"

    def innter():
        print("innter", name)

    return innter


# 返回innter的内存地址
print(outer())
