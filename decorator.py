def new_decorator(func):
    def wrap_func():
        print('Code before executing func')
        func()
        print('func executed')
    return wrap_func
@new_decorator
def func_needs_decorator():
    print('This function is in need of decorator')

#func_needs_decorator=new_decorator(func_needs_decorator)
func_needs_decorator()
