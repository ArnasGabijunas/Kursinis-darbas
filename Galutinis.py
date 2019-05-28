import pygame
import random

pygame.init()

gameDisplay=pygame.display.set_mode((374,374))
pygame.display.set_caption('Good luck!')



GameOver=False
HotCount=36
WarmCount=36
CoolCount=36
Matrix = [[0 for abc in range(6)] for ABC in range(6)] 

#1) IMAGE start#####################################################################
frame = pygame.image.load('frame.png')
background = pygame.image.load('background.png')
gameDisplay.blit(background, (0,0))
gameDisplay.blit(frame, (0,0))
pygame.display.update()
#1) IMAGES end#####################################################################



#2) OBJECT start#####################################################################
class BoardPiece:
    def __init__ (self, temp, value, xCorner, yCorner, highlight, filename, legal):
        self.temp = temp #1 is Layer1, cool. layer2 is warm. layer3 is hot
        self.value = value
        self.xCorner = xCorner
        self.yCorner = yCorner #self.abc=Anything. doing a .abc next time will store it in the Anything 'field'
        self.highlight = highlight
        self.filename = filename
        self.legal = legal
#2) OBJECT end#####################################################################       
        
        
        
#3 DATA STRUCTURE OF BOARD + INITIAL DISPLAY start############################################    
def BeginGame():
    pygame.display.set_caption('Good luck!')
    for x in range(6):
        for y in range(6):
            pieceSpawn = random.randint(1,8) # 1 TO 4 IS NUMERICAL. 5 TO 8 IS CHESS.    '
            if x in range(2,4) and y in range(2,4):
                if pieceSpawn ==4:
                    pieceSpawn =1
            if pieceSpawn == 1:
                CurrentFileName = "hot1"
                gameDisplay.blit(pygame.image.load('hot1.png'), (x*60+7, y*60+7))
            elif pieceSpawn == 2 :
                CurrentFileName = "hot2"            
                gameDisplay.blit(pygame.image.load('hot2.png'), (x*60+7, y*60+7))
            elif pieceSpawn == 3 :
                CurrentFileName = "hot3"            
                gameDisplay.blit(pygame.image.load('hot3.png'), (x*60+7, y*60+7))
            elif pieceSpawn == 4 :
                CurrentFileName = "hot4"            
                gameDisplay.blit(pygame.image.load('hot4.png'), (x*60+7, y*60+7))
                
     ####################       # 5 is Rook. 6 is Bishop. 7 is Queen. 8 is Knight  ####################3
            elif pieceSpawn == 5 :
                CurrentFileName = "hot5"            
                gameDisplay.blit(pygame.image.load('hot5.png'), (x*60+7, y*60+7))
            elif pieceSpawn == 6 :
                CurrentFileName = "hot6"            
                gameDisplay.blit(pygame.image.load('hot6.png'), (x*60+7, y*60+7))
            elif pieceSpawn == 7 :
                CurrentFileName = "hot7"            
                gameDisplay.blit(pygame.image.load('hot7.png'), (x*60+7, y*60+7))
            elif pieceSpawn == 8 :
                CurrentFileName = "hot8"            
                gameDisplay.blit(pygame.image.load('hot8.png'), (x*60+7, y*60+7))    
                
        
                
                
                
            Matrix[x][y]=BoardPiece(3, pieceSpawn, x*60+7, y*60+7, False, CurrentFileName, True)
    pygame.display.update()
#3 DATA STRUCTURE OF BOARD + INITIAL DISPLAY end############################################       
   


#4) Function 1 start###########################################################
def ProcessCurrentClick():    
    #if Matrix[Matrix_X][Matrix_Y].legal == True: #then proceed
     #   CurrentValue = Matrix[Matrix_X][Matrix_Y].value #take value
        
        
        for x in range(6):
            for y in range(6):
                Matrix[x][y].legal = False # set fullboard.legal = False
                
        #if itsnumerical
        try:#for currentvalue = integers
            if Matrix_X + CurrentValue <=5:
                newX = Matrix_X + CurrentValue
                Matrix[(newX)][Matrix_Y].legal = True #downwards
            
            if Matrix_Y + CurrentValue <=5:
                newY = Matrix_Y + CurrentValue               
                Matrix[Matrix_X][newY].legal = True #rightwards
                
            if Matrix_X + CurrentValue <=5 and Matrix_Y + CurrentValue <=5: 
                newX = Matrix_X + CurrentValue
                newY = Matrix_Y + CurrentValue
                Matrix[(newX)][(newY)].legal = True #downright
            
            if Matrix_X - CurrentValue >=0:
                newX = Matrix_X - CurrentValue
                Matrix[(newX)][Matrix_Y].legal = True #upwards
            
            if Matrix_Y - CurrentValue >=0:
                newY = Matrix_Y - CurrentValue               
                Matrix[Matrix_X][newY].legal = True #leftwards
                
            if Matrix_X - CurrentValue >=0 and Matrix_Y - CurrentValue >=0: 
                newX = Matrix_X - CurrentValue
                newY = Matrix_Y - CurrentValue
                Matrix[(newX)][(newY)].legal = True #upleft
                
            if Matrix_X + CurrentValue <=5 and Matrix_Y - CurrentValue >=0: 
                newX = Matrix_X + CurrentValue
                newY = Matrix_Y - CurrentValue
                Matrix[(newX)][(newY)].legal = True #downleft
                
            if Matrix_X - CurrentValue >=0 and Matrix_Y + CurrentValue <=5: 
                newX = Matrix_X - CurrentValue
                newY = Matrix_Y + CurrentValue
                Matrix[(newX)][(newY)].legal = True #upright
            
        except Exception:
            pass
       
        
       # print("end of Function1")
