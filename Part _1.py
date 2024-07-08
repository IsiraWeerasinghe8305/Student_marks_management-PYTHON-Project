from graphics import *
from Part2 import *
from contextlib import redirect_stdout

x_win = 500
y_win = 500

def main():
    win = GraphWin(" Histogram ",  x_win , y_win )
    message = Text(Point( x_win-(x_win /2),24),  " Histogram Results ")
    message.setSize(18)
    message.draw(win)
    
    aLine = Line(Point( x_win/14 ,(y_win - ( y_win/8 ))), Point(( x_win - (x_win/14) ), y_win  -  ( y_win/8 ) ))
    aLine.draw(win)

    total = total_frequency
    Height =  (y_win -(y_win/3) )/  total
    
    total_full = ' outcomes in total '  ,total 
    message = Text(Point(x_win/2, y_win - 10) ,  total_full )
    message.draw(win)
    x = [ ]
    for i in range(len(x_first)):
        m = x_first[i] * Height
        x.append(m)

    n = x_win/14
    
    y = [ "Progress" , "Trailer" ,"Retriever","Exclude" ]
    z = ["#9370DB", "#ADFF2F", "#6B8E23", "#32CD32"]
    
    for i in range(len(x)):
        X = x[i]
        Y = y[i]
        X_first = x_first[ i ]
        aRectangle = Rectangle(Point(10 + n , y_win - ( y_win/8 )), Point((x_win/7)+ n, y_win -  X -  y_win/8  ))
        aRectangle.setFill( z [ i ])
        aRectangle.draw(win)
        
        message = Text(Point( ((x_win/14) )+ n  ,  y_win -( X +10 + y_win/8 )) ,  X_first)
        message.draw(win)
        
        message = Text(Point((x_win/14) + n, y_win - (y_win/11)), Y)
        message.draw(win)
        
        n += (x_win / 5)

if s_student != 1:  
    main()

    with open("D:\Part 3 - Text File.txt", "w") as file:
        with redirect_stdout(file):
            print("Part 3:")
            list_print()
