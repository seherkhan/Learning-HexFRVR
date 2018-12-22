# each put method checks if space independent of can_put before executing.
from Game import Game

class Piece_Line_R(object):
    def get_name(self):
        return 'Piece_Line_R'
    def __str__(self):
        return 'o\n o\n  o\n   o\n'
    def can_put(self,game,loc):
        #rType: bool
        #check
        tmp_loc=loc
        for i in range(4):
            if tmp_loc is None or game.is_full_loc(tmp_loc):
                return False
            else:
                tmp_loc = game.neigh_SE(tmp_loc)
        if tmp_loc is None or game.is_full_loc(tmp_loc):
            return False
        else:
            return True
    def put(self,game,loc):
        tmp_loc=loc
        for i in range(4):
            if tmp_loc is None or game.is_full_loc(tmp_loc):
                return False
            else:
                tmp_loc = game.neigh_SE(tmp_loc)
        if tmp_loc is None or game.is_full_loc(tmp_loc):
            return False
        else:
            for i in range(4):
                game.loc(loc,1)
                loc = game.neigh_SE(loc)
            return True
class Piece_Line_L(object):
    def get_name(self):
        return 'Piece_Line_L'    
    def __str__(self):
        return '    o\n   o\n  o\n o\n'
    def can_put(self,game,loc):
        #rType: bool
        #check
        tmp_loc=loc
        for i in range(4):
            #print tmp_loc
            if tmp_loc is None or game.is_full_loc(tmp_loc):
                return False
            else:
                tmp_loc = game.neigh_SW(tmp_loc)
        if tmp_loc is None or game.is_full_loc(tmp_loc):
            return False
        else:
            return True
            print True
    def put(self,game,loc):
        tmp_loc=loc
        for i in range(4):
            if tmp_loc is None or game.is_full_loc(tmp_loc):
                return False
            else:
                tmp_loc = game.neigh_SW(tmp_loc)
        if tmp_loc is None or game.is_full_loc(tmp_loc):
            return False
        else:
            for i in range(4):
                game.loc(loc,1)
                loc = game.neigh_SW(loc)
            return True
class Piece_Line_H(object):
    def get_name(self):
        return 'Piece_Line_H'
    def __str__(self):
        return 'o o o o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        tmp_loc=loc
        for i in range(4):
            if tmp_loc is None or game.is_full_loc(tmp_loc):
                return False
            else:
                tmp_loc = game.neigh_E(tmp_loc)
        if tmp_loc is None or game.is_full_loc(tmp_loc):
            return False
        else:
            return True
    def put(self,game,loc):
        tmp_loc=loc
        for i in range(4):
            if tmp_loc is None or game.is_full_loc(tmp_loc):
                return False
            else:
                tmp_loc = game.neigh_E(tmp_loc)
        # if space exists, put
        if tmp_loc is None or game.is_full_loc(tmp_loc):
            return False
        else:
            for i in range(4):
                game.loc(loc,1)
                loc = game.neigh_E(loc)
            #return True
class Piece_Dot(object):
    def get_name(self):
        return 'Piece_Dot'    
    def __str__(self):
        return 'o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        return True
        
    def put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        else:
            game.loc(loc,1)
            return True
class Piece_Box_R(object):
    def get_name(self):
        return 'Piece_Box_R'
    def __str__(self):
        return 'o o\n o o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        side_loc=game.neigh_E(loc)
        if  side_loc is None or game.is_full_loc(side_loc) or             game.neigh_SE(loc) is None or game.is_full_loc(game.neigh_SE(loc)) or             game.neigh_SE(side_loc) is None or game.is_full_loc(game.neigh_SE(side_loc)):
            return False
        return True
        
    def put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        side_loc=game.neigh_E(loc)
        if  side_loc is None or game.is_full_loc(side_loc) or             game.neigh_SE(loc) is None or game.is_full_loc(game.neigh_SE(loc)) or             game.neigh_SE(side_loc) is None or game.is_full_loc(game.neigh_SE(side_loc)):
            return False
                        
        # if space exists, put
        game.loc(loc,1)
        game.loc(side_loc,1)
        game.loc(game.neigh_SE(loc),1)
        game.loc(game.neigh_SE(side_loc),1)
        return True
