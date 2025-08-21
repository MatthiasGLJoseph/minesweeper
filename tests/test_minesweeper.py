import pytest

import src.minesweeper as minesweeper


def test_module_exists():
    assert minesweeper


def test_init():
    game = minesweeper.Minesweeper(3, 3, 2)
    assert game.rows == 3, "Wrong number of rows received."
    assert game.cols == 3, "Wrong number of columns received."
    assert game.num_mines == 2, "Wrong number of mines received."
    assert len(game.board) == 3, "Wrong number of rows placed."
    for c in game.board:
        assert len(game.board) == 3, "Wrong number of columns placed."
    assert len(game.mines) == 2, "Wrong number of mines placed."
    assert len(game.revealed) == 0, "Board already partially revealed."


def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    assert len(game.mines) == 2, "The mines weren't placed properly."


def test_reveal_failure():
    game = minesweeper.Minesweeper(3, 3, 2)
    pos = next(iter(game.mines))
    test = game.reveal(pos[0], pos[1])
    assert pos in game.revealed, "The mine was not revealed."
    assert test == "Game Over", "The game should be over."


def test_reveal_success():
    game = minesweeper.Minesweeper(3, 3, 2)
    pos = (0, 0)
    for r in range(game.rows):
        for c in range(game.cols):
            if pos == (0, 0) and (r, c) not in game.mines:
                pos = (r, c)

    test = game.reveal(pos[0], pos[1])
    assert pos in game.revealed, "A wrong case was revealed."
    assert test == "Continue", "The game should be continuing."


def test_get_board():
    game = minesweeper.Minesweeper(3, 3, 2)
    assert len(game.get_board()) == 3, "Wrong number of rows."
    for c in game.get_board():
        assert len(game.get_board()) == 3, "Wrong number of columns."


def test_is_winner():
    game = minesweeper.Minesweeper(3, 3, 2)
    for r in range(game.rows):
        for c in range(game.cols):
            if (r, c) not in game.mines and (r, c) not in game.revealed:
                game.reveal(r, c)

    assert game.is_winner(), "Winner has not won."
