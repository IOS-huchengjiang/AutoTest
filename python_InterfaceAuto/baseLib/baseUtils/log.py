import functools
class logging(object):
    def __init__(self, level='INFO', desc=None):
        self.level = level
        self.desc = desc

    def __call__(self, func):  # 接受函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level,func=func.__name__))
            print("{desc}>>>>>>开始".format(desc=self.desc))
            funReturn = func(*args, **kwargs)
            print("{desc}<<<<<<完成".format(desc=self.desc))
            if isinstance(funReturn, dict):
                for key, value in funReturn.items():
                    print("[{key}]:{value}".format(key = key, value = value))
            # else:
            #     print('非字典类型不打印结果')
            return funReturn
        return wrapper  # 返回函数

# @logging(level='INFO')
# def say(something):
#     print("say {}!".format(something))

# def say(something):
#     print("say {}!".format(something))


# class logging(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("[DEBUG]: enter function {func}()".format(func=self.func.__name__))
#         return self.func(*args, **kwargs)
# @logging(level='INFO')
# def say(something):
#     print("say {}!".format(something))
#     return 'a'
#
# a = say('0k')
# print(a)
