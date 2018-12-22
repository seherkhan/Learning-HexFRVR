from Game import Game
from Piece import *

class Agent(object):
    def move(self,piece_name,game,loc):
        klass = globals()[piece_name]
        p = klass()
        p.put(game,loc) # if space is available has already been checked
        print 'moved:\n', p,' at ',loc
    def make_move(self,game,actions):
        for i in range(len(actions)):
            picked_action = actions[i]
            for l0 in range(5):
                for l1 in range(5+l0):
                    if self.move(picked_action,game,(l0,l1)):
                        #attempt move
                        return True
            for l0 in range(5,9):
                for l1 in range(13-l0):
                    if self.move(picked_action,game,(l0,l1)):
                        # attempt move
                        return True
        return False
'''        
game = Game()
print game
#game.loc((0,0),1)
actions = game.get_available_pieces()
print actions
agent = Agent()
agent.make_move(game, actions)
#agent.move(actions[0],game,(0,0))
print game
'''
