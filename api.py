from orders.app import app, get_db_conn
from datetime import datetime
from fastapi import HTTPException
from fastapi import Request #Send a received request

#Capture the data

#Insert data into the db
#Decorator
@app.post('/orders') #End point
#async fun runs independently
async def createOrder(request: Request):
    
    #inside the function request payload customer
    data=await request.json()
    print(data)
    created_at=datetime.now()
    status="created"
    connection, cursor = get_db_conn()

    #
    try:
        #dynamically insert values into the db
          cursor.execute("""
          INSERT INTO Orders(datetime,status)
          VALUES (%s,%s)             
                         """,(created_at,status))
          
          orderId=cursor.lastrowid
          print(orderId)

          for item in data["orders"]:
            product = item["product"]
            qty = item["quantity"]
            size = item["size"]
            print(product,qty,size)
            cursor.execute("""
            insert into orderItems (orderId, item, qty, size)
             values (%s, %s, %s, %s)
                           """, (orderId, product, qty, size))
          connection.commit()
          return "Success!!!"

    except Exception as e:
            #initaite an in case of an error
            print("There has been an error {e}")
            raise HTTPException(status_code=500,detail="Unable to connect to the db")
    
#Second api
@app.get('/orders/{id}')
async def getOrders(id:str):
     try:
          #
          connection,cursor=get_db_conn()
          #
          cursor.execute("""
          SELECT * FROM orders WHERE orderid=%s               
          """,(id))
          order=cursor.fetchone()
          # cursor.execute("""
          #                )
          return order
          

     except Exception as e:
            #initaite an in case of an error
            print("There has been an error {e}")
            raise HTTPException(status_code=500,detail="Unable to fetch the data")