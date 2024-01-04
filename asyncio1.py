import asyncio
from re import X
import asyncio
import time

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
    
asyncio.run(main())



import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
        
        