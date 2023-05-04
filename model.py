from copy import deepcopy

class Model:
    def __init__(self, state):
        self.mModel =  state
        
        # Observable Percepts
        self.mPlayerOnePoints = 0
        self.mPlayerTwoPoints = 0
        self.mCurrentPlayer = "NONE"
        self.mExtraTurn = False
    
    def updatePlayer(self, new_player):
     
        self.mCurrentPlayer = new_player
       
        
    def result(self, a):
        state_copy = deepcopy(self)
        player = self.mCurrentPlayer
        
        
        if player == "P1":
            state_copy.mModel.playerOneTurn(a)
        
        else:
            state_copy.mModel.playerTwoTurn(a)

            
       
        
        return state_copy
        
    
    def getLegalActions(self):

        player = self.mCurrentPlayer
      
   
        if player == "P1":
          
            return self.mModel.legalActionsPlayerOne()
        
        else:
      
            return self.mModel.legalActionsPlayerTwo()
            
    
        
        
    
    def GoalTest(self,state):
        if self.mModel.empty() == True:
            return True
        
        
        else:
            return False
        
    
    def updatePercepts(self, percepts):
        
        
        
        self.mModel.updateBoard(percepts[2])
        self.mModel.setTurnFlag(percepts[-1])
        self.mPlayerOnePoints = percepts[0]
        self.mPlayerTwoPoints = percepts[1]
        self.mExtraTurn = percepts[-1]
      
    def applyAction(self, a):
     
        if self.mCurrentPlayer == "P1":
            self.mModel.playerOneTurn(a)
        else:
            self.mModel.playerTwoTurn(a)

    
    
    def getObserveable(self):
        return self.mModel.getPlayerOnePoints(), self.mModel.getPlayerTwoPoints(), self.mModel.getBoard(), self.mModel.getTurnFlag()
    
    def done(self):
        
        while self.mModel.empty() == False:
            return False


        return True
        
        
    
