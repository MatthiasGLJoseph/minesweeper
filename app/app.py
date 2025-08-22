# app.py
import os
import sys

from flask import Flask, redirect, render_template, request, url_for

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.minesweeper import Minesweeper

app = Flask(__name__)

# Create a new game
game = Minesweeper(5, 5, 3)


@app.route("/")
def index():
    board = game.get_board()
    if game.is_winner():
        game.maybe = set()
        return render_template("index.html", board=board, message="🔥 You Win! 🔥")
    return render_template("index.html", board=board, maybe=game.maybe)


@app.route("/reveal/<int:row>/<int:col>")
def reveal(row, col):
    if (row, col) not in game.maybe:
        result = game.reveal(row, col)
        if result == "Game Over":
            game.maybe = set()
            return render_template(
                "index.html", board=game.board, message="🥲 Game Over! 🥲"
            )
    return redirect(url_for("index"))


@app.route("/select/<int:row>/<int:col>")
def select(row, col):
    game.select(row, col)
    return redirect(url_for("index"))


@app.route("/restart")
def restart():
    game.restart()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
