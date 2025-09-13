import pytest
from app import app, check_winner, new_board

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Tic Tac Toe' in response.data

def test_new_game_board():
    board = new_board()
    assert board == [[None, None, None], [None, None, None], [None, None, None]]

def test_check_winner_x():
    board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
    assert check_winner(board) == 'X'

def test_check_winner_o():
    board = [[None, None, None], ['O', 'O', 'O'], [None, None, None]]
    assert check_winner(board) == 'O'

def test_check_winner_diag():
    board = [['X', None, None], [None, 'X', None], [None, None, 'X']]
    assert check_winner(board) == 'X'

def test_check_draw():
    board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    assert check_winner(board) == 'Draw'

def test_move_and_win(client):
    with client.session_transaction() as sess:
        sess['board'] = [[None, None, None], [None, None, None], [None, None, None]]
        sess['turn'] = 'X'
        sess['winner'] = None
    # X moves (0,0)
    client.post('/', data={'row': 0, 'col': 0})
    # O moves (1,0)
    client.post('/', data={'row': 1, 'col': 0})
    # X moves (0,1)
    client.post('/', data={'row': 0, 'col': 1})
    # O moves (1,1)
    client.post('/', data={'row': 1, 'col': 1})
    # X moves (0,2) - X wins
    response = client.post('/', data={'row': 0, 'col': 2}, follow_redirects=True)
    assert b'X wins!' in response.data or b'X wins' in response.data
