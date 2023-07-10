from tester import *

one = 0
two = 0

scores = {"2-0": 0, "2-1": 0, "0-2": 0, "1-2": 0}
# scores = {"3-0": 0, "3-1": 0, "3-2": 0, "0-3": 0, "1-3": 0, "2-3": 0}


teams = ["100 Thieves", "Cloud9", "Evil Geniuses", "FaZe Clan", "Ghost Gaming",  "Luminosity Gaming", "NRG Esports", "OpTic Gaming", "Sentinels", "The Guard", "TSM", "XSET"]


t1 = teams[3]
t2 = teams[0]
for x in range(0,1000):
    
    won, round = play_round(Team(t1, 800, 800, 0, 0, 0), Team(t2, 800, 800, 0, 0, 0), 1)
    # print(play_round(Team("The Guard", 800, 0, 0, 0), Team("Luminosity Gaming", 800, 0, 0, 0), 1, 800, 800))


    #ADD Wins
    if(won == "1"):
        one += 1
    else:
        two += 1


    #BO3
    if(one == 2 or two == 2):
        if(one == 2 and two == 0):
            scores.update({"2-0": scores["2-0"]+1})
        elif(one == 2 and two == 1):
            scores.update({"2-1": scores["2-1"]+1})
        elif(one == 0 and two == 2):
            scores.update({"0-2": scores["0-2"]+1})
        else:
            scores.update({"1-2": scores["1-2"]+1})
        one=0
        two=0


    #BO5
    '''
    if(one == 3 and two == 0):
        scores.update({"3-0": scores["3-0"]+1})
        one = 0
    
    elif(one == 3 and two == 1):
        scores.update({"3-1": scores["3-1"]+1})
        one= 0
        a = 0

    elif(one == 3 and two == 2):
        scores.update({"3-2": scores["3-2"]+1})
        one= 0
        two= 0

    elif(one == 0 and two == 3):
        scores.update({"0-3": scores["0-3"]+1})
        a = 0
    
    elif(one == 1 and two == 3):
        scores.update({"1-3": scores["1-3"]+1})
        one= 0
        a = 0


    elif(one == 2 and two == 3):
        scores.update({"2-3": scores["2-3"]+1})
        one = 0
        two= 0
    
        
    else:
        pass
    '''
    


 
# print(scores)
print(t1, t2)
total = sum(scores.values())

#BO3
chances = {"Team 1": 1/((scores["2-0"]+scores["2-1"])/total), 
           "Team 2": 1/((scores["0-2"]+scores["1-2"])/total), 
           "2-0": 1/(scores["2-0"]/total), 
           "2-1": 1/(scores["2-1"]/total), 
           "0-2": 1/(scores["0-2"]/total), 
           "1-2": 1/(scores["1-2"]/total),
           "Over": 1/((scores["2-1"]+scores["1-2"])/total), 
           "Under": 1/((scores["2-0"]+scores["0-2"])/total), "Team 1 (+1.5)": 1/((scores["2-0"]+scores["2-1"]+scores["1-2"])/total), "Team 2 (+1.5)": 1/((scores["0-2"]+scores["1-2"]+scores["2-1"])/total) }


#BO5
'''
chances = {"Team 1": 1/((scores["3-0"]+scores["3-1"]+scores["3-2"])/total),
"Team 2": 1/((scores["0-3"]+scores["1-3"]+scores["2-3"])/total), 
"3-0": 1/(scores["3-0"]/total),
"3-1": 1/(scores["3-1"]/total),
"3-2": 1/(scores["3-2"]/total), 
"0-3": 1/(scores["0-3"]/total),
"1-3": 1/(scores["1-3"]/total), 
"2-3": 1/(scores["2-3"]/total), 
"Over 3.5": 1/((scores["3-1"]+scores["3-2"]+scores["1-3"]+scores["2-3"])/total),
"Under 3.5": 1/((scores["3-0"]+scores["0-3"])/total),
"Over 4.5": 1/((scores["3-2"]+scores["2-3"])/total),
"Under 4.5": 1/((scores["3-0"]+scores["3-1"]+scores["0-3"]+scores["1-3"])/total),
"Team 1 (-1.5)": 1/((scores["3-0"]+scores["3-1"])/total),
"Team 1 (+1.5)": 1/((scores["3-0"]+scores["3-1"]+scores["3-2"]+scores["2-3"])/total),
"Team 2 (-1.5)": 1/((scores["0-3"]+scores["1-3"])/total),
"Team 2 (+1.5)": 1/((scores["0-3"]+scores["1-3"]+scores["2-3"]+scores["3-2"])/total),
"Team 1 (+2.5)": 1/((scores["3-0"]+scores["3-1"]+scores["3-2"]+scores["2-3"]+scores["1-3"])/total),
"Team 2 (+2.5)": 1/((scores["0-3"]+scores["1-3"]+scores["2-3"]+scores["3-2"]+scores["3-1"])/total)} 
'''  

print(chances)

