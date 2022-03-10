import matplotlib.pyplot as plt

open_file = open('CupcakeInvoices.csv')
total_total = 0
strawberry_sales = 0
chocolate_sales = 0
vanilla_sales = 0
for line in open_file:
    line = line.rstrip('\n,\r').split(',')
    for i in line:
        order_total = float(line[3]) * float(line[4])
        if line[2] == 'Strawberry':
            strawberry_sales += order_total
        if line[2] == 'Chocolate':
            chocolate_sales += order_total
        if line[2] == 'Vanilla':
            vanilla_sales += order_total
        total_total += order_total
print(total_total)

flavors = ['strawberry', 'chocolate', 'vanilla']
totals = [strawberry_sales, chocolate_sales, vanilla_sales]

fig1, ax1 = plt.subplots()
ax1.pie(totals, labels=flavors, autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

open_file.close()

exit()
