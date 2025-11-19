import asyncio
from util import delay 
import time 


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))

    result = await sleep_for_three
    print(result)


asyncio.run(main())

print('-'*100)

async def main2():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await sleep_for_three
    await sleep_again
    await sleep_once_more

asyncio.run(main2())

print('_'*100)
print("running code while other operation complete...!!")

async def hello_every_sec():
    for i in range(2):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting..!")


async def main3():
    start_main=time.time()
    first_delay = asyncio.create_task(delay(5))
    second_delay = asyncio.create_task(delay(3))
    start_await=time.time()
    await hello_every_sec()
    end_hello = time.time()
    await first_delay
    await second_delay

    final_end = time.time()

    print(f'start_await = {start_await - start_main:.3f} end_hello = {end_hello - start_main:.3f} final = {final_end - start_main:.3f}')

asyncio.run(main3())