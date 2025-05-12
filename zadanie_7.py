# ZADANIE 7: Uzupełnij kod, aby użyć wątku do uruchomienia funkcji asynchronicznej, a następnie wykonać kolejne zadania.

import asyncio
import threading

async def asynchroniczne_zadanie():
    await asyncio.sleep(2)
    print("Asynchroniczne zadanie zakończone")

def uruchom_watek():
    asyncio.run(asynchroniczne_zadanie())

def main():
    # ← tutaj uzupełnij
    thread = threading.Thread(target=uruchom_watek)
    thread.start()
    thread.join()
    print("Program główny kontynuuje działanie")

main()
