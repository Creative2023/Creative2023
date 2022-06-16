
# Create a function called convert
def convert(greeting, go):
       
       print(greeting,go)
       
#Say hello 
greeting=input("Please type Hello")
happy = input("Hello, please enter :)")

happi = happy.replace(":)", "🙂")
convert(greeting,happy)
print("Hello", happi)
#Say goodbye
greeting=input("Please say Goodbye")
goodbye=input("Please enter :(")
bye=goodbye.replace(":(", "🙁")
convert(greeting,goodbye)
print("Goodbye", bye)
