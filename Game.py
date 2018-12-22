#!/usr/bin/env python
# coding: utf-8

# In[134]:

class Game:
    def __init__(self):
        # initialize empty board
        self.grid =[]
        for count in range(4):
            self.grid.append([0]*(5+count))
        self.grid.append([0]*9)
        for count in range(4):
            self.grid.append([0]*(8-count))

    def __str__(self):
        # string representation
        s=''
        for row in range(4):
            #s = s + ' '*(4-row),str(self.grid[row])+'\n'
            s = ''.join([s,' '*(4-row),str(self.grid[row]),'\n'])
        #s = s + str(self.grid[4])+'\n'
        s=''.join([s,str(self.grid[4]),'\n'])
        for row in range(5,9):
            #s = s + ' '*(row-4),str(self.grid[row])+'\n'
            s = ''.join([s,' '*(row-4),str(self.grid[row]),'\n'])
        return s
    
    def get_grid(self):
        return str(self.grid) 
    def test_grid_2(self,grid):
        self.grid = grid
            
    def test_grid(self):
        # set grid with locations of each cell, and print
        # can be used to test neighbour functions.
        num=1
        for i in range(5):
            for j in range(5+i):
                self.grid[i][j]=str(i)+','+str(j)
        for i in range(5,9):
            for j in range(13-i):
                self.grid[i][j]=str(i)+','+str(j)
        # print
        for row in range(4):
            print ' '*(12-3*row),self.grid[row]
        print self.grid[4]
        for row in range(5,9):
            print ' '*(row*3-12),self.grid[row]
    
    # functions to get neighbour 
    # returning true or false would also suffice
    # currently, will have to check output==0 or ==1
    # None output for edge cases
    def neigh_NE(self,loc):
        #loc[0]=0,1,2,3,4
        if loc[0]<5:
            if loc[0]==0 or loc[1]==4+loc[0]: # in top row or on right edge
                return None
            else:
                return loc[0]-1,loc[1]
        else: #loc[0]=5,6,7,8
            return loc[0]-1,loc[1]+1
    def neigh_E(self,loc):
        if loc[0]<5 and (loc[1] == 4+loc[0]): # on right edge
                return None
        elif loc[1]==12-loc[0]:
            return None
        else:
                return loc[0],loc[1]+1
            
    def neigh_SE(self,loc): #loc[0]=0,1,2,3,4
        if loc[0]<5:
            if loc[0]==4 and loc[1]==8: # on center row, last cell
                return None
            elif loc[0]==4: # on center row
                return loc[0]+1,loc[1]
            else: 
                return loc[0]+1,loc[1]+1
        else:
            if loc[1]==12-loc[0] or loc[0]==8: # on right edge or bottom row
                return None
            else:
                return loc[0]+1,loc[1]
    def neigh_SW(self,loc): #loc[0]=0,1,2,3,4
        if loc[0]<5:
            if loc[0]==4 and loc[1]==0: # on center row, first cell
                return None
            elif loc[0]==4: # on center row
                return loc[0]+1,loc[1]-1
            else: 
                return loc[0]+1,loc[1]
        else: #loc[0]=5,6,7,8
            if loc[1]==0 or loc[0]==8: # on left edge or bottom row
                return None
            else: 
                return loc[0]+1,loc[1]-1
    def neigh_W(self,loc):
        if loc[1] == 0: # on left edge
            return None
        else:
            return loc[0],loc[1]-1
    def neigh_NW(self,loc):
        #loc[0]=0,1,2,3,4
        if loc[0]<5:
            if loc[0]==0 or loc[1]==0: # in top row or on left edge
                return None
            else: 
                return loc[0]-1,loc[1]-1 
        else: #loc[0]=5,6,7,8
            return loc[0]-1,loc[1]
        
    # is Full functions check if specfied array is full
    # and return T/F
    # called by is_full()
        #rr 0,1,2,3,4
        #rl 1,2,3,4
        #ll 0,1,2,3,4
        #lr 1,2,3,4
        #hh 0,1,2,3,4,5,6,7,8
    def is_full_rr(self,n): #n=0,1,2,3,4
        till=5
        repeat=n+4
        for i in range(till):
            if(self.grid[i][i+n]==0):
                return False
        for i in range(till,9-n):
            if(self.grid[i][repeat]==0):
                return False
        return True, 9-n
    def is_full_rl(self,n): # n=1,2,3,4
        till=5-n
        repeat=4-n
        for i in range(till):
            if(self.grid[n+i][i]==0):
                return False
        for i in range(till+n,9):
            if(self.grid[i][repeat]==0):
                return False
        return True, 9-n
    def is_full_ll(self,n): # n=0,1,2,3,4
        till=4
        repeat=n
        for i in range(0,till):
            if(self.grid[i][repeat]==0):
                return False
        for i in range(till,till+n+1):
            if(self.grid[i][repeat+4-i]==0):
                return False
        return True, 5+n
    def is_full_lr(self,n): # n=1,2,3,4
        till=4
        repeat=n+4
        for i in range(n,till):
            if(self.grid[i][repeat]==0):
                return False
        for i in range(till,9):
            if(self.grid[i][repeat+4-i]==0):
                return False
        return True,9-n

    def is_full_hh(self,n): # n=0,1,2,3,4,5,6,7,8
        if n<5: # n=0,1,2,3,4
            for i in range(5+n):
                if(self.grid[n][i]==0):
                    return False
            return True,n+5
        else: # n=5,6,7,8
            for i in range(13-n):
                if(self.grid[n][i]==0):
                    return False
        return True,13-n
    
    def is_full(self):
        output=dict()
        count_cleared=0
        for n in range(5):
            if(self.is_full_rr(n)):
                if 'rr' in output:
                    output['rr'].append(n)
                    count_cleared=count_cleared+self.is_full_rr(n)[1]
                else:
                    output['rr']=[n]
            if(self.is_full_ll(n)):
                if 'll' in output:
                    output['ll'].append(n)
                    count_cleared=count_cleared+self.is_full_ll(n)[1]
                else:
                    output['ll']=[n]
        for n in range(1,5):
            if(self.is_full_rl(n)):
                if 'rl' in output:
                    output['rl'].append(n)
                    count_cleared=count_cleared+self.is_full_rl(n)[1]
                else:
                    output['rl']=[n]
            if(self.is_full_lr(n)):
                if 'lr' in output:
                    output['lr'].append(n)
                    count_cleared=count_cleared+self.is_full_lr(n)[1]
                else:
                    output['lr']=[n]
        for n in range(9):
            if(self.is_full_hh(n)):
                if 'hh' in output:
                    output['hh'].append(n)
                    count_cleared=count_cleared+self.is_full_hh(n)[1]
                else:
                    output['hh']=[n]
        return output,count_cleared

    
    # fill/empty location
    def loc(self,loc,val):
        self.grid[loc[0]][loc[1]]=val
    # check if location is full
    # assuming only 1 or 0 values are possible
    def is_full_loc(self,loc):
        return self.grid[loc[0]][loc[1]]==1
    def empty(self):
        self.grid = map(lambda row:map(lambda cell:0,row),self.grid)
        
    # testing methods
    def rr(self,n,val): # n=0,1,2,3,4 # val=1 or 0
        till=5
        repeat=n+4
        for i in range(till):
            self.grid[i][i+n]=val
        for i in range(till,9-n):
            self.grid[i][repeat]=val
    def rl(self,n,val): # n=1,2,3,4
        till=5-n
        repeat=4-n
        for i in range(till):
            self.grid[n+i][i]=val
        for i in range(till+n,9):
            self.grid[i][repeat]=val
    def lr(self,n,val): # n=1,2,3,4
        till=4
        repeat=n+4
        for i in range(n,till):
            self.grid[i][repeat]=val
        for i in range(till,9):
            self.grid[i][repeat+4-i]=val
    def ll(self,n,val): # n=0,1,2,3,4
        till=4
        repeat=n
        for i in range(0,till):
            self.grid[i][repeat]=val
        for i in range(till,till+n+1):
            self.grid[i][repeat+4-i]=val
    def hh(self,n,val):
        if n<5: # n=0,1,2,3,4
            for i in range(5+n):
                self.grid[n][i]=val
        else: # n=5,6,7,8
            for i in range(13-n):
                self.grid[n][i]=val


