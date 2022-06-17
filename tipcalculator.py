dollars = input("How much was the meal? Please include dollar sign.")
#strip dollars of the $ sign and make it a float
dollars= float(dollars.replace("$",''))
percent=input("What percent do you want to tip?" )
percent=float(percent.replace("%", ""))
percent=float(percent/100)
tip = dollars * percent
print(f"Leave ${tip:.2f}")


