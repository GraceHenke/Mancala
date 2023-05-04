from model import Model
from mancala import Mancala
import random 

class RandomAgent:
    def __init__(self, env):
        self.model = Model(env)

    def agentFunction(self, percepts, player):
        self.model.updatePlayer(player)
        self.model.updatePercepts(percepts)
        
        
        actions = self.model.getLegalActions()
        if actions == []:
            return None
        
        action = random.choice(actions)
        
     

        return action

    

def RandomAgentFunction():
    env = Model(Mancala())
    P1 = RandomAgent(Mancala())
    P2 = RandomAgent(Mancala())

    # To view the state of the board: env.mModel.printState()
    while not env.done():

        # P1 TURN
        env.updatePlayer("P1")
        percepts = env.getObserveable()
        
        
        action = P1.agentFunction(percepts, "P1")
        
        if action == None:
            break
        

        env.applyAction(action)
        
        
        
        
        if P1.model.mExtraTurn == True:
            percepts = env.getObserveable()
            action = P1.agentFunction(percepts, "P2")
            
            if action == None:
                break
            
            env.applyAction(action)
            
            P1.model.mExtraTurn == False

        
        
        #P2 TURN
        env.updatePlayer("P2")
        percepts = env.getObserveable()
        
        
        action = P2.agentFunction(percepts, "P2")
      
        
        if action == None:
            break
        
        env.applyAction(action)
        
        
  
   
 
        if P2.model.mExtraTurn == True:
            percepts = env.getObserveable()
            action = P2.agentFunction(percepts, "P2")
            
            if action == None:
                break
            env.applyAction(action)

            P2.model.mExtraTurn == False

    env.mModel.determineWinner()
    
    




def main():
    RandomAgentFunction()
    
    
    
    

if '__main__':
    main()
    