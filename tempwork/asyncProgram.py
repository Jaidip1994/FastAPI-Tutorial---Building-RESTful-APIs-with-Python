import asyncio

# Defining Co-routine

async def main():
    print('Hello Co-routine')

# If we directly call the same it will be giving the error
# main()
# RuntimeWarning: coroutine 'main' was never awaited
# main()
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback

# print(main())
# As it can be seen above the main() -> returns a coroutine object
# <coroutine object main at 0x03350DA8>
# c:/Users/I327559/OneDrive - SAP SE/Documents/IMP/Python/FastAPI-Tutorial---Building-RESTful-APIs-with-Python/asyncProgram.py:14: RuntimeWarning: coroutine 'main' was never awaited
#   print(main())
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback

# So as to call the Async process we need an async event loop which expects a co-routine object
asyncio.run(main())

print("Next example\n\n\n")

# Below code explains the working behaviour of asynchronous code and also the usage of await keyword
async def test():
    print('test')
    # await test2()
    # the problem here is await will wait until and unless the below method have finished execution
    # So as to run con-currently use the the below line

    asyncio.create_task(test2())
    # what happens now is it will first execute the whole main then switch back to the next method

    await asyncio.sleep(3)
    print('finished')

async def test2():
    print('test2')
    await asyncio.sleep(2)
    print('finished test2')

asyncio.run(test())


print("Next example\n")

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'name': 'hello_async'}

async def print_number():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_number())

    value = await task1
    print(value)
    await task2

asyncio.run(main())