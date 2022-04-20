#Tkinter to create windows application
from tkinter import *
#OS to open files and folders
import os

#squareID will hold all board coords
squareID = {}

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
                'letter':'P',
                'color':['black', 'white'],
                'image':[r'Assets\Images\pawn.gif', r'Assets\Images\pawn_b.gif'],
                'movement':[],
                'attack':[],
                'value':1,
                'special':[]
                },
        'knight':{
                'letter':'N',
                'color':['black', 'white'],
                'image':[r'Assets\Images\knight.gif', r'Assets\Images\knight_b.gif'],
                'movement':[],
                'attack':[],
                'value':3,
                'special':[]
                },
        'bishop':{
                'letter':'B',
                'color':['black', 'white'],
                'image':[r'Assets\Images\bishop.gif', r'Assets\Images\bishop_b.gif'],
                'movement':[],
                'attack':[],
                'value':3,
                'special':[]
                },
        'rook':{
                'letter':'R',
                'color':['black', 'white'],
                'image':[r'Assets\Images\rook.gif', r'Assets\Images\rook_b.gif'],
                'movement':[],
                'attack':[],
                'value':5,
                'special':[]
                },
        'queen':{
                'letter':'Q',
                'color':['black', 'white'],
                'image':[r'Assets\Images\queen.gif', r'Assets\Images\queen_b.gif'],
                'movement':[],
                'attack':[],
                'value':9,
                'special':[]
                },
        'king':{
                'letter':'K',
                'color':['black', 'white'],
                'image':[r'Assets\Images\king.gif', r'Assets\Images\king_B.gif'],
                'movement':[],
                'attack':[],
                'value':0,
                'special':[]
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
    pawn_path = get_path(r'Assets\Images\square.gif')
    newImg = PhotoImage(file=pawn_path)
    coord_xy = str(x+1) + str(y+1)    
    squareID[coord_xy] = color
    x += 1
    y += 1
    newButton = Button(root, bg=color, borderwidth=0, activebackground='#46E576', image=newImg,  height=100, width=100).grid(column=x, row=y)
    
#This function is used to get the index using an adress format like 'a2' to get '17' (the second index is reversed from 8 to 1)
#Uses lbv as default, to use lbh, set 'a' to anything different than 1 like: get_Index(num, 0)
def get_Index(num, a=1):
    if (a == 1):
        return letToNum[num]
    else:
        return numToInd[num]    

   
#Window of the board game
root = Tk()
bGC = '#bfba8f'
root.configure(bg=bGC, padx=10, pady=10)
root.title('Chess')
root.geometry('1200x900')

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
varImg = {}
while i < len(start_place):
    if (start_place[i][1] == 'white'):
        varPath = get_path(start_place[i][0]['image'][0])
    else:
        varPath = get_path(start_place[i][0]['image'][1])
    varImg[i] = PhotoImage(file=varPath) 
    cVarInd = start_place[i][2][0]
    rVarInd = start_place[i][2][1]
    cVar = get_Index(cVarInd)
    rVar = get_Index(rVarInd, 0)
    idVar = str(cVar) + str(rVar)
    #print('Column: ', cVar)
    #print('Row: ', rVar)
    #print('IDs', idVar)    
    bg_board = get_boardID_color(idVar)
    pieceBut = Button(root, bg=bg_board, borderwidth=0, image=varImg[i], height=100, width=100).grid(column=cVar, row=rVar)
    i += 1


#Run the Windows
root.mainloop()