import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="<password>",
    database="pandeyji_eatery"
)

def get_next_order_id():
        cursor = cnx.cursor()

        query = "SELECT max(order_id) FROM orders"

        cursor.execute(query)

        result = cursor.fetchone()[0]

        # Return next available
        if result is None:
            return 1
        else:
            return result+1

def insert_order_item(order_id, food_item, quantity):
    try:
        cursor = cnx.cursor()

        # Calling stored function
        cursor.callproc("insert_order_item", (food_item, quantity, order_id))

        # Committing changes
        cnx.commit()

        cursor.close()

        print("Order Item Inserted")

        return 1

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL - {e}")
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error has occurred - {e}")
        cnx.rollback()

        return -1


def get_total_order_price(order_id):
    cursor = cnx.cursor()

    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    result = cursor.fetchone()[0]
    cursor.close()

    return result


def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(query, (order_id, status))
    cnx.commit()
    cursor.close()

def get_order_status(order_id: int):
    # Create a cursor object
    cursor = cnx.cursor()

    # Query for getting status
    query = ("SELECT status FROM order_tracking WHERE order_id = %s")

    # Execute the query
    cursor.execute(query, (order_id,))

    result = cursor.fetchone()

    # Close the cursor
    cursor.close()

    if result is not None:
        return result[0]
    else:
        return None
