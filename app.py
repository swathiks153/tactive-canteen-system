from flask import Flask, render_template, request
from database import get_connection, initialize_database

app = Flask(__name__)

initialize_database()


@app.route("/")
def home():
    connection = get_connection()

    foods = connection.execute(
        "SELECT * FROM foods"
    ).fetchall()

    connection.close()

    return render_template("index.html", foods=foods)


@app.route("/order", methods=["POST"])
def order():

    food_id = request.form["food_id"]
    quantity = int(request.form["quantity"])

    connection = get_connection()

    food = connection.execute(
        "SELECT * FROM foods WHERE id = ?",
        (food_id,)
    ).fetchone()

    if food is None:
        connection.close()
        return render_template(
            "error.html",
            message="Sorry, the selected food item could not be found."
        ), 404

    if quantity <= 0:
        connection.close()
        return render_template(
            "error.html",
            message="Quantity must be greater than 0."
        ), 400

    if quantity > food["stock"]:
        connection.close()
        return render_template(
            "error.html",
            message="Sorry, there isn't enough stock available for this order."
        ), 400


 

    total = food["price"] * quantity
    remaining_stock = food["stock"] - quantity

    connection.execute(
        "UPDATE foods SET stock = ? WHERE id = ?",
        (remaining_stock, food_id)
    )

    connection.execute(
        """
        INSERT INTO orders (food_name, quantity, total)
        VALUES (?, ?, ?)
        """,
        (food["name"], quantity, total)
    )




    connection.commit()
    connection.close()

    return render_template(
        "success.html",
        food=food,
        quantity=quantity,
        total=total,
        remaining_stock=remaining_stock
    )
@app.route("/orders")
def orders():
    connection = get_connection()

    orders = connection.execute(
        "SELECT * FROM orders ORDER BY order_time DESC"
    ).fetchall()

    connection.close()

    return render_template("orders.html", orders=orders)



if __name__ == "__main__":
    app.run(debug=True)


