

#!/usr/bin/env python3
"""Entry point for the trading card game."""

from __future__ import annotations
from gamefield import Gamefield, Minion
from footman import FootManMinion

import sys


def main() -> int:
    """Run the game loop."""
    print("Welcome to the Trading Card Game!")
    print("Game starting...")

    gamefield = Gamefield()
    testMinion = FootManMinion()
    gamefield.add_minion(testMinion)
    for minion in gamefield.minions:
        print(f"{minion.name}: HP {minion.currentHp}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
