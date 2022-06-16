#I speak rather quickly. Slow me down by adding three... to your response.
speedy = input("Say hello,my name is Mud. I will slow you down." )
#Strip white space from either end of response
speedy = speedy.strip()

#Put three dots between reponse words.
speedy = speedy.replace(" ", "...")
#Print response
print(speedy)
