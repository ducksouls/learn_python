'''
@description: 
@param: 
@return: 
'''
'''
@description: 
@param: 
@return: 
'''
# lambda 表达式的分析 
'''
其实也就是个函数，
def noname(参数):
    return 对参数的操作
'''
a = {'1':1,'eglish':2,'age':3}
b = lambda c: c['eglish']
print(b(a))

d = lambda x: print(x) 
print(d('shit')) #shit表达式中的内容 --- none 因为表达式没有返回值