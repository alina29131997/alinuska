from product import Product

searchDate =int(input("vvedite god :"))
productList = []
productList.append(Product("videokarta","AMD","2016","100", "900"))
productList.append(Product("RAM","kingston","2019","120","50"))
productList.append(Product("monitor","Acer","2021","400","150"))
productList.append(Product("router","cisco","2020","200","100"))
productList.append(Product("ventiljator","noname","2021","400","30"))
productList.append(Product("matplata","intel","2019","200","200"))

summa = 0

for product in productList:
    if product.getDateOfIssue() == searchDate:
        summa += product.getPrice()*product.getAmount()
        product.show()
print(summa)
