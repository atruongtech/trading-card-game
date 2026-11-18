

#!/usr/bin/env python3
"""Entry point for the trading card game."""

from __future__ import annotations
from gamefield import Game
from minions.footman import FootManMinion



def main() -> int:
    """Run the game loop."""
    print("Welcome to the Trading Card Game!")
    print("Game starting...")

    game = Game(lambda player: print(f"Player {player.name} wins!"))
    testMinion = FootManMinion()
    game.gamefield.add_minion(game.player1, testMinion)
    testMinion.calculateDamage(5, game.gamefield);
    for minions in game.gamefield.minions.values():
        for minion in minions:
            print(f"{minion.name}: HP {minion.currentHp}")


    return 0


if __name__ == "__main__":
    raise SystemExit(main())
