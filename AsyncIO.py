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
#-------------------------------------------------------------------------------------------------------------------------

async def func(a):
    print("This is func")
    await asyncio.sleep(a)
    print("This is a ",a)
def main2():
    print("this is main2")
    test=asyncio.run(func(1))
main2()
#-----------------------------------------------------------------------------------------------------------------------------
async def main_func(t_id, time):
    print(f"the task with the {t_id} id  is started")
    await asyncio.sleep(time)
    return f"the task with the {t_id} id  is finished"
async def main3():
    task1=asyncio.create_task(main_func(1,1))
    task2=asyncio.create_task(main_func(2,2))
    task3=asyncio.create_task(main_func(3,3))
    result1=await task1
    result2=await task2
    result3=await task3
    print(result1, result2, result3, sep="\n")
asyncio.run(main3())
#------------------------------------------------------------------------------------------------------------------------------------
#save way to handle multiple task
async def task_list(t_id, time):
    print(f"the task with the {t_id} id  is started")
    await asyncio.sleep(time)
    return f"the task with the {t_id} id  is finished"
async def main4():
    task=[]
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([1,2,3], start=1):
            tasks=tg.create_task(task_list(i, sleep_time))
            task.append(tasks)
    result= [tasks.result() for tasks in task]
    for result in result:
        print(f"completed result : {result}")
asyncio.run(main4())
#------------------------------------------------------------------------------------------------------------------------
#shared resource
Shared_resource = 0
#The lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global Shared_resource
    #Only one func can access at a time and other are locks
    async with lock:
        print(f"Shared resource before modification{Shared_resource}")
        Shared_resource += 1
        await asyncio.sleep(1)
        print(f"Shared resource after modification{Shared_resource}")
    # end of the lock

async def main5():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))
asyncio.run(main5())
#--------------------------------------------------------------------------------------------------------------------------
async def access_resource(semaphore, resource_id):
    async  with semaphore:
        # Simulate accessing a limited resource
        print(f"Access resource {resource_id}")
        print(f"Releasing resource {resource_id}")

async def main6():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))
asyncio.run(main6())
#---------------------------------------------------------------------------------------------------------------------------------
async def waiter(event):
    print("Wait for event to be set")
    await event.wait()
    print("Event has been continuing execution")
async def setter(event):
    await asyncio.sleep(2)
    event.set()
    print("Event has been set!")
async def main7():
    event = asyncio.Event()
    await  asyncio.gather(waiter(event), setter(event))

asyncio.run(main7())