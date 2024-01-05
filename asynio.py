# https://youtu.be/qeOcZiSp3tE
# a = lambda x: x*x
# a(3)
    
# print(a(3))

# def square(x):
#     return x*x
# print(square(3))

# i_value = "apples"
# i_object = iter(i_value)

# while True:
    
#     item = next(i_object)
#     print(item)
# Except: StopIteration
# print("no more")

# i_value = "apples"
# i_value2 = [1, 2, 3, 4, 5]
# i_object = iter(i_value)
# i_object2 = iter(i_value2)

# while True:
    
#     item = next(i_object2)
#     print(item)
# Except: StopIteration
# print("no more")

'''def foo(input):
    res =[]
    for i in input:
        res.append(i*i)
        return res'''
    
# def foo(input):
    
#     for i in input:
#         yield(i*i)

# def cube(num):
#     res = []
#     for i in num:
#         res.append(i*i*i)
#     return res
# bar = cube([1,2,3,4,5])
# print(bar)

# def cube(num):
    
#     for i in num:
#      yield(i*i*i)
# bar = cube([1,2,3,4,5])
# print(next(bar))
# print(next(bar))
# print(next(bar))
# print(next(bar))
# print(next(bar))

# def genFun():
#     yield 10
#     yield 20
#     yield 30
# for i in genFun():
#      print(i)

#(The Yield keyword in Python is similar 
# to a return statement used for returning
# values or objects in Python)

#You can create a generator function using the generator() and yield keywords. Consider the example below.

# def generator():

#    yield "Welcome"

#    yield "to"

#    yield "Simplilearn"


# gen_object = generator()

# print(type(gen_object))

# for i in gen_object:

#    print(i)

# def genFun2():
#     yield 100
#     yield True
#     yield ("michel")
# try:
#   scrap = genFun2()
#   print(next(scrap))
#   print(next(scrap))
#   print(next(scrap))
  
# except StopIteration:
#     print('enough last iteration')


# def addNum(num):
#     for i in num:
#         yield(i+i)
        
# foo = addNum([7, 2])
# try:
#  print(next(foo))
#  print(next(foo)) 
#  print(next(foo))
# except StopIteration:
#    print('too many iterations') 

# def outer_func():
#     text = "hello from outer function" 
    
#     def inner_func():
#         print(text)
#     inner_func()
# outer_func()     

# def outer_func():
#     text = "hello from outer function" 
    
#     def inner_func():
#         print(text)
#     return inner_func
# batman = outer_func()
# print(batman)
# print(batman.__name__)







# def outer_func(name):
#     text = name

#     def inner_func():
#         print(text)
#     return inner_func

# batman = outer_func('rita josephine')
# spiderman = outer_func('michel')
# batman()
# spiderman()
import asyncio
# async def main():
#     print('../hehoo')
#     await asyncio.sleep(2)
#     print('...world')
#     await asyncio.sleep(3)
#     print('the end')

# asyncio.run(main())
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(2)
    print('... World!')
    await asyncio.sleep(3)
    print('...rita jose')
    await asyncio.sleep(4)
    print('...josephine')

asyncio.run(main())

    
    
        
        
    





        
