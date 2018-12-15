#!/usr/bin/env python
# coding: utf-8

# In[4]:


from Agent import Agent
from Game import Game
from Piece import *
import numpy as np


__pieces__ = ['Piece_Dot','Piece_Diamond','Piece_Box_R','Piece_Box_L','Piece_Line_R','Piece_Line_L','Piece_Seven_RU', 'Piece_Seven_LU', 'Piece_Seven_RD', 'Piece_Seven_LU', 'Piece_Hook_RU', 'Piece_Hook_LU', 'Piece_Hook_RD', 'Piece_Hook_LD','Piece_T_RU', 'Piece_T_LU', 'Piece_T_RD', 'Piece_T_LD', 'Piece_Semi_U', 'Piece_Semi_D', 'Piece_Semi_RU', 'Piece_Semi_LU', 'Piece_Semi_RD', 'Piece_Semi_LD']
__score_for_move__=40
__score_for_clear__=20 # per title removed
#score_for_clear_bonus=1 # not sure how this works

class Controller(object):
    def __init__(self):
        self.agent = Agent()
        self.game = Game()
        self.score = 0
    def play(self):
        print "New Game"
        print self.game
        i=1
        while i<200: # to test, should be while(True)
            print '****** Move ',str(i),': ******'
            i=i+1
            actions = self.get_available_pieces()
            # TODO agent strategy
            if(not self.agent.make_move(self.game,actions)):
                # no moves available # this should be checked by game not agent
                self.exit()
                break
            else:
                # if move available, move has been made in if statement
                self.score=self.score+__score_for_move__
                # get h and d's that are now full and set them to 0
                is_full_result = self.game.is_full()
                fulls = is_full_result[0]
                self.score = self.score + is_full_result[1]*__score_for_clear__
                # make full null
                for k, vs in fulls.items():
                    for v in vs:
                        getattr(self.game, k)(v,0)
                        print 'cleared: ', (k,v)
                print self.game
                print 'current score: ',self.score
            
    def exit(self):
        print 'End of Game'
    
    def get_available_pieces(self):
        pieces = np.random.choice(__pieces__,3)
        for piece in pieces:
            klass = globals()[piece]
            p = klass()
            print p
            print '___'
        return pieces
        
controller = Controller()
controller.play()

