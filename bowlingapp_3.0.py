#Ekin Yurekli
#October 27, 2022
#Bowling Application Project
#This program asks for scores of a Bowling game frame by frame. Strikes and spares are calculated automatically.


#VARIABLES OF THE PROGRAM

#Keeps the Scores in One Group
ScoreList=[]

#Keeping the Loop Active
repeat = 1

#Helps us keep track of the number of strikes
strikecounter = 0

#Helps us keep track of spares
sparecounter = 0

#Frame 1's Score
score1 = 0

#Frame 2's Score
score2 = 0 

#Frame 3's Score (It will be used only on Round 10 if there was a strike/spare
score3 = 0

#Helps us keep track of the number of rounds.
i = 1


#The Code

#Small welcome message.
print("")
print("Welcome to the Bowling Score Calculator!")
print("")

#Sets up the loop. Prevents exceeding 10 rounds just in case.
#Can be broken by assigning "repeat" a new value
while repeat == 1 and i < 11:


    #Using try-break prevents our code from crashing if the input is not entered correctly.
    try:
        
#Asks for the FIRST FRAME
        score1=int(input("Please enter the first frame's score: "))
     
    except:
        print("")
        print("You have entered a letter, words, or a non integer. Please try again")
        print("")
        
        continue
        #By using continue, we will skip the rest of the code and restart again.
        #This way, the "i" counter will not increase



    #This checks if the user has entered a number that is not between 0-10.
    if score1 > 10 or score1 < 0:  
        print("")
        print("Your number exceeds 10 or is below 0. Please try again.")
        print("")
        
        continue
        #Continue sees the same purpose as before, the rest of the code will be skipped
        #And we will restart again, the round counter will not be affected.
    
        

    #Checks if a strike was scored
    if score1 == 10: 
    

    #Adds up if there was no strike previously   
        if strikecounter == 0:
            strikecounter = strikecounter + 1
            
    #Adds up 10 if there was previously one strike 
        elif strikecounter == 1:
            strikecounter = strikecounter + 1
            ScoreList.append(10)

    #Adds up if there was a double strike
        elif strikecounter == 2:
            strikecounter = strikecounter + 1
            ScoreList.append(20)
            
        elif strikecounter == 3:
            ScoreList.append(30)
            strikecounter = strikecounter - 1

            


    #Checks a spare
    if sparecounter == 1:
        ScoreList.append(score1+10)
        sparecounter = 0

    
    #Checks if there wasn't a strike and if it is not Round 10.
    #If it is Round 10 a different code will be executed so that a input for a 3rd frame can be asked
    if score1 < 10 and i < 10:


#Asks for the SECOND FRAME
        try:
            score2=int(input("Please enter the second frame's score: "))
        except:
            print("")
            print("You have entered a letters or words, please try again from the start of this round.")
            print("")
            continue

        #Checks if a score that exceeds the number of pins left or is below 0 is entered.
        if score2 > 10-score1 or score2 < 0:
            print("")
            print("The score you have entered exceeds the number of pins left or is below 0.")
            print("Please try again.")
            print("")
            continue
            
            #Strike calculation
            #Adds up 10 if there was previously one strike 
        if strikecounter == 1:
            ScoreList.append(score1+score2+10)

            
            #Adds up 20 if there was a double strike
        elif strikecounter == 2:
            ScoreList.append(score1+score2+20)
            
            #Adds up 30 if there was a triple (Turkey) strike
        elif strikecounter == 3:
            ScoreList.append(score1+score2+30)

            #All of the strike calculation has been done.
            #Clears the strike count if score1 wasn't a strike.
            strikecounter = 0


            #Checks if a spare was scored.
        if score1+score2 == 10:
            sparecounter = sparecounter + 1
            
    #Adds the score to the list instantly if there wasn't a spare.
        if score1+score2 < 10:
            ScoreList.append(score1+score2)
            sparecounter = 0


    #Executes a different code if it is Round 10,
    #so that the code can ask for a third frame if a strike or spare is scored.
    elif i == 10:
        
#Asks for the SECOND FRAME in Round 10
        try:
            score2=int(input("Please enter the second frame's score: "))
        except:
            print("")
            print("You have entered a letters or words, please try again from the start of this round.")
            print("")
            continue
        

        #Strike calculation is done.
        #Round 10 functions differently compared to the the previous rounds.
        #A player has the chance to reset the pins if they score 10.
        #So it's Strike/Spare calculation is different as well.
        
        if score1 == 10:

        #Checks if score2 exceeds 10 pins or is below 0 if score1 was a strike during Round 10
            if score2 > 10 or score2 < 0:
                print("")
                print("Your number exceeds 10 or is below 0. Please try again.")
                print("")
                continue
        
            if strikecounter == 1:
                ScoreList.append(10)

            elif strikecounter == 2:
                ScoreList.append(20)

            elif strikecounter == 3:
                ScoreList.append(30)
                
        elif score1 < 10:

        #Checks if score2 exceeds the pins or is below 0 if score1 wasn't a strike during Round 10
            if score2 > 10-score1 or score2 < 0: 
                print("")
                print("The score you have entered exceeds the number of pins left or is below 0.")
                print("Please try again.")
                print("")
                continue

            
            if strikecounter == 1:
                ScoreList.append(score1+score2+10)
                
            elif strikecounter == 2:
                ScoreList.append(score1+score2+20)
                
            elif strikecounter == 3:
                ScoreList.append(score1+score2+30)
                
            strikecounter = 0

        if score1 + score2 == 10:
            sparecounter = sparecounter + 1

        if score1 + score2 < 10:
            ScoreList.append(score1+score2)
    

    #Will be active only if it's the 10th score and a strike or spare was scored
    if i == 10:
        if strikecounter >= 1 or sparecounter == 1:

        #Prevents crashing for the third frame's score as well.
            try:
                score3=int(input("Please enter the third and FINAL frame's score: "))
            except:
                print("")
                print("You have entered a letters or words, please try again.")
                print("You will have to start entering Round 10 scores from the beginning.")
                print("")

        #This time we will unfortunately have to go back to writing Round 10 scores from the beginning of Round 10.
                continue 
                
        #Checks any spares of strikes before the third frame
            if sparecounter == 1:
                ScoreList.append(score3+score2+score1)

            elif strikecounter == 1:
                ScoreList.append(score3+10)

            elif strikecounter >= 2:
                ScoreList.append(score3+20)
            
        
    
    #Keeps the player updated with information about the scores and round.
    print("")
    print("Current Total Score for Round", i,"is:",sum(ScoreList))
    print("")
    print("Current Number of Strikes:",strikecounter)
    print("")
    print("Current Number of Spares:",sparecounter)
    print("")

    
    #Adding 1 to the counter to prevent exceeding 10 frames
    i = i + 1

    #Ending the loop if the user wants to stop before 10 frames
    try:
        repeat=int(input("Type in '1' to continue: "))
    except:
        break
    if repeat != 1:
        break


#Prints all the scores and final score count
print("")
print("All scores are:",ScoreList)
print("Final Total Score is:",sum(ScoreList))


#Displays a small message if a perfect game was reached.
if sum(ScoreList) == 300:
    print("")
    print("You achieved a perfect game!")


               
    

    



        
        
        
            
            
    

        
            
                   
    
