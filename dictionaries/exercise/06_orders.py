products = {}

def process_input(data):
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name]['quantity'] += quantity
        products[name]['price'] = price
    else:
        products[name] = {'price': price, 'quantity': quantity}

def print_products():
    for name, info in products.items():
        total_price = info['price'] * info['quantity']
        print(f"{name} -> {total_price:.2f}")

while True:
    line = input()
    if line == "buy":
        break
    process_input(line)

print_products()
