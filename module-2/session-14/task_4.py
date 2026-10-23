

zomato_orders = {}

def add_order(orders, order_id, restaurant, items, total):
    orders.setdefault(order_id, {
        "restaurant": restaurant,
        "items": items,
        "total": total
    })


def update_total(orders, order_id, new_total):
    if order_id in orders:
        orders[order_id]["total"] = new_total
    else:
        print("Order not found!")


add_order(zomato_orders, 101, "Pizza Hut", ["Pizza", "Coke"], 450)
add_order(zomato_orders, 102, "Dominos", ["Burger", "Fries"], 300)

update_total(zomato_orders, 101, 500)

print(zomato_orders)