class Piece_Box_L(object):
    def get_name(self):
        return 'Piece_Box_L'
    def __str__(self):
        return ' o o\no o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        side_loc=game.neigh_E(loc)
        if  side_loc is None or game.is_full_loc(side_loc) or            game.neigh_SW(loc) is None or game.is_full_loc(game.neigh_SW(loc)) or             game.neigh_SW(side_loc) is None or game.is_full_loc(game.neigh_SW(side_loc)):
            return False
        return True
        
    def put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        side_loc=game.neigh_E(loc)
        if  side_loc is None or game.is_full_loc(side_loc) or            game.neigh_SW(loc) is None or game.is_full_loc(game.neigh_SW(loc)) or             game.neigh_SW(side_loc) is None or game.is_full_loc(game.neigh_SW(side_loc)):
            return False
                        
        # if space exists, put
        game.loc(loc,1)
        game.loc(side_loc,1)
        game.loc(game.neigh_SW(loc),1)
        game.loc(game.neigh_SW(side_loc),1)
        return True
class Piece_Diamond(object):
    def get_name(self):
        return 'Piece_Diamond'
    def __str__(self):
        return ' o \no o\n o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        se_loc=game.neigh_SE(loc)
        if  se_loc is None or game.is_full_loc(se_loc) or             game.neigh_SW(loc) is None or game.is_full_loc(game.neigh_SW(loc)) or             game.neigh_SW(se_loc) is None or game.is_full_loc(game.neigh_SW(se_loc)):
            return False
        return True
        
    def put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        se_loc=game.neigh_SE(loc)
        if  se_loc is None or game.is_full_loc(se_loc) or             game.neigh_SW(loc) is None or game.is_full_loc(game.neigh_SW(loc)) or             game.neigh_SW(se_loc) is None or game.is_full_loc(game.neigh_SW(se_loc)):
            return False
                        
        # if space exists, put
        game.loc(loc,1)
        game.loc(se_loc,1)
        game.loc(game.neigh_SW(loc),1)
        game.loc(game.neigh_SW(se_loc),1)
        return True

