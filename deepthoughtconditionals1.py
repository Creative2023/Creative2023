#Ask the user the question: What is the answer to the Great Quesiton of life, the universe and everything.
answer = input("What is the answer to the Great Question of Life, the Universe and Everything?" )
if answer == str("42"):
    print("Yes")
elif answer == str("forty-two"):
    print("Yes")
elif answer == str("forty two"):
    print("Yes")
else:
    print("No, Adams has failed.")
    

