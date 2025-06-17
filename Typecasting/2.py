#string to int converter 
num_string = "111"
num_int = int(222)
print("Number before typecasting", type(num_string))
num_string = int(num_string)
print ("Datatype after typecasting", type(num_string))
print(f"Now their sum is {num_string+num_int}")
