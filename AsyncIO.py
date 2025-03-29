#It is basically use to run multiple function parallely
import asyncio
async def function1():
    await asyncio.sleep(1)
    print("This is function 1")
    return "god"
async def function2():
    await asyncio.sleep(1)
    print("This is function 2")
    return "Jayant"
async def function3():
    await asyncio.sleep(3)
    print("This is function 3")
    return "sinha"
async def main():
    # task=asyncio.create_task(function1())
    # task=asyncio.create_task(function2())
    # task=asyncio.create_task(function3())
    # await function1()
    # await function2()
    # await function3()
    L=await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)
asyncio.run(main())