class Piece_Seven_RU(object):
    def get_name(self):
        return 'Piece_Seven_RU'
    def __str__(self):
        return 'o o\n o\no'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_SW(cells[1]) is None:
            return False
        cells.append(game.neigh_SW(cells[1]))
        if game.neigh_SW(cells[2]) is None:
            return False
        cells.append(game.neigh_SW(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_SW(cells[1]) is None:
            return False
        cells.append(game.neigh_SW(cells[1]))
        if game.neigh_SW(cells[2]) is None:
            return False
        cells.append(game.neigh_SW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Seven_LU(object):
    def get_name(self):
        return 'Piece_Seven_LU'
    def __str__(self):
        return 'o o\n o\n  o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_SE(cells[1]) is None:
            return False
        cells.append(game.neigh_SE(cells[1]))
        if game.neigh_SE(cells[2]) is None:
            return False
        cells.append(game.neigh_SE(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False 
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_SE(cells[1]) is None:
            return False
        cells.append(game.neigh_SE(cells[1]))
        if game.neigh_SE(cells[2]) is None:
            return False
        cells.append(game.neigh_SE(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False 
class Piece_Seven_RD(object):
    def get_name(self):
        return 'Piece_Seven_RD'
    def __str__(self):
        return 'o\n o\no o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_NW(cells[1]) is None:
            return False
        cells.append(game.neigh_NW(cells[1]))
        if game.neigh_NW(cells[2]) is None:
            return False
        cells.append(game.neigh_NW(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False 
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_NW(cells[1]) is None:
            return False
        cells.append(game.neigh_NW(cells[1]))
        if game.neigh_NW(cells[2]) is None:
            return False
        cells.append(game.neigh_NW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False 
class Piece_Seven_LD(object):
    def get_name(self):
        return 'Piece_Seven_LD'
    def __str__(self):
        return '  o\n o\no o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_NE(cells[1]) is None:
            return False
        cells.append(game.neigh_NE(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_NE(cells[1]) is None:
            return False
        cells.append(game.neigh_NE(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False

class Piece_Hook_RU(object):
    def get_name(self):
        return 'Piece_Hook_RU'
    def __str__(self):
        return ' o\no o\n   o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NE(loc) is None:
            return False
        cells.append(game.neigh_NE(loc))
        if game.neigh_SE(cells[1]) is None:
            return False
        cells.append(game.neigh_SE(cells[1]))
        if game.neigh_SE(cells[2]) is None:
            return False
        cells.append(game.neigh_SE(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NE(loc) is None:
            return False
        cells.append(game.neigh_NE(loc))
        if game.neigh_SE(cells[1]) is None:
            return False
        cells.append(game.neigh_SE(cells[1]))
        if game.neigh_SE(cells[2]) is None:
            return False
        cells.append(game.neigh_SE(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Hook_LU(object):
    def get_name(self):
        return 'Piece_Hook_LU'
    def __str__(self):
        return '  o\n o o\no'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NW(loc) is None:
            return False
        cells.append(game.neigh_NW(loc))
        if game.neigh_SW(cells[1]) is None:
            return False
        cells.append(game.neigh_SW(cells[1]))
        if game.neigh_SW(cells[2]) is None:
            return False
        cells.append(game.neigh_SW(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NW(loc) is None:
            return False
        cells.append(game.neigh_NW(loc))
        if game.neigh_SW(cells[1]) is None:
            return False
        cells.append(game.neigh_SW(cells[1]))
        if game.neigh_SW(cells[2]) is None:
            return False
        cells.append(game.neigh_SW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Hook_RD(object):
    def get_name(self):
        return 'Piece_Hook_RD'
    def __str__(self):
        return '   o\no o\n o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_SE(loc) is None:
            return False
        cells.append(game.neigh_SE(loc))
        if game.neigh_NE(cells[1]) is None:
            return False
        cells.append(game.neigh_NE(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_SE(loc) is None:
            return False
        cells.append(game.neigh_SE(loc))
        if game.neigh_NE(cells[1]) is None:
            return False
        cells.append(game.neigh_NE(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Hook_LD(object):
    def get_name(self):
        return 'Piece_Hook_LD'
    def __str__(self):
        return 'o\n o o\n  o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_SW(loc) is None:
            return False
        cells.append(game.neigh_SW(loc))
        if game.neigh_NW(cells[1]) is None:
            return False
        cells.append(game.neigh_NW(cells[1]))
        if game.neigh_NW(cells[2]) is None:
            return False
        cells.append(game.neigh_NW(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_SW(loc) is None:
            return False
        cells.append(game.neigh_SW(loc))
        if game.neigh_NW(cells[1]) is None:
            return False
        cells.append(game.neigh_NW(cells[1]))
        if game.neigh_NW(cells[2]) is None:
            return False
        cells.append(game.neigh_NW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_T_RU(object):
    def get_name(self):
        return 'Piece_T_RU'
    def __str__(self):
        return 'o o o\n   o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_E(cells[1]) is None:
            return False
        cells.append(game.neigh_E(cells[1]))
        if game.neigh_SW(cells[2]) is None:
            return False
        cells.append(game.neigh_SW(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_E(cells[1]) is None:
            return False
        cells.append(game.neigh_E(cells[1]))
        if game.neigh_SW(cells[2]) is None:
            return False
        cells.append(game.neigh_SW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_T_LU(object):
    def get_name(self):
        return 'Piece_T_LU'
    def __str__(self):
        return 'o o o\n o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_W(cells[1]) is None:
            return False
        cells.append(game.neigh_W(cells[1]))
        if game.neigh_SE(cells[2]) is None:
            return False
        cells.append(game.neigh_SE(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_W(cells[1]) is None:
            return False
        cells.append(game.neigh_W(cells[1]))
        if game.neigh_SE(cells[2]) is None:
            return False
        cells.append(game.neigh_SE(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
    
class Piece_T_RD(object):
    def get_name(self):
        return 'Piece_T_RD'
    def __str__(self):
        return '   o\no o o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_E(cells[1]) is None:
            return False
        cells.append(game.neigh_E(cells[1]))
        if game.neigh_NW(cells[2]) is None:
            return False
        cells.append(game.neigh_NW(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_E(cells[1]) is None:
            return False
        cells.append(game.neigh_E(cells[1]))
        if game.neigh_NW(cells[2]) is None:
            return False
        cells.append(game.neigh_NW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_T_LD(object):
    def get_name(self):
        return 'Piece_T_LD'
    def __str__(self):
        return ' o\no o o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_W(cells[1]) is None:
            return False
        cells.append(game.neigh_W(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_W(cells[1]) is None:
            return False
        cells.append(game.neigh_W(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False

class Piece_Semi_U(object):
    def get_name(self):
        return 'Piece_Semi_U'
    def __str__(self):
        return 'o  o\n o o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_SE(loc) is None:
            return False
        cells.append(game.neigh_SE(loc))
        if game.neigh_E(cells[1]) is None:
            return False
        cells.append(game.neigh_E(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_SE(loc) is None:
            return False
        cells.append(game.neigh_SE(loc))
        if game.neigh_E(cells[1]) is None:
            return False
        cells.append(game.neigh_E(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Semi_D(object):
    def get_name(self):
        return 'Piece_Semi_D'
    def __str__(self):
        return ' o o\no   o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NW(loc) is None:
            return False
        cells.append(game.neigh_NW(loc))
        if game.neigh_W(cells[1]) is None:
            return False
        cells.append(game.neigh_W(cells[1]))
        if game.neigh_SW(cells[2]) is None:
            return False
        cells.append(game.neigh_SW(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NW(loc) is None:
            return False
        cells.append(game.neigh_NW(loc))
        if game.neigh_W(cells[1]) is None:
            return False
        cells.append(game.neigh_W(cells[1]))
        if game.neigh_SW(cells[2]) is None:
            return False
        cells.append(game.neigh_SW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Semi_RU(object):
    def get_name(self):
        return 'Piece_Semi_RU'
    def __str__(self):
        return 'o\n o\no o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_NE(cells[1]) is None:
            return False
        cells.append(game.neigh_NE(cells[1]))
        if game.neigh_NW(cells[2]) is None:
            return False
        cells.append(game.neigh_NW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
        
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_E(loc) is None:
            return False
        cells.append(game.neigh_E(loc))
        if game.neigh_NE(cells[1]) is None:
            return False
        cells.append(game.neigh_NE(cells[1]))
        if game.neigh_NW(cells[2]) is None:
            return False
        cells.append(game.neigh_NW(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Semi_RD(object):
    def get_name(self):
        return 'Piece_Semi_RD'
    def __str__(self):
        return 'o o\n   o\n o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NE(loc) is None:
            return False
        cells.append(game.neigh_NE(loc))
        if game.neigh_NW(cells[1]) is None:
            return False
        cells.append(game.neigh_NW(cells[1]))
        if game.neigh_W(cells[2]) is None:
            return False
        cells.append(game.neigh_W(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NE(loc) is None:
            return False
        cells.append(game.neigh_NE(loc))
        if game.neigh_NW(cells[1]) is None:
            return False
        cells.append(game.neigh_NW(cells[1]))
        if game.neigh_W(cells[2]) is None:
            return False
        cells.append(game.neigh_W(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Semi_LU(object):
    def get_name(self):
        return 'Piece_Semi_LU'
    def __str__(self):
        return '  o\n o\no o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_NW(cells[1]) is None:
            return False
        cells.append(game.neigh_NW(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_W(loc) is None:
            return False
        cells.append(game.neigh_W(loc))
        if game.neigh_NW(cells[1]) is None:
            return False
        cells.append(game.neigh_NW(cells[1]))
        if game.neigh_NE(cells[2]) is None:
            return False
        cells.append(game.neigh_NE(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False
class Piece_Semi_LD(object):
    def get_name(self):
        return 'Piece_Semi_LD'
    def __str__(self):
        return ' o o\no\n o'
    def can_put(self,game,loc):
        #rType: bool
        #check
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NW(loc) is None:
            return False
        cells.append(game.neigh_NW(loc))
        if game.neigh_NE(cells[1]) is None:
            return False
        cells.append(game.neigh_NE(cells[1]))
        if game.neigh_E(cells[2]) is None:
            return False
        cells.append(game.neigh_E(cells[2]))
        if map(game.is_full_loc,cells).count(False) == len(cells):
            return True
        else:
            return False
    def put(self,game,loc):
        if game.is_full_loc(loc):
            return False
        cells=[]
        cells.append(loc)
        if game.neigh_NW(loc) is None:
            return False
        cells.append(game.neigh_NW(loc))
        if game.neigh_NE(cells[1]) is None:
            return False
        cells.append(game.neigh_NE(cells[1]))
        if game.neigh_E(cells[2]) is None:
            return False
        cells.append(game.neigh_E(cells[2]))
        
        if map(game.is_full_loc,cells).count(False) == len(cells):
            map(lambda cell: game.loc(cell,1),cells)
            return True
        else:
            return False

'''
# testing put # works for line_R, line_L, line_H, Dot, Box_R, Box_L
# Seven_LU, Seven_RU, Seven_LD, Seven_RD, semi_,U,DRU,LU,RD,LD works with new format
# Hooks and T's also work
p = Piece_Semi_LD()
print p
game = Game()
game.loc((0,0),1)
game.loc((1,1),1)
game.loc((2,2),1)
game.loc((3,3),1)
game.loc((4,2),1)
print game
#print p.put(game,(0,1))
#print p.put(game,(3,1))
#print p.put(game,(8,4))
#print p.put(game,(1,5))
#print p.put(game,(2,6))
#print p.put(game,(5,1))
#print p.put(game,(4,1))
#print p.put(game,(7,3))
print p.put(game,(6,3))
#print p.put(game,(0,0))
print game

'''
'''
game = Game()
#game.test_grid()
game.test_grid_2([
        [0, 1, 0, 0, 0],
   [0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 1, 0, 0],
 [1, 0, 0, 0, 1, 1, 0, 1],
[0, 0, 0, 1, 1, 0, 1, 0, 0],
 [0, 1, 0, 0, 1, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 1],
   [1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]])
print game

p = Piece_Line_L()
print p
print p.can_put(game,(1,1))
print p.put(game,(1,1))
'''



