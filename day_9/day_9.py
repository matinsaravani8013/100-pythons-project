prices = {} 

while True:
    name = input("enter your name: ")
    if name == 'exit':
        break
    
    price = float(input("enter your price: "))
    
    prices[name] = price

if prices:
    max_price = max(prices.values())
    max_product = [key for key, value in prices.items() if value == max_price]
    print(f"name: {max_product}، price: {max_price}")
else:
    print("no name no price")