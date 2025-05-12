# ZADANIE 5: Uzupełnij funkcje producenta i konsumenta, by dodawały i odbierały dane z kolejki asynchronicznej.

import asyncio

async def producent(queue):
    for i in range(3):
        await asyncio.sleep(1)
        # ← tutaj uzupełnij
        await queue.put(i)

async def konsument(queue):
    while True:
        item = await queue.get()
        # ← tutaj uzupełnij
        print("Odebrano:", item)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producent(queue), konsument(queue))

asyncio.run(main())
