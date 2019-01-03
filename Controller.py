# -*- coding: utf-8 -*-

#from google.colab import drive
#drive.mount('/content/gdrive')
#drive.mount("/content/gdrive", force_remount=True)
#path = '/content/gdrive/My Drive/mlhexfrvr/'
path=''

from Agent import Agent
from Game import Game
from Piece import *
import pandas as pd
import numpy as np
import random
import yaml
import re
import sys

#grid_str_1 = '[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]'
__pieces__ = ['Piece_Dot','Piece_Diamond','Piece_Box_R','Piece_Box_L','Piece_Line_R','Piece_Line_L','Piece_Seven_RU', 'Piece_Seven_LU', 'Piece_Seven_RD', 'Piece_Seven_LU', 'Piece_Hook_RU', 'Piece_Hook_LU', 'Piece_Hook_RD', 'Piece_Hook_LD','Piece_T_RU', 'Piece_T_LU', 'Piece_T_RD', 'Piece_T_LD', 'Piece_Semi_U', 'Piece_Semi_D', 'Piece_Semi_RU', 'Piece_Semi_LU', 'Piece_Semi_RD', 'Piece_Semi_LD']
__score_for_move__=40
__score_for_clear__=20 # per title removed
#__reward_for_losing__=-10 # not used
#score_for_clear_bonus=1 # not sure how this works

class Controller(object):
    def __init__(self,lr,d,Qtable):
        self.agent = Agent()
        #self.game = Game()
        #self.score = 0
        self.lr = lr #0.1 # learning rate
        self.d = d #-0.1 # discount rate
        if Qtable is None:
            self.Qtable=dict()
        else:
            self.Qtable=Qtable

    def exit(self):
        ## print 'End of Game (final score = '+str(self.score)+')\n'
        #print self.Qtable
        return None
    
    def get_available_pieces(self):
        pieces = np.random.choice(__pieces__,3)
        ## for piece in pieces:
        ##    klass = globals()[piece]
        ##    p = klass()
        ##    print p
        ##    print '___'
        return pieces
    
    def get_action_key(self,action_tuple):
    	return str(__pieces__.index(action_tuple[0]))+','+str(action_tuple[1][0])+','+str(action_tuple[1][1])
    
    def add_grid_to_Qtable(self,grid_str):
        if not grid_str in self.Qtable:
            self.Qtable[grid_str]={}
            return True
        return False
        # if Q value for an action dne, randomly initialize it and use it.
    
    def max_expQval(self,grid_str):
        max_= 0
        for k,v in self.Qtable[grid_str].iteritems():
            if v>max_:
                max_=v
        return max_
    
    def init_action_reward_to_Qtable(self,grid_str,action_str):
        # at this point grid_str is definitely in Qtable
        self.Qtable[grid_str][action_str] = random.random()
    
    def add_action_reward_to_Qtable(self,grid_str,action_str,reward):
        # at this point grid_str is definitely in Qtable
        # and action_str is in Qtable[grid_str]
        #if action_str in self.Qtable[grid_str]:
        current_Qval = self.Qtable[grid_str][action_str]
        self.Qtable[grid_str][action_str] = current_Qval + self.lr*(reward+self.d*self.max_expQval(grid_str)-current_Qval)
            
    def play_learnt_game(self):
        ## print "New Game"
        self.game = Game()
        self.score = 0
        ## print self.game

        move=1
        while True: # to test i<200, should be while(True)
            ## print '** Move ',str(move),': **'
            grid_str = self.game.get_grid()
            
            possible_actions=[]
            pieces = self.get_available_pieces()
            for piece in pieces:
                # check if can_put in any location
                klass = globals()[piece]
                p = klass()
                for l0 in range(5):
                    for l1 in range(5+l0):
                        if p.can_put(self.game,(l0,l1)):
                            possible_actions.append((piece,(l0,l1)))
                for l0 in range(5,9):
                    for l1 in range(13-l0):
                        if p.can_put(self.game,(l0,l1)):
                            possible_actions.append((piece,(l0,l1)))

            if len(possible_actions)==0: 
                break
            else:
            	self.add_grid_to_Qtable(grid_str)
                if len(possible_actions)==1:
                    action=possible_actions[0]
                    #self.init_action_reward_to_Qtable(grid_str,str(action))
                    self.init_action_reward_to_Qtable(grid_str,self.get_action_key(action))
                else:
                    # pick highest Qval action for current grid                  
                    action = possible_actions[np.random.choice(len(possible_actions),1)[0]]  # random action than can be taken
                    try:                        
                        #val=self.Qtable[grid_str][str(action)]
                        val=self.Qtable[grid_str][self.get_action_key(action)]
                    except KeyError:
                        #self.init_action_reward_to_Qtable(grid_str,str(action))
                        #val=self.Qtable[grid_str][str(action)]
                        self.init_action_reward_to_Qtable(grid_str,self.get_action_key(action))
                        val=self.Qtable[grid_str][self.get_action_key(action)]
                    for index in range(len(possible_actions)):
                        try:
                            #if self.Qtable[grid_str][str(possible_actions[index])]>val:
                            #    val = self.Qtable[grid_str][str(possible_actions[index])]
                            #    action = possible_actions[index]
                            if self.Qtable[grid_str][self.get_action_key(possible_actions[index])]>val:
                                val = self.Qtable[grid_str][self.get_action_key(possible_actions[index])]
                                action = possible_actions[index]
                        except KeyError:
                            continue
               
                self.agent.move(action[0],self.game,action[1]) 
                ## print 'moved:\n', action[0],' at ',self.game,action[1]
                move_reward=__score_for_move__
                # get h and d's that are now full and set them to 0
                is_full_result = self.game.is_full()
                fulls = is_full_result[0]
                ## print is_full_result
                for i in range(1,len(is_full_result[1])+1):
                    move_reward = move_reward + is_full_result[1][i-1]*i
                self.score = self.score + move_reward

                # make full null
                for k, vs in fulls.items():
                    for v in vs:
                        getattr(self.game, k)(v,0)
                        #print 'cleared: ', (k,v)
                ## print self.game
                ## print 'current score: ',self.score
                #self.add_action_reward_to_Qtable(grid_str,str(action),move_reward)
                self.add_action_reward_to_Qtable(grid_str,self.get_action_key(action),move_reward)
                #print self.Qtable
            move=move+1
        self.exit()

lr = 0.2
dr = 0.5
if len(sys.argv)==1:
	num_trials = 10
else:
	num_trials=int(sys.argv[1])

scores_file=open(path+'scores.csv','a+')#,encoding="utf-8")
scores = scores_file.readlines()
if len(scores) == 0:
    scores_file.write('game_id|final_score\n')
    game_id = 1
elif len(scores)==1:
    game_id = 1
else:
    last_game_id = int(scores[len(scores)-1].split('|')[0])
    game_id = last_game_id + 1

with open(path+'QTable.yaml', 'a+') as f:
    loaded_QTable = yaml.safe_load(f)
    if loaded_QTable is None:
        print '***No previous Q table loaded***'
    else:
        print '***Previous Q table loaded***'
    for trial in range(num_trials):
        controller = Controller(lr,dr,loaded_QTable)
        controller.play_learnt_game()
        loaded_QTable = controller.Qtable
        scores_file.write(str(game_id)+'|'+str(controller.score)+'\n')
        print '*** Game_id = '+str(game_id)+' (trial='+ str(trial+1) +'), final score = '+str(controller.score)+' ***'
        game_id=game_id+1
    f.seek(0)
    f.truncate()
    yaml.dump(loaded_QTable, f)
scores_file.flush()
scores_file.close()
