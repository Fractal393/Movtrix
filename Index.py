import random
import sys
def replaceMultiple(movie, tobereplaced, newString):
    for elem in tobereplaced:
        if elem in movie :
            movie = movie.replace(elem, newString)
    return  movie
f=open("A.txt","r+")
al=f.read()
f.seek(0,0)
movie=random.choice(f.readlines())
con=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','W','Y','Z']
vow=['A','E','I','O','U']
movie_rep = replaceMultiple(movie,con,"-")
print ("\t\tMovTrix 1.0 \n Rules: \n  1.Use the clue to guess the movie. \n  2.Only letters are to be entered. \n  3.A player has six lives which deduct when a wrong letter is entered.\n  4.If all the lives of a player run out then 'GAME OVER'.\n  5.To exit enter 'EXIT'.\n")
print ("\t",movie_rep)
life=6
while movie_rep != movie:
    letter=input("Enter a letter: ")
    if letter=="BAZINGA":
        print(movie)
        break
    if letter=="XERTZ":
        print(al)
        break
    if letter=="EXIT":
        break
    while letter.isalpha()!=True or len(letter)>1:
        letter=input("Enter single letter: ")
        if not letter.isalpha():
            print("Only letters are allowed!")
    letter=letter.upper()
    check=movie.find(letter)
    while(life>0):
        if(letter in vow):
            print("Letter already in there or already used or is a vowel!")
            break
        elif(check==-1):
            life=life-1
            vow.append(letter)
            if(life==0):
                print("Game Over!")
                #sys.exit()
            print("You have" , life , "lives left!")
            break
        else: 
            con.remove(letter)
            movie_rep = replaceMultiple(movie,con,"-")
            print(movie_rep)
            print("You have" , life , "lives left!")
            break
if movie_rep == movie:
    print("Y      Y     O O O      U         U           W                 W    I     N         N     !!!")
    print(" YY  YY    O       O    U         U            W               W     I     N N       N     !!!")
    print("  YYYY    O         O   U         U             W             W      I     N   N     N     !!!")
    print("   YY     O         O   U         U              W     W     W       I     N     N   N     !!!")
    print("   YY      O       O     U       U                W   W W   W        I     N       N N        ")
    print("   YY        O O O         U U U                   W W   W W         I     N         N     [ ]")
