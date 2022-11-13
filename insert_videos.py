import requests
import motor.motor_asyncio
import asyncio
import pprint
import inspect

conn_str = "localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
db = client.Peertuber

async def get_instances():
    collection = db.instances
    i = 0
    # async for document in collection.find({'id': {'$gt': 0}})
    # cursor = collection.find({})
    async for doc in collection.find({},{'host': 1, '_id': False}):
        print(doc)
        # print(document['host'])
            # doc = asyncio.result(document)
        print(i)
        i += 1
        # res = asyncio.Future.set_result(doc)
        # itms = res.items()
        # print(itms['host'])
        # pprint.pprint(inspect.getmembers(host))
        # print('items {0}'.format(host.items()))
        # pprint.pprint('host: {0} id: {1}'.format(document['host'],document['id']))

loop = client.get_io_loop()
loop.run_until_complete(get_instances())