# https://docs.python.org/3/library/asyncio-task.html
# from re import X
import asyncio
import time

from asyncio1 import say_after

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
         say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
# asyncio.run(main())
    