import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

EMPTY_BOARD = [[None, None, None], [None, None, None], [None, None, None]]


def check_winner(board):
    # Rows, columns, diagonals
    lines = board + [list(col) for col in zip(*board)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    for line in lines:
        if line[0] and line.count(line[0]) == 3:
            return line[0]
    if all(cell for row in board for cell in row):
        return 'Draw'
    return None


def new_board():
    return [[None, None, None], [None, None, None], [None, None, None]]


@app.route("/", methods=["GET", "POST"])
def index():
    if "board" not in session:
        session["board"] = new_board()
        session["turn"] = "X"
        session["winner"] = None

    board = session["board"]
    turn = session["turn"]
    winner = session["winner"]

    if request.method == "POST" and not winner:
        row = int(request.form["row"])
        col = int(request.form["col"])
        if board[row][col] is None:
            board[row][col] = turn
            winner = check_winner(board)
            session["winner"] = winner
            session["turn"] = "O" if turn == "X" else "X"
            session["board"] = board
        return redirect(url_for("index"))

    return render_template("index.html", board=board, turn=turn, winner=winner)


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
