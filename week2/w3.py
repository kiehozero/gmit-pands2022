carorder = "I have a {carname}, it is a {model}."
itemno = 567
myorder = "I want {0} pieces of item number {1} for {2:.2f} euro. The sales total is {2:.2f}."
price = 49
qty = 3
txt = "The price is {:.2f} euro."

print(txt.format(price))

print(myorder.format(qty,itemno,price))

print(carorder.format(carname = "Toyota", model = "Corolla"))