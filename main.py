"""Charm the Commuter: one line of weather for a city that does not exist.

Writes the chosen forecast line to /output/entry.txt.
No network, no clock, no randomness, no file reads outside the repo.
The line is a fixed string in the code.
"""

import os

FORECAST = "Puddlington: heavy rain all day, puddles promoted to ponds \u2014 the ducks have queued at the bus stop, and honestly, they look drier than us."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)

if __name__ == "__main__":
    main()
