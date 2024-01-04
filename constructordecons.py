# https://www.youtube.com/watch?v=f8QpyhWnVvI&list=PLlvFEn0NKwXIU9LoEOJn_4Yyn0mH-bExL&index=9&t=784s
class Student:
    #constructor
    def __init__(self,name, email) :
        self.name = name
        self.email = email
        print("new Customer")
        
    #destructor  
    def __del__(self):
        print(" Customer deleted")
        
    
obj1 = Student ("michel","mf@gmail.com")
print(obj1.name)
del(obj1)



    
    
       
        