
import random


# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 


## Classes

## Dice class 
class Dice ():

    def __init__(self, faces):
        self.faces = faces
    ### end function

    def roll_dice(self):
        return random.randrange(1,self.faces)
    ### end function
#### End of Dice class

## Snake class
class Snake ():

    def __init__(self, start,end):
        self.start = start
        self.end = end
    ### end function

    def get_start(self):
        return self.start
    ### end function

    def get_end(self):
        return self.end
    ### end function

#### End of Snake class


## Ladder class
class Ladder ():

    def __init__(self, start,end):
        self.start = start
        self.end = end
    ### end function

    def get_start(self):
        return self.start
    ### end function

    def get_end(self):
        return self.end
    ### end function

#### End of Ladder class

## Player class
class Player ():

    def __init__(self, name):
        self.pos = 0
        self.name = name
    ### end function

    def get_pos(self):
        return self.pos
    ### end function

    def set_pos(self,p):
        self.pos = p
    ### end function

#### End of Player class

## Board class
class Board ():

    def __init__(self):
        ## Create a player list and add two players
        self.player_list = []
        p = Player("Andrew")
        self.player_list.append(p)
        q = Player("Adam")
        self.player_list.append(q)

        ## create snake list
        self.snake_list = []
        s = Snake(32,14)
        self.snake_list.append(s)
        s = Snake(56,34)
        self.snake_list.append(s)
        s = Snake(92,50)
        self.snake_list.append(s)

        ## create ladder list
        self.ladder_list = []
        l = Ladder(3,12)
        self.ladder_list.append(l)
        s = Snake(22,43)
        self.ladder_list.append(s)
        s = Snake(65,72)
        self.ladder_list.append(s)

        ### Create a dice
        self.dice = Dice(6)

    ### end function

#### End of Board class

#### Game class
class Game():
    def __init__(self):
        ## Create a board
        self.board = Board()
        self.done = False
    ## End of function

    def play_game(self):
        
        while self.done == False:
            for p in self.board.player_list:
                d = self.board.dice.roll_dice()
                p.pos = p.pos + d
                print (p.name, p.pos)

                for s in self.board.snake_list:
                    if s.start == p.pos:
                        print (p.name, "hit snake", str(p.pos) + "-->" + str(s.end))
                        p.pos = s.end
                        

                for l in self.board.ladder_list:
                    if l.start == p.pos:
                        print (p.name, "hit ladder", str(p.pos) + "-->" + str(l.end))
                        p.pos = l.end
                        

                if p.pos  > 100:
                    self.done = True
            ## next

### end of Game class



### -- GMain Program ###
g = Game()
g.play_game()

