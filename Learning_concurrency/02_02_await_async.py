import asyncio


# async def add_one(number: int) -> int:
#     return number + 1


# async def main() -> None:
#     one_plus_one = await add_one(1) #The keyword await can only be used inside an async def function
#     one_plus_two = await add_one(2)

#     print(one_plus_one)
#     print(one_plus_two)

# asyncio.run(main())


print('#'*100)
print('First app with sleep')

async def hello_world() -> str:
    await asyncio.sleep(1) # Pause hello_world_message for 1 sec 
    return "Hello world..!"

async def main() -> None:
    message = await hello_world() #Pause main until hello_world_message finishes

    print(message)

asyncio.run(main())