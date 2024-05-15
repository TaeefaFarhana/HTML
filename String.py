#string
name="Taeefa"
print(name)
print(f"My name is {name}")

#string with loop
for i in name:
    print(i)
    
#taking string as input
string_input= input("Enter a string : ")
print("Result of input string is : ",string_input)

#uppercase and lower case
Upper_str = string_input.upper()
print("Upper String is : ",Upper_str)

lower_str = string_input.lower()
print("Lower String result is : ",lower_str)

#concate string
str1 = input("Enter a string : ")
str2 = "Assalamualikum."
result1= str1 + str2

print("Concate String is : ",result1)

#string with number adding
str3 = input("Enter a string :")
num1= input("Enter a number : ")
result2= str3 + str(num1)   # here type casting is must
print("After adding we get : ",result2)
