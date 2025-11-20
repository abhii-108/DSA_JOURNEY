import asyncio

from util import delay

async def add_one(number) -> int:
    return number + 1 

async def hello() -> str:
    await delay(1)
    return "Hello abhilash..!"

async def main() -> None:
    print(sync_start = time.time())
    message = await hello()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)


asyncio.run(main())