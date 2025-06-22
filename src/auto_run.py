# src/auto_run.py

import time
from main import run  # <- a main.py-ból importáljuk a futtató függvényt

INTERVAL_MINUTES = 0.1  # teszthez 6 másodperc

def run_loop():
    print(f"⏱️ Indul az automatikus predikciós ciklus ({INTERVAL_MINUTES} percenként)...")

    while True:
        print("\n🔄 Új ciklus:", time.strftime('%Y-%m-%d %H:%M:%S'))
        try:
            run()  # EZ futtatja a main.py tartalmát!
        except Exception as e:
            print(f"❌ Hiba történt a ciklusban: {e}")

        print(f"⏸️ Várakozás {INTERVAL_MINUTES} percig...\n")
        time.sleep(INTERVAL_MINUTES * 60)

if __name__ == "__main__":
    run_loop()
