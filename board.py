#Tkinter to create windows application
from tkinter import *
#OS to open files and folders
import os


   
#Window of the board game
root = Tk()
bGC = '#bfba8f'
root.configure(bg=bGC, padx=10, pady=10)
root.title('Chess')
root.geometry('1200x900')


#squareID will hold all board coords
squareID = {}

#Save the piece location in the board
pieceLoc = {}

#Store all images
global varImg
varImg = {}
global varImg_Count
varImg_Count = 0

#label horizontal (lbh) and label vertical (lbv)
lbh = ['none', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lbv = ['none', '8', '7', '6', '5', '4', '3', '2', '1']

# letter to number and number to index to convert the piece adress in the board
letToNum = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
numToInd = {'1':8,'2':7,'3':6,'4':5,'5':4,'6':3,'7':2,'8':1}

#color themes of the board
theme_pieces = {'bw':['black','white'],
                'yb':['#e6b42c','#784a0d']}

#Chess Pieces Objects
piece = {'pawn':{
                'name':'pawn',
                'color':['black', 'white'],
                'image':[r'Assets\Images\pawn.gif', r'Assets\Images\pawn_b.gif'],
                'movement':[
                            [[1,'y']]
                            ],
                'attack':[[[1,'y'],[1,'x']],
                          [[1,'y'],[-1,'x']]
                          ],
                'value':1,
                'special':[{'Not Moved':[2,'y']}],
                'letter':'P'
                },
        'knight':{
                'name':'knight',
                'color':['black', 'white'],
                'image':[r'Assets\Images\knight.gif', r'Assets\Images\knight_b.gif'],
                'movement':[
                            [[2,'x'],
                             [1,'y']],
                            [[2,'x'],
                             [-1,'y']],
                            [[1,'x'],
                             [2,'y']],
                            [[-1,'x'],
                             [2,'y']],
                            [[-2,'x'],
                             [1,'y']],
                            [[-2,'x'],
                             [-1,'y']],
                            [[1,'x'],
                             [-2,'y']],
                            [[-1,'x'],
                             [-2,'y']]                            
                            ],
                'attack':[],
                'value':3,
                'special':[],
                'letter':'N'
                },
        'bishop':{
                'name':'bishop',
                'color':['black', 'white'],
                'image':[r'Assets\Images\bishop.gif', r'Assets\Images\bishop_b.gif'],
                'movement':[
                            [[1,'y'],[1,'x'], 
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x'], 
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x']],
                            [[-1,'y'],[1,'x'], 
                             [-1,'y'],[1,'x'],
                             [-1,'y'],[1,'x'], 
                             [-1,'y'],[1,'x'],
                             [-1,'y'],[1,'x'], 
                             [-1,'y'],[1,'x'],
                             [-1,'y'],[1,'x'],
                             [-1,'y'],[1,'x']],
                            [[-1,'y'],[-1,'x'], 
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x']],
                            [[1,'y'],[-1,'x'], 
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x']]
                            ],                           
                'attack':[],
                'value':3,
                'special':[],
                'letter':'B',
                },
        'rook':{
                'name':'rook',
                'color':['black', 'white'],
                'image':[r'Assets\Images\rook.gif', r'Assets\Images\rook_b.gif'],
                'movement':[
                            [[1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x']],
                            [[-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x']],
                            [[-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y']],
                            [[1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y']]
                            ],
                'attack':[],
                'value':5,
                'special':[],
                'letter':'R'
                },
        'queen':{
                'name':'queen',
                'color':['black', 'white'],
                'image':[r'Assets\Images\queen.gif', r'Assets\Images\queen_b.gif'],
                'movement':[
                            [[1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x'],
                             [1,'x']],
                            [[-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x'],
                             [-1,'x']],
                            [[-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y'],
                             [-1,'y']],
                            [[1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y'],
                             [1,'y']],
                            [[1,'y'],[1,'x'], 
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x'], 
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x'],
                             [1,'y'],[1,'x']],
                            [[-1,'y'],[1,'x'], 
                             [-1,'y'],[1,'x'],
                             [-1,'y'],[1,'x'], 
                             [-1,'y'],[1,'x'],
                             [-1,'y'],[1,'x'], 
                             [-1,'y'],[1,'x'],
                             [-1,'y'],[1,'x'],
                             [-1,'y'],[1,'x']],
                            [[-1,'y'],[-1,'x'], 
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x'],
                             [-1,'y'],[-1,'x']],
                            [[1,'y'],[-1,'x'], 
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x'],
                             [1,'y'],[-1,'x']]                          
                            ],
                'attack':[],
                'value':9,
                'special':[],
                'letter':'Q'
                },
        'king':{
                'name':'king',
                'color':['black', 'white'],
                'image':[r'Assets\Images\king.gif', r'Assets\Images\king_B.gif'],
                'movement':[
                            [[1,'x']],
                            [[1,'y']],
                            [[-1,'x']],
                            [[-1,'y']],
                            [[1, 'x'],
                             [1,'y']],
                            [[-1, 'x'],
                             [1,'y']],
                            [[1, 'x'],
                             [-1,'y']],
                            [[-1, 'x'],
                             [-1,'y']]                            
                            ],
                'attack':[],
                'value':0,
                'special':[],
                'letter':'K'
                }        
         }

#Chess Pieces Start Position
start_place = [[piece['pawn'],'white','a2'],
               [piece['pawn'],'white','b2'],
               [piece['pawn'],'white','c2'],
               [piece['pawn'],'white','d2'],
               [piece['pawn'],'white','e2'],
               [piece['pawn'],'white','f2'],
               [piece['pawn'],'white','g2'],
               [piece['pawn'],'white','h2'],
               [piece['rook'],'white','a1'],
               [piece['rook'],'white','h1'],
               [piece['knight'],'white','b1'],
               [piece['knight'],'white','g1'],
               [piece['bishop'],'white','f1'],
               [piece['bishop'],'white','c1'],
               [piece['queen'],'white','d1'],              
               [piece['king'],'white','e1'],
               [piece['pawn'],'black','a7'],
               [piece['pawn'],'black','b7'],
               [piece['pawn'],'black','c7'],
               [piece['pawn'],'black','d7'],
               [piece['pawn'],'black','e7'],
               [piece['pawn'],'black','f7'],
               [piece['pawn'],'black','g7'],
               [piece['pawn'],'black','h7'],
               [piece['rook'],'black','a8'],
               [piece['rook'],'black','h8'],
               [piece['knight'],'black','b8'],
               [piece['knight'],'black','g8'],
               [piece['bishop'],'black','f8'],
               [piece['bishop'],'black','c8'],
               [piece['queen'],'black','d8'],              
               [piece['king'],'black','e8']
               ]


#Get the path of the images used in the pieces
def get_path(relative_path):
    directory_path = os.path.dirname(__file__)
    file_path = os.path.join(directory_path, relative_path)
    return file_path


#Create Square image for the board
pawn_path = get_path(r'Assets\Images\square.gif')
squareImg = PhotoImage(file=pawn_path)


#Get the board adress background color to blend with the piece button
def get_boardID_color(boardID): 
    color = squareID[boardID]
    return color


#Create each square in the chess board, uses index of x and y based on odd and even numbers
def addSquare(x, y):
    if (y%2 == 0):
        if (x%2 == 0):
            squareColor(myTheme[0], x, y)
        else:
            squareColor(myTheme[1], x, y)
    else:
        if (x%2 != 0):
            squareColor(myTheme[0], x, y)
        else:
            squareColor(myTheme[1], x, y)       


#Sub function of addSquare(), save each adress color in the squareID = {}
def squareColor(color, x, y):
    coord_xy = str(x+1) + str(y+1)    
    squareID[coord_xy] = color
    x += 1
    y += 1
    newButton = Button(root, bg=color, borderwidth=0, activebackground='#46E576', image=squareImg,  height=100, width=100)
    newButton.grid(column=x, row=y)

    
#This function is used to get the index using an adress format like 'a2' to get '17' (the second index is reversed from 8 to 1)
#Uses lbv as default, to use lbh, set 'a' to anything different than 1 like: get_Index(num, 0)
def get_Index(num, a=1):
    if (a == 1):
        return letToNum[num]
    else:
        return numToInd[num]    
    
 
#Inverse converter from x,y to 'a2' format    
def toA2(x,y):
    a = lbh[x]
    b = lbv[y]
    return  str(a) + str(b) 

#Create a green selection over the possible movements of the piece selected
def clickPiece(pie, pos):  
    pieceObj = piece[pieceLoc[pos][0]]
    pieceColor = pieceLoc[pos][1]
    mov = pieceObj['movement'] 
    i = 0
    while i < len(mov):
        j = 0
        print(mov[i], 'i', i)   
        boardXY = conv_xy(pos)  
        while j < len(mov[i]):
            print(mov[i][j], 'j', j)
            if (pieceColor == 'white'):
                mov2 = mov[i][j][0] * -1
            else:
                mov2 = mov[i][j][0]
            print(mov2)
            if (mov[i][j][1] == 'x'):
                boardXY[0] += mov2
            if (mov[i][j][1] == 'y'):
                boardXY[1] += mov2
            if (boardXY[0] <= 0) or (boardXY[1] <= 0) or (boardXY[0] >= 9) or (boardXY[1] >= 9):
                break
            print(boardXY)
            #Movement based on piece
            if     (pie == 'bishop' and (j%2 != 0)) \
                or (pie == 'pawn' and (len(mov[i]) == 1)) \
                or (pie == 'rook') \
                or ((pie == 'knight') and (boardXY[0] != conv_xy(pos)[0]) and (boardXY[1] != conv_xy(pos)[1])) \
                or (pie == 'king') \
                or ((pie == 'queen') and ((j%2 != 0) \
                    or (j <= 1) \
                    or ((mov[i][j-1][1] == 'x') and (mov[i][j][1] == 'x') \
                    or ((mov[i][j-1][1] == 'y') and (mov[i][j][1] == 'y'))))):                                    
                posA2 = toA2(boardXY[0], boardXY[1])
                locBut = Button(root, bg='#5cfa86', borderwidth=0, command=lambda p=posA2, l=pos, t=pie, c=pieceColor: movePiece(p, l, t, c), image=squareImg, height=100, width=100)
                locBut.grid(column=boardXY[0], row=boardXY[1])                    
            j += 1
        i += 1


#Move the piece to location
def movePiece(pos, posOld, type, color):
    butt = pieceLoc[posOld][2]
    butt.grid_remove()
    addPiece(type, pos, color)


#Convert 'a2' to [x,y]
def conv_xy(startPos, x=0, y=0):
    startIndX = get_Index(startPos[0])        
    startIndY = get_Index(startPos[1], 0)
    finalIndX = int(startIndX) + x
    finalIndY = int(startIndY) + y
    return [finalIndX, finalIndY]


#Add piece to selected A2 coord, Ex: type='pawn', pos='a2', color='white'
def addPiece(type, pos, color):
    global varImg_Count
    global varImg
    pieceType = piece[type]
    if (color == 'white'):
        varP = get_path(pieceType['image'][0])
    elif(color == 'black'):
        varP = get_path(pieceType['image'][1])
    varImg[varImg_Count] = PhotoImage(file=varP) 
    cVar = get_Index(pos[0])
    rVar = get_Index(pos[1], 0)
    idVar = str(cVar) + str(rVar)
    bg_board = get_boardID_color(idVar) 
    pieceBt = Button(root, bg=bg_board, borderwidth=0, command=lambda t = type, p = pos: clickPiece(t, p), image=varImg[varImg_Count], height=100, width=100)
    pieceBt.grid(column=cVar, row=rVar)
    pieceLoc.__setitem__(pos, [type, color, pieceBt])
    varImg_Count += 1


#Themes
myTheme = theme_pieces['yb']
#myTheme = theme_pieces['bw']


#Create the labels of the board    
i = 0
while i < 8:
    j = 0
    while j < 8:
        addSquare(j, i)
        a1 = j+1
        if (i==0):
            
            lb1 = Label(root, text=lbh[a1], bg=bGC, fg='black', font='Arial').grid(column=a1, row=0)           
            lb2 = Label(root, text=lbh[a1], bg=bGC, fg='black', font='Arial').grid(column=a1, row=9)
        j += 1
    a2 = i+1
    lb3 = Label(root, text=lbv[a2], bg=bGC, fg='black', font='Arial').grid(column=0, row=a2)           
    lb4 = Label(root, text=lbv[a2], bg=bGC, fg='black', font='Arial').grid(column=9, row=a2)
    i += 1


#Create the Pieces on the Starting Position   
i = 0
while i < len(start_place):
    pColor = start_place[i][1]  
    pos = start_place[i][2]
    keyName = start_place[i][0]['name']
    addPiece(keyName, pos, pColor)
    i += 1

#For Test
addPiece('bishop', 'd6', 'white')
addPiece('rook', 'c3', 'white')
addPiece('king', 'e5', 'white')
addPiece('knight', 'f5', 'white')
addPiece('queen', 'd5', 'white')


#Run the Windows
root.mainloop()