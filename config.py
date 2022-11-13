import asyncio
import motor.motor_asyncio



async def get_server_info():

    conn_str = "localhost:27017"

    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)

    try: 
        dbList = await client.list_database_names()
        # print(await client.server_info())
        print(dbList)
    except Exception:
        print("Unable to connect to the server")

loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())


