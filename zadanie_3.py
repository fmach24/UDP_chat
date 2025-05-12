# ZADANIE 3: Uzupełnij kod, aby stworzyć zadanie asynchroniczne zegar() i kontynuować inne operacje w programie.

import asyncio

async def zegar():
    await asyncio.sleep(3)
    print("Zegar po 3 sekundach")

async def main():
    # ← tutaj uzupełnij
    print("Zadanie wystartowało")
    await asyncio.sleep(1)
    print("Program nadal działa")

asyncio.run(main())
