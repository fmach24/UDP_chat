# ZADANIE 4: Uzupełnij funkcję, aby uruchomić ją w osobnym wątku i kontynuować główny program.

import threading
import time

def watek():
    time.sleep(2)
    print("Wątek zakończony")

def main():
    # ← tutaj uzupełnij
    print("Program działa równolegle")
    time.sleep(1)
    print("Program dalej działa")

main()
