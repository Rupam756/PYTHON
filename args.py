# # def add(a,b):
    
# #     return a+b

# # print (add(5,10))

# # ** function arguments

# def print_address(**kwargs):
#     print(type(kwargs))
    
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(name="John", 
              
              
#               address="123 Main St", 
#               city="New York")




def shiping_address(*args , **kwargs):
    
    
    print(type(args))
    for arg in args:
        print(arg, end=" ")
        
    print()
    
    print(type(kwargs)) 
    for key, value in kwargs.items():
        print(f"{key}: {value}")


shiping_address("Dr.", "Rupam","Mondal",
    Name="John",
    Address="123 Main St", 
    City="New York",
    country="USA", 
    zip_code="10001")
  
  
