from flask import Flask, redirect, request, render_template, flash, url_for
import requests
import datetime


app = Flask(__name__)


    
cart=[]
fullOrder = []


def createOrder():
    orderID = []
    orderIDs = requests.get("http://localhost:2223/orders").json()
    for i in orderIDs:
        orderID.append(i["orderId"])
    print(orderID[-1][0:5]+str(int(orderID[-1][5:])+1))
    return orderID[-1][0:5]+str(int(orderID[-1][5:])+1)
    
@app.route("/", methods=["POST", "GET"])
def home():
    products = requests.get("http://localhost:2222/products").json()
    return render_template("home.html", data=[products,int(len(products))])

@app.route("/addToCart", methods=["POST", "GET"])
def addToCart():
    product_id = request.form["product"]
    cart.append(product_id)
    return redirect(url_for('home'))

@app.route("/orderPage", methods=["POST", "GET"])
def orderPage():
    fullCart = []
    totalPrice = 0
    amounts = []
    for i in range(len(cart)):
        product = requests.get("http://localhost:2222/products/"+str(cart[i])).json()
        if product in fullCart:
            amounts[fullCart.index(product)] += 1
        else:
            amounts.append(1)
            fullCart.append(product)
        totalPrice += product["price"]

    for i in range(len(fullCart)):
        fullOrder.append([fullCart[i]["id"],amounts[i]])

    return render_template("orderPage.html", data=[fullCart,round(totalPrice,2),amounts,sum(amounts),len(fullCart)])

@app.route("/order", methods=["POST", "GET"])
def order():
    id = request.form["custID"]
    # cartJSON = cart.__dict__
    #public Order(String orderId, Long customerId, Long productId, int quantity, LocalDateTime orderDate)

    orderID = createOrder()
    for i in fullOrder:
        print({   "orderId":orderID,
                                    "customerId":id,
                                    "productId":i[0],
                                    "quantity":i[1],
                                    "orderDate":datetime.datetime.now().strftime("%Y-%m-%d")})
        order = requests.post("http://localhost:2223/orders/createOrder", 
                              json={"orderId":orderID,
                                    "customerId":id,
                                    "productId":i[0],
                                    "quantity":i[1],
                                    })
                              
        print(order.text)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()