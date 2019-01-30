value = int(input("how old are you:"))
def age(age):
 if age <= 18:
     print('you are a minor')
 elif age <= 36:
     print('you are a youth')
 else:
     print('you are an elder')
age(value)