'''
#game = Game()
checking neigh functions
print game
locs=[(0,0),(0,2),(0,4),(2,6),(4,8),(6,6),(8,4),(8,2),
     (8,0),(6,0),(4,0),(2,0),(4,4),(2,1),(7,4)]
for loc in locs:
    game.test_grid()
    print loc
    print game.neigh_NE(loc)
    print game.neigh_E(loc)
    print game.neigh_SE(loc)
    print game.neigh_SW(loc)
    print game.neigh_W(loc)
    print game.neigh_NW(loc)
    print '*****'
    
'''

'''
#checking set diag/hh functions for fill and is_full
for i in range(5):
    print('rr ',i)
    game.empty()
    game.rr(i,1)
    print game
    print game.is_full()
    print('*****')
for i in range(5):
    print('ll ',i)
    game.empty()
    game.ll(i,1)
    print game
    print game.is_full()
    print('*****')
for i in range(1,5):
    print('rl ',i)
    game.empty()
    game.rl(i,1)
    print game
    print game.is_full()
    print('*****')
for i in range(1,5):
    print('lr ',i)
    game.empty()
    game.lr(i,1)
    print game
    print game.is_full()
    print('*****')
for i in range(9):
    print('hh ',i)
    game.empty()
    game.hh(i,1)
    print game
    print game.is_full()
    print('*****')
game.empty()
game.hh(8,1)
game.rl(4,1)
game.rr(0,1)
print game
game.rr(0,0)
print game
print game.is_full()

'''
'''

#checking fill_loc, empty_loc and is_full_loc
game.empty()
game.hh(8,1)
game.rl(4,1)
game.rr(2,1)
print game
print game.is_full_loc((5,7))
game.loc((5,7),1)
game.loc((4,0),1)
game.loc((0,2),0)
print game
print game.is_full_loc((5,7))


'''




