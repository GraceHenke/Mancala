# Mancala AI
This implements the game of Mancala. It also implements two random agents that work against each other to win


### Actions
Depending on which holes are full and which are empty. Actions are also determined based on the which players turn it is.

### Board Repersentation
[0,4,4,4,4,4,4,0,4,4,4,4,4,4]


### Mancala Environment Methods (mancala.py)
- __init__:  creates and initalizes the board + variables
- __getTurnFlag__: returns the turn flag 
- __getPlayerOnePoints__: returns player one's points 
- __getPlayerTwoPoints__: returns player two's points
- __getBoard__: returns the board
- __playerOneTurn__: simulates one turn for player one 
- __playerTwoTurn__: simulates one turn for player two
- __capture_or_extra_or_nothing__: determines capture/extra for each turn
- __legalActionsPlayerOne__: returns all possible legal actions for player one
- __legalActionsPlayerTwo__:returns all possible legal actions for player two
- __empty__: determine whether (6) holes are empty
- __determineWinner__: prints the winner of the game
- __printState__: prints the board 


### Mancala Datamembers (maze.py)
- __mBoard__: holds the values for each pit 
- __mExtraTurnFlag__: indicates whether or not the player has gotten an extra turn
- __mMoves__: how many moves have been taken




### Model Class Methods (model.py)
- __updatePlayer__: sets the current player to the new player
- __result__: creates a copy of the environment after applying an action
- __getLegalActions__: returns the possible actions
- __GoalTest__: tests whether or not the goal has been met 
- __updatePercepts__: updates the observable percepts
- __applyAction__: applies the desired action to the environment
- __getObservable__: returns all of the observeable percepts from the env.
- __done__: returns whether or not the done condition has been met

### Model Class Datamemebers
- __mModel__: the environment obj
- __mPlayerOne__: player ones points
- __mPlayerTwo__: player two points
- __mExtraTurn__: whether or not player gets another turn or not
- __mMoves__: how many moves have been taken
- __mCurrentPlayer__: current player 


### Agent Class Methods (main.py)
- __init__: initalizes a model object by passing in a maze object.
- __agentFunction__: takes in the percpts and the current player. outputs the random action the agent should take


### Main (main.py)
creates enviorment and the agent, displays the perfomance measure, currently runs the random agent implementation 
