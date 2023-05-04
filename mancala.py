class Mancala:
    def  __init__(self):
        self.mBoard = [4,4,4,4,4,4,4,4,4,4,4,4,4,4]
        self.mBoard[0] = 0
        self.mBoard[7] = 0 
      
        self.mExtraTurnFlag = False
        
        

        
        
       
    def updateBoard(self, board):
        self.mBoard = board
    def getTurnFlag(self):
        return self.mExtraTurnFlag

    def setTurnFlag(self, assignment):
        self.mExtraTurnFlag = assignment
    
    def getPlayerOnePoints(self):
        return self.mBoard[0]
    
    def getPlayerTwoPoints(self):
        return self.mBoard[7]
    
    def getBoard(self):
        return self.mBoard

        
        

    def playerOneTurn(self, H):
        
       
        stones = self.mBoard[H]
        self.mBoard[H] = 0
       
        POS = 0
        for stone in range(1, stones+1):
          
            POS = H + stone
            
            if POS >= 7:
                POS = POS + 1
            
            if POS >= 14:
                # recalculate pos
                POS = POS % 14
             

                

            self.mBoard[POS] += 1
   
            
        
        self.capture_or_extra_or_nothing(POS, "P1")
    def playerTwoTurn(self, H):
    
        stones = self.mBoard[H]
        
        self.mBoard[H] = 0
        POS = 0
        for stone in range(1, stones+1):
            POS = (H + stone % 14) + 1
         
            
            if POS >= 14:
                # recalculate pos
                POS = (POS % 14) + 1
                
            if POS == 0:
                POS = POS + 1
                
                
            self.mBoard[POS] += 1
        
        self.capture_or_extra_or_nothing(POS, "P2")
    
    def capture_or_extra_or_nothing(self, end_pos, P):
        # looks at where it ended, and determines if the hole is EMPTY (will have one from the move/drop prev)
        if P == "P1":
            
            if end_pos == 0:
                self.mExtraTurnFlag == True
                
            elif self.mBoard[end_pos] == 1:
        
                self.mBoard[end_pos] = 0 
              
                    
                capture_stones = self.mBoard[-end_pos]
                self.mBoard[-end_pos] = 0
                self.mBoard[0] += capture_stones + 1
                
        
        else:
            if end_pos == 7:
                self.mExtraTurnFlag == True
                
            
            elif self.mBoard[end_pos] == 1:
                self.mBoard[end_pos] = 0
                
                capture_stones = self.mBoard[-end_pos]
                self.mBoard[-end_pos] = 0
                self.mBoard[7] += capture_stones + 1
                

                    
                    
    def legalActionsPlayerOne(self):
        
        playable_holes = []
        
        for i in range(1, 7):
            
            if self.mBoard[i] != 0:
                playable_holes.append(i)
                
        return playable_holes
            
            
    def legalActionsPlayerTwo(self):
        
        playable_holes = []
        
        for i in range(8, 14):
            if self.mBoard[i] != 0:
                playable_holes.append(i)
                
        return playable_holes
    
    
    def empty(self):
        sideone = 0
        sidetwo = 0
        for i in range(1,6):
            if self.mBoard[i] == 0:
                sideone += 1
                
        
        
        for i in range(8, 14):
            if self.mBoard[i] == 0:
                sidetwo += 1
                
        if sideone == 6 or sidetwo == 6:
            return True
        
    
        return False
    
    def determineWinner(self):
        player_one = self.mBoard[0]
        
        player_two = self.mBoard[7]
        
        if player_one > player_two:
            print("P1")
        
        elif player_one == player_two:
           print("TIE")
        
        else:
             print("P2")


    def printState(self):
        print(self.mBoard)
            


  
            
