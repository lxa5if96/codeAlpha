stocks = {"AAPL":180,"TSLA":250,"MSFT": 420,"AMZN": 190,"GOOGL": 170}
totalInvestment  = 0
portfolio = {}

def view_stock():
    for i,j in stocks.items():
        print(i,"-",j)

def buy_stock():
    global totalInvestment
    stockName = input("Enter stock name: ").upper()

    if stockName not in stocks:
        print("Stock not found.")
        return
    
    try:
        stockQuantity = int(input("Enter stock quantity: "))
        if stockQuantity <= 0:
            print("Quantity must be above 0.")
            return
    except ValueError:
        print("Invalid number")
        return
    
    if stockName in portfolio:
        portfolio[stockName]["quantity"] += stockQuantity
    else:
        portfolio[stockName] = {
            "price" : stocks[stockName],
            "quantity": stockQuantity
        }

    totalInvestment += stocks[stockName] * stockQuantity
    print("Stock bouht Successfully.")   

def view_Total():     
    print("\n-------Portfolio--------")

    for stock, data in portfolio.items():
        print(stock,"-","Quantity:",data["quantity"],"price:",data["price"])

    print("------------------------")
    print("Total Investment: ",totalInvestment)

def save_file():

    with open("portfolio.txt","w") as file:
        for stock, data in portfolio.items():
            file.write(f"{stock}- quantity:{data["quantity"]}- price per stock:{data["price"]}\n")
        
        file.write("-----------------------------------------")
        file.write("\nTotal Investment: "+str(totalInvestment))

    print("file save successfully!")


while True:
    print("\n1. View Stock\n2. Buy Stock\n3. View Total Investment\n4. Save as file\n5.Exit")
    

    try:
        choice = int(input("Enter your option: "))
    except ValueError:
        print("Please enter number only!")
        continue


    if choice == 1:
        view_stock()
    elif choice == 2:
        buy_stock()
    elif choice == 3:
        view_Total()
    elif choice == 4:
        save_file()
    elif choice == 5:
        break
    else:
        print("Invalid Option.")