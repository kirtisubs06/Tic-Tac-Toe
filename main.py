# Tic Tac Toe
from tictactoe import Tictactoe

game = Tictactoe()

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    player1Letter, player2Letter = game.inputPlayerLetter()
    turn = game.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player 1':
            # Player 1's turn.
            game.drawBoard()
            move = game.getPlayerMove()
            game.makeMove(player1Letter, move)

            if game.isWinner(player1Letter):
                game.drawBoard()
                print('Hooray! Player 1 has won the game! Better luck next time to Player 2.')
                gameIsPlaying = False
            else:
                if game.isBoardFull():
                    game.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2's turn.
            game.drawBoard()
            move = game.getPlayerMove()
            game.makeMove(player2Letter, move)

            if game.isWinner(player2Letter):
                game.drawBoard()
                print('Hooray! Player 2 has won the game! Better luck next time to Player 1.')
                gameIsPlaying = False
            else:
                if game.isBoardFull():
                    game.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not game.playAgain():
        break