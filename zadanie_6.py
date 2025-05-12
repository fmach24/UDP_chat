# ZADANIE 6: Uzupełnij kod, aby zadania ping() były uruchamiane równolegle w osobnych zadaniach.

import asyncio

async def ping(n):
    await asyncio.sleep(n)
    print(f"Ping po {n} sekundach")

async def main():
    # ← tutaj uzupełnij
    task1 = asyncio.create_task(ping(1))
    task2 = asyncio.create_task(ping(2))
    await asyncio.gather(task1, task2)

asyncio.run(main())
