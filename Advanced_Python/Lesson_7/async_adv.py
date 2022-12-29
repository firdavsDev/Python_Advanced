##################### ASYNC ADVANCED #####################

# Questions:

# 1. What is the difference between async and await?
# 2. What is the difference between asyncio and aiohttp?
# 3. What is the difference between asyncio and multiprocessing?
# 4. What is the difference between asyncio and threading?

# Q: What is the difference between async and await?
# A: The async keyword is used to define a function as a coroutine. The await keyword is used to await the result of a coroutine. 
# The await keyword can only be used inside a coroutine.

# Q: What is the difference between asyncio and aiohttp?
# A: asyncio is a library to write concurrent code using the async/await syntax.
# aiohttp is a HTTP client/server for asyncio.

# Q: What is the difference between asyncio and multiprocessing?
# A: The multiprocessing module offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads.
# Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.
# The asyncio module is used to write single-threaded concurrent code using the async/await syntax.
# Due to this, the asyncio module allows the programmer to fully leverage a single processor on a given machine. It runs on both Unix and Windows.

# Q: What is the difference between asyncio and threading?
# A: The threading module offers local concurrency, effectively side-stepping the Global Interpreter Lock by using threads instead of processes.
# Due to this, the threading module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.
# The asyncio module is used to write single-threaded concurrent code using the async/await syntax.
# Due to this, the asyncio module allows the programmer to fully leverage a single processor on a given machine. It runs on both Unix and Windows.



# Exmaple: Sne d 5000 requests to a website using asyncio and aiohttp

import asyncio
import aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
        
async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.google.com')
        print(html)

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop() # get_event_loop() returns the event loop for the current OS thread
    tasks = [main() for _ in range(5)] # create 5 tasks
    loop.run_until_complete(asyncio.wait(tasks)) # run the tasks until they are complete
    print(time.time() - start) # print the time it took to run the tasks

# Sychronous version of the above code

import requests
import time

def main():
    html = requests.get('https://www.google.com')
    print(html.text)

if __name__ == '__main__':
    start = time.time()
    for _ in range(5):
        main()
    print(time.time() - start)


# Example 2: Calculate the sum of 1000000 numbers using asyncio and aiohttp

import asyncio
import aiohttp
import time

# Calculate the sum of 1000000 numbers
async def sum_numbers():
    return sum(range(1, 100))

async def main():
    task1 = asyncio.create_task(sum_numbers())
    task2 = asyncio.create_task(sum_numbers())
    await task1
    await task2
    return task1.result() + task2.result()

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())
    print(result)
    print(time.time() - start)

# Sychronous version of the above code

import time

def sum_numbers():
    return sum(range(1, 100))

def main():
    task1 = sum_numbers()
    task2 = sum_numbers()
    return task1 + task2

if __name__ == '__main__':
    start = time.time()
    result = main()
    print(result)
    print(time.time() - start)
