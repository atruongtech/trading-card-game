
"""Game state container for a trading card game."""
from __future__ import annotations
from typing import Callable


class Minion:
    def __init__(self, name:str, maxHp: int, strength: int) -> None:
        self.name = name
        self.maxHp = maxHp
        self.currentHp = maxHp
        self.strength = strength

    def calculateDamage(self, damage: int, gamefield: Gamefield) -> None:
        self.currentHp -= damage
        if (self.currentHp <= 0):
            self.removeSelf(gamefield)

    def removeSelf(self, gamefield: Gamefield) -> None:
        gamefield.remove_minion(self)

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self._maxHp = 20
        self.currentHp = 20

    def calculate_damage(self, damage: int, game: Game):
        self.currentHp -= damage
        if (self.currentHp <= 0):
            game.declare_loser(self)

class Game:
    def __init__(self, on_win: Callable[[Player], None]) -> None:
        self.players = [Player("1"), Player("2")]
        self.gamefield = Gamefield(self.players[0], self.players[1])
        self.is_over = False
        self._on_win = on_win

    @property
    def player1(self):
        return self.players[0]

    @property
    def player2(self):
        return self.players[1]
    
    def declare_loser(self, player: Player):
        winner = next((x for x in self.players if x != player))
        self.declare_winner(winner)

    def declare_winner(self, player: Player):
        self.is_over = True
        self._on_win(player)


class Gamefield:
    def __init__(self, player1: Player, player2: Player):
        self.minions: dict[Player, list[Minion]] = {player1: [], player2: []}

    def add_minion(self, player: Player, minion: Minion) -> None:
        if minion in self.minions[player]:
            raise ValueError("Minion already on field")
        self.minions[player].append(minion)

    def remove_minion(self, minion: Minion) -> None:
        for minions in self.minions.values():
            if minion in minions:
                minions.remove(minion)

