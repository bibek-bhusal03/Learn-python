import asyncio
import time

async def say_after(delay, what):
    """Coroutine that waits for a delay and then prints a message."""
    await asyncio.sleep(delay) # Yield control to the event loop
    print(what)

print(f"print coroutine: {say_after(1, 'wow nice')}")

async def main():
    print(f"started at {time.strftime('%X')}")

    # Create tasks to run concurrently
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # Wait until both tasks are completed
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

# The entry point to run the asynchronous program
# if __name__ == "__main__":
    # asyncio.run(main())