#4) Function 1 end###########################################################
  


#5) Function 2 start###########################################################
def LegalRefresh():
    global HotCount
    global WarmCount
    global CoolCount
    
    if Matrix[Matrix_X][Matrix_Y].legal==True:
        if Matrix[Matrix_X][Matrix_Y].temp == 3:
            HotCount -= 1
        if Matrix[Matrix_X][Matrix_Y].temp == 2:
            WarmCount -= 1
        if Matrix[Matrix_X][Matrix_Y].temp == 1:
            CoolCount -= 1
            
            
        Matrix[Matrix_X][Matrix_Y].temp -= 1 
        Matrix[Matrix_X][Matrix_Y].legal=False
    gameDisplay.blit(background, (0,0))
    gameDisplay.blit(frame, (0,0))

    for x in range(6):
        for y in range(6):
            NewSpawn=True
            if Matrix[x][y].legal==True: # proceed
                if Matrix[x][y].temp ==3: #if used to be hot
                    StringTemp = "hot" #replace with a warm
                elif Matrix[x][y].temp ==2:
                    StringTemp = "warm"
                elif Matrix[x][y].temp ==1:
                    StringTemp = "cool" #used to be cool, replace with BG
                else:
                    Matrix[x][y].legal = False
                    NewSpawn=False
            
                if NewSpawn:    
                    BlitString = StringTemp + str(Matrix[x][y].value) + "b.png"
                    gameDisplay.blit(pygame.image.load(BlitString), (x*60+7, y*60+7))
                
            else: # Matrix[x][y].legal==False: exactly the same, but no b.png
                if Matrix[x][y].temp ==3: #if used to be hot
                    StringTemp = "hot" #replace with a warm
                elif Matrix[x][y].temp ==2:
                    StringTemp = "warm"
                elif Matrix[x][y].temp ==1:
                    StringTemp = "cool" #used to be cool, replace with BG
                else:
                    NewSpawn=False
            
                if NewSpawn:    
                    BlitString = StringTemp + str(Matrix[x][y].value) + ".png"
                    gameDisplay.blit(pygame.image.load(BlitString), (x*60+7, y*60+7))  
                    
    
    pygame.display.update()
   # print("end of Function2")       
            
            
    
#6) Function 4 start###########################################################
def checkGameOver():
    global GameOver
    GameOver=True
    for x in range(6):
        for y in range(6):
            if Matrix[x][y].legal == True:
                GameOver=False
    



#7) Function 5 start###########################################################
def ProcessRook():    
    #if Matrix[Matrix_X][Matrix_Y].legal == True: #then proceed
     #   CurrentValue = Matrix[Matrix_X][Matrix_Y].value #take value   
    for x in range(6):
        for y in range(6):
            Matrix[x][y].legal = False # set fullboard.legal = False    
    Matrix[0][Matrix_Y].legal = True   
    Matrix[5][Matrix_Y].legal = True   
    Matrix[Matrix_X][0].legal = True   
    Matrix[Matrix_X][5].legal = True      
                
    
    
#8) Function 6 start###########################################################
def ProcessBishop():    
    #if Matrix[Matrix_X][Matrix_Y].legal == True: #then proceed
     #   CurrentValue = Matrix[Matrix_X][Matrix_Y].value #take value   
    for x in range(6):
        for y in range(6):    
            Matrix[x][y].legal = False # set fullboard.legal = False   
    
    DownRightLimit = min(5 - Matrix_X, 5 - Matrix_Y)
    Matrix[Matrix_X+DownRightLimit][Matrix_Y+DownRightLimit].legal = True
    
    DownLeftLimit = min(5 - Matrix_X, Matrix_Y-0)
    Matrix[Matrix_X + DownLeftLimit][Matrix_Y - DownLeftLimit].legal = True
    
    UpRightLimit = min(Matrix_X - 0, 5 - Matrix_Y)
    Matrix[Matrix_X - UpRightLimit][Matrix_Y + UpRightLimit].legal = True
    
    UpLeftLimit = min(Matrix_X - 0, Matrix_Y - 0)
    Matrix[Matrix_X - UpLeftLimit][Matrix_Y - UpLeftLimit].legal = True
       
                
    
    
