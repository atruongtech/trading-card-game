
"""Game state container for a trading card game."""
from __future__ import annotations


class Minion:
    def __init__(self, name:str, maxHp: int, strength: int) -> None:
        self.name = name
        self.maxHp = maxHp
        self.currentHp = maxHp
        self.strength = strength

    def calculateDamage(damage: int, gamefield: Gamefield) -> None:
        self.currentHp -= damage
        if (self.currentHp <= 0):
            removeSelf(gamefield)

    def removeSelf(gamefield: Gamefield) -> None:
        gamefield.remove_minion(self)

class Gamefield:
    """Store and update the players, cards, and turn state of a game."""

    def __init__(self, players=None, cards=None):
        self._players = list(players or ())
        self._current_player_index = 0
        self._turn_number = 1 if self._players else 0
        self.minions: list[Minion] = []

    @property
    def players(self):
        """Players in the game, in turn order."""
        return tuple(self._players)

    @property
    def current_player(self):
        """The player whose turn it is, or None when unavailable."""
        if self._is_over or not self._players:
            return None
        return self._players[self._current_player_index]

    @property
    def turn_number(self):
        return self._turn_number

    def add_minion(self, minion: Minion) -> None:
        if minion in self.minions:
            raise ValueError("Minion already on field")
        self.minions.append(minion)

    def remove_minion(self, minion: Minion) -> None:
        self.minions.remove(minion)

    def advance_turn(self):
        """Move play to the next player and return that player."""
        if self._is_over:
            raise RuntimeError("Cannot advance a game that has ended.")
        if not self._players:
            raise RuntimeError("Cannot advance a game with no players.")

        self._current_player_index += 1
        if self._current_player_index == len(self._players):
            self._current_player_index = 0
            self._turn_number += 1
        return self.current_player

