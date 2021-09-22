#Greeting
print("Welcome to the Tip Calculator")
#Input for Bill
bill = input("What was the total bill? ")
#input for Tip
tip = input("What percentage tip would you like to give? ")
#Input for number of people
pax = input("How many people to split the bill? ")
#per person
bill_per_person = round((float(bill[1:]) *(1+int(tip)/100))/int(pax),2)

print(f"Each person should pay ${bill_per_person
