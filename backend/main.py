from backend import session_functions, db_management
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
app = FastAPI()

inprogress_orders = {}
@app.post("/")
async def handle_request(request: Request):
    # get json data from request
    payload = await request.json()

    # Extract necessary information from payload
    # based on structure of Webhook Request from Dialogflow
    intent = payload["queryResult"]["intent"]["displayName"]
    parameters = payload["queryResult"]["parameters"]
    output_contexts = payload["queryResult"]["outputContexts"]

    session_id = session_functions.get_session_id(output_contexts[0]['name'])

    intent_handler_dict = {
        "order.add - context: ongoing-order": add_to_order,
        "order.remove - context: ongoing-order" : remove_from_order,
        "order.complete - context: ongoing-order" : complete_order,
        "track.order: context: ongoing-tracking" : track_order
    }

    return intent_handler_dict[intent](parameters, session_id)


# Adds items to database
def add_to_database(order: dict, session_id: str):

    order_id = db_management.get_next_order_id()

    for food_item, quantity in order.items():
        rcode = db_management.insert_order_item(
            order_id,
            food_item,
            quantity
        )

        if rcode == -1:
            return -1

    db_management.insert_order_tracking(order_id, "in progress")

    return order_id


# For adding order
def add_to_order(parameters: dict, session_id: str):
    food_items = parameters["food-item"]
    quantities = parameters["number"]

    if len(food_items) != len(quantities):
        fulfilment_text = "Sorry, I didn't understand. Can you please provide food items and their quantity clearly."
    else:
        new_food_dict = dict(zip(food_items, quantities))

        if session_id in inprogress_orders:
            current_food_dict = inprogress_orders[session_id]
            current_food_dict.update(new_food_dict)
            inprogress_orders[session_id] = current_food_dict
        else:
            inprogress_orders[session_id] = new_food_dict

        order_string = session_functions.get_food_string(inprogress_orders[session_id])
        fulfilment_text = f"Now you have : {order_string} in your order. Do you wish to add anything else?"

    return JSONResponse(content={
        "fulfillmentText": fulfilment_text
    })


# Complete the order
def complete_order(order: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text = "Couldn't find your order. Can you place a new order?"
    else:
        order = inprogress_orders[session_id]
        order_id = add_to_database(order, session_id)

        if order_id == -1:
            fulfillment_text = "Sorry, couldn't place your order due to some issues. Can you place a new order?"
        else:
            order_total = db_management.get_total_order_price(order_id)
            fulfillment_text = f"Wonderful, we have placed your order. " \
                              f"Here is your order id : {order_id}. " \
                              f"Your order total is {order_total}, which you may pay at the time of delivery :)"

        del inprogress_orders[session_id]

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

# For removing items
def remove_from_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text = "Couldn't find your order. Can you place a new order?"

    current_order = inprogress_orders[session_id]
    food_items = parameters["food-item"]
    removed_items = []
    not_present = []

    for item in food_items:
        if item not in current_order:
            not_present.append(item)
        else:
            removed_items.append(item)
            del current_order[item]

    if len(removed_items) > 0:
        fulfillment_text = f"Removed {', '.join(removed_items)} from your order."

    if len(not_present) > 0:
        fulfillment_text = f"Sorry, {', '.join(not_present)} are not present in your order."

    if len(current_order.keys()) == 0:
        fulfillment_text += f" Your order is empty."
    else:
        order_string = session_functions.get_food_string(current_order)
        fulfillment_text += f"Now you have {order_string} in your order."

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

# For tracking the order
def track_order(parameters: dict, session_id: str):
    order_id = int(parameters["number"])
    order_status = db_management.get_order_status(order_id)

    if order_status:
        fulfillment_text = f"The order status for order {order_id} is: {order_status}"
    else:
        fulfillment_text = f"No order status for order {order_id} found."

    return JSONResponse(content = {
        "fulfillmentText": fulfillment_text
    })