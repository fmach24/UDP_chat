# ZADANIE 2: Uzupełnij kod, aby uruchomić dwie funkcje zegar1() i zegar2() równolegle.

import asyncio

async def zegar1():
    await asyncio.sleep(1)
    print("Zegar 1")

async def zegar2():
    await asyncio.sleep(2)
    print("Zegar 2")

async def main():
    # ← tutaj uzupełnij
    await asyncio.gather(zegar1(), zegar2())

asyncio.run(main())