#9) Function 7 start###########################################################
def ProcessQueen():    
       
    ProcessBishop() #illegalise is inside me
    Matrix[0][Matrix_Y].legal = True   
    Matrix[5][Matrix_Y].legal = True   
    Matrix[Matrix_X][0].legal = True   
    
    
#8) Function 8 start###########################################################
def ProcessKnight():    
    
    for x in range(6):
        for y in range(6):    
            Matrix[x][y].legal = False # set fullboard.legal = False  
            
       
    
    if Matrix_X-2 >= 0: # UUL/UUR:
        if Matrix_Y-1 >= 0:
            Matrix[Matrix_X-2][Matrix_Y-1].legal = True # UP UP LEFT
        if Matrix_Y+1 <= 5:  
            Matrix[Matrix_X-2][Matrix_Y+1].legal = True # UP UP RIGHT
            
            
    if Matrix_X+2 <= 5: # DDL/DDR:
        if Matrix_Y-1 >= 0:
            Matrix[Matrix_X+2][Matrix_Y-1].legal = True # DOWN DOWN LEFT
        if Matrix_Y+1 <= 5:  
            Matrix[Matrix_X+2][Matrix_Y+1].legal = True # DOWN DOWN RIGHT
            
    if Matrix_Y-2 >= 0: # LLU/LLD:
        if Matrix_X-1 >= 0:
            Matrix[Matrix_X-1][Matrix_Y-2].legal = True # lEFT LEFT UP
        if Matrix_X+1 <= 5:  
            Matrix[Matrix_X+1][Matrix_Y-2].legal = True # LEFT LEFT DOWN
            
    if Matrix_Y+2 <= 5: # RRU/RRD:
        if Matrix_X-1 >= 0:
            Matrix[Matrix_X-1][Matrix_Y+2].legal = True # RIGHT RIGHT UP
        if Matrix_X+1 <= 5:  
            Matrix[Matrix_X+1][Matrix_Y+2].legal = True # RIGHT RIGHT DOWN
    
            
#9) Function 9 start###########################################################
def ProcessRum():    
      
    for x in range(6):
        for y in range(6):    
            Matrix[x][y].legal = True # set fullboard.legal = False               
    
            
#10) Function 10 start###############
def SpawnNew():
    pieceSpawn = random.randint(1,101) # 1 TO 4 IS NUMERICAL. 5 TO 8 IS CHESS. 9 CANNOT SPAWN    
    if pieceSpawn <=18.5:
        pieceSpawn = 1
    elif pieceSpawn <=31.2:
        pieceSpawn = 2
    elif pieceSpawn <=41.1:
        pieceSpawn = 3
    elif pieceSpawn <=49.6:
        pieceSpawn = 4
    elif pieceSpawn <=60.1:
        pieceSpawn = 5
    elif pieceSpawn <=69.2:
        pieceSpawn = 6
    elif pieceSpawn <=88:
        pieceSpawn = 7
    else:
        pieceSpawn=8

    if Matrix_X in range(2,4) and Matrix_Y in range(2,4):
        if pieceSpawn ==4:
            pieceSpawn =1
    
    if HotCount == 1 and Matrix[Matrix_X][Matrix_Y].temp==3:
        pieceSpawn = 9      
    if WarmCount == 1 and Matrix[Matrix_X][Matrix_Y].temp==2:
        pieceSpawn = 9      
    if CoolCount == 1 and Matrix[Matrix_X][Matrix_Y].temp==1:
        pieceSpawn = 9      
    
    Matrix[Matrix_X][Matrix_Y].value=pieceSpawn
    Matrix[Matrix_X][Matrix_Y].legal=True
    

    
###########
###########
###########
###########
###########
    
BeginGame()
    
gameExit=False
while not gameExit:
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            gameExit = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                BeginGame()         
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            xMouse, yMouse = pygame.mouse.get_pos()
            if xMouse in range (7, 367) and yMouse in range (7, 367):
                Matrix_X = int( (xMouse-7) / 60)
                Matrix_Y = int( (yMouse-7) / 60)
                if Matrix[Matrix_X][Matrix_Y].legal == True: #then proceed
                    CurrentValue = Matrix[Matrix_X][Matrix_Y].value
                    if CurrentValue in range(1,5):  # 1 TO 4 IS NUMERICAL. 5 TO 8 IS CHESS. 9 CANNOT SPAWN    
                        ProcessCurrentClick()
                    elif CurrentValue == 5:
                        ProcessRook()
                    elif CurrentValue == 6:
                        ProcessBishop()
                    elif CurrentValue == 7:
                        ProcessQueen()
                    elif CurrentValue == 8:
                        ProcessKnight()
                    elif CurrentValue == 9:
                        ProcessRum()                       
                    SpawnNew()
                    LegalRefresh()
                                    
                    
                    
                    
                checkGameOver()
                if GameOver==True:            
                    pygame.display.set_caption("No moves. 'k' for new game")
           
pygame.quit() #to unitialise pygame
quit()

    















