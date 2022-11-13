import requests
import motor.motor_asyncio

conn_str = "localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
db = client.Peertuber

async def do_insert():
    
    more_instances = True
    page_num = 0
    while more_instances:
        api_url = 'https://instances.joinpeertube.org/api/v1/instances?start={0}&count=10&sort=-createdAt'.format(page_num)  
        response = requests.get(api_url)
        res = response.json()

        instances = res['data']
        if len(instances) == 0:
            more_instances = False
            break

        page_num += 10
        result = await db.instances.insert_many(instances)
        print('result %s' % repr(result))

loop = client.get_io_loop()
loop.run_until_complete(do_insert())

    


