from fastapi import FastAPI # BAckend Framework
import pymysql # Connect Python and MYSQL
from fastapi import HTTPException # Used to handle errors

app = FastAPI()

db_config={
    "host":"localhost",
    "user":"root",
    "password":"Kumar.S@292004..",
    "database":"projectapi"
}

def get_db_conn():
    try:
        #initiate a connection
        connection=pymysql.connect(**db_config,cursorclass=pymysql.cursors.DictCursor)
        cursor=connection.cursor()
        print("Successfully connected to the db")
        return connection,cursor
    
    except Exception as e:
        #initaite an in case of an error
        print("There has been an error {e}")
        raise HTTPException(status_code=500,detail="Unable to connect to the db")
    
get_db_conn()

from orders.API import api
    
