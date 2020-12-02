def nameOfBestCustomer(sales, customers):
    maxSaleIndex = 0

    for i in range(len(sales)):
        if sales[i] > sales[maxSaleIndex]:
            maxSaleIndex = i

    return customers[maxSaleIndex]

sales = []
customers = []

price = int(input("Inserire importo dell'acquisto(0 per uscire): "))
while price != 0:
    name = input("Inserire nome del cliente: ")

    sales.append(price)
    customers.append(name)
    price = int(input("Inserire importo dell'acquisto(0 per uscire): "))

print("Il cliente migliore è stato", nameOfBestCustomer(sales, customers))