from tester import *

#variable for team 1 wins and team 2 wins
one = 0
two = 0
rounds = 0

#List of teams
teams = ["100 Thieves", "Cloud9", "Evil Geniuses", "FaZe Clan", "Ghost Gaming",  "Luminosity Gaming", "NRG Esports", "OpTic Gaming", "Sentinels", "The Guard", "TSM", "XSET"]
playoffTeams = ["100 Thieves", "Evil Geniuses", "FaZe Clan", "Ghost Gaming", "Luminosity Gaming", "NRG Esports", "OpTic Gaming", "XSET"]
LCQTeams = ["100 Thieves", "Evil Geniuses", "FaZe Clan", "Luminosity Gaming", "NRG Esports", "Sentinels", "The Guard"]

#Loop through teams list so every matchup is made
for team1 in LCQTeams:

    row = 0

    for team2 in LCQTeams:

        if (team1 != team2): 

            scores = {"2-0": 0, "2-1": 0, "0-2": 0, "1-2": 0}  
            t1 = team1
            t2 = team2
           
           #Simulate X number of games
            for x in range(0, 1000):

                won, rounds = play_round(Team(t1, 800, 800, 0, 0, 0), Team(t2, 800, 800, 0, 0, 0), 1)
                  
                #ADD Wins
                if(won == "1"):
                    one += 1 
                else:
                    two += 1

                #BO3
                if(one==2 or two==2): 

                    if(one==2 and two==0):
                        scores.update({"2-0": scores["2-0"]+1})

                    elif(one==2 and two==1):
                        scores.update({"2-1": scores["2-1"]+1})

                    elif(one==0 and two==2):
                        scores.update({"0-2": scores["0-2"]+1})

                    else:
                        scores.update({"1-2": scores["1-2"]+1})

                    #RESET for next BO3
                    one=0
                    two=0

            

            # print(t1, t2)
            print(scores)
            total = sum(scores.values())

            #Odds of each bet
            chances = {"Team 1": 1/((scores["2-0"]+scores["2-1"])/total), 
                       "Team 2": 1/((scores["0-2"]+scores["1-2"])/total), 
                       "2-0": 1/(scores["2-0"]/total), 
                       "2-1": 1/(scores["2-1"]/total), 
                       "0-2": 1/(scores["0-2"]/total), 
                       "1-2": 1/(scores["1-2"]/total),
                       "Over": 1/((scores["2-1"]+scores["1-2"])/total), 
                       "Under": 1/((scores["2-0"]+scores["0-2"])/total), 
                       "Team 1 (+1.5)": 1/((scores["2-0"]+scores["2-1"]+scores["1-2"])/total), 
                       "Team 2 (+1.5)": 1/((scores["0-2"]+scores["1-2"]+scores["2-1"])/total) }

            odds = pd.DataFrame(chances, index=['vs ' + t2])
            odds = odds.round(3)

            # print(odds)

            #Append to CSV after each matchup. Need to create a blank XLSX file first.
            with pd.ExcelWriter("./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-oddsTrainDataFORLCQ.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                odds.to_excel(writer, sheet_name=team1, startrow=row) 


            print(t1, t2)
            row += 4
