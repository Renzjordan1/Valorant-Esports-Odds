from data import *
from classes import *
import random, math


#Calculate the win % for each team
def calc_win_percent(p1, p2, round):

    #Team win/loss %
    p1_probW = 0
    p2_probW = 0
    p1_probL = 0
    p2_probL = 0

    #Combined Win/loss % of all teams in the league
    nat1_probW = 0
    nat2_probW = 0

    ##PISTOL ROUND
    if(round == 1 or round == 13):
        p1_probW = pistol[(pistol.Team == p1.name)]['Win %'].values[0]
        p2_probW = pistol[(pistol.Team == p2.name)]['Win %'].values[0]
        nat1_probW = pistol[(pistol.Team.isnull())]['Win %'].values[0]
        nat2_probW = pistol[(pistol.Team.isnull())]['Win %'].values[0]
        # print("pistol", round)

    
    ##SMG VS ECO ROUND
    elif(round == 2 or round == 14):
        if(p1.prevEcon > p2.prevEcon):
            p1_probW = smg_eco[(smg_eco.Team == p1.name)]['Win %'].values[0]
            p2_probW = eco_smg[(eco_smg.Team == p2.name)]['Win %'].values[0]
            nat1_probW = smg_eco[(smg_eco.Team.isnull())]['Win %'].values[0]
            nat2_probW = eco_smg[(eco_smg.Team.isnull())]['Win %'].values[0]
        else:
            p2_probW = smg_eco[(smg_eco.Team == p2.name)]['Win %'].values[0]
            p1_probW = eco_smg[(eco_smg.Team == p1.name)]['Win %'].values[0]
            nat2_probW = smg_eco[(smg_eco.Team.isnull())]['Win %'].values[0]
            nat1_probW = eco_smg[(eco_smg.Team.isnull())]['Win %'].values[0]
        # print("smg v eco", round)


    ##BONUS VS BUY ROUND
    elif((round == 3 or round == 15) and p1.WS + p2.WS == 2):
        if(p1.WS == 2):
            p1_probW = bonus_buy[(bonus_buy.Team == p1.name)]['Win %'].values[0]
            p2_probW = buy_bonus[(buy_bonus.Team == p2.name)]['Win %'].values[0]
            nat1_probW = bonus_buy[(bonus_buy.Team.isnull())]['Win %'].values[0]
            nat2_probW = buy_bonus[(buy_bonus.Team.isnull())]['Win %'].values[0]
        else:
            p2_probW = bonus_buy[(bonus_buy.Team == p2.name)]['Win %'].values[0]
            p1_probW = buy_bonus[(buy_bonus.Team == p1.name)]['Win %'].values[0]
            nat2_probW = bonus_buy[(bonus_buy.Team.isnull())]['Win %'].values[0]
            nat1_probW = buy_bonus[(buy_bonus.Team.isnull())]['Win %'].values[0]
        # print("bonus", round)


    ##POST 2ND ROUND THRIFTY
    elif((round == 3 or round == 15) and p1.WS + p2.WS == 1):
        if(p1.WS == 1):
            p1_probW = smg_eco[(smg_eco.Team == p1.name)]['Win %'].values[0]
            p2_probW = eco_smg[(eco_smg.Team == p2.name)]['Win %'].values[0]
            nat1_probW = smg_eco[(smg_eco.Team.isnull())]['Win %'].values[0]
            nat2_probW = eco_smg[(eco_smg.Team.isnull())]['Win %'].values[0]
        else:
            p2_probW = smg_eco[(smg_eco.Team == p2.name)]['Win %'].values[0]
            p1_probW = eco_smg[(eco_smg.Team == p1.name)]['Win %'].values[0]
            nat2_probW = smg_eco[(smg_eco.Team.isnull())]['Win %'].values[0]
            nat1_probW = eco_smg[(eco_smg.Team.isnull())]['Win %'].values[0]
        # print("thrifted", round)

    ##REST OF ROUNDS
    else:
        if(p2.econ == 8500 and p2.WS == 0):
            p1_probW = (rifle_thrift[(rifle_thrift.Team == p1.name)]['Win %'].values[0] + rifle_half[(rifle_half.Team == p1.name)]['Win %'].values[0]) / 2
            p2_probW = (thrift_rifle[(thrift_rifle.Team == p2.name)]['Win %'].values[0] + half_rifle[(half_rifle.Team == p2.name)]['Win %'].values[0]) / 2
            nat1_probW = (rifle_thrift[(rifle_thrift.Team.isnull())]['Win %'].values[0] + rifle_half[(rifle_half.Team.isnull())]['Win %'].values[0]) / 2
            nat2_probW = (thrift_rifle[(thrift_rifle.Team.isnull())]['Win %'].values[0] + half_rifle[(half_rifle.Team.isnull())]['Win %'].values[0]) / 2
            # print("rifle vs thrift", round)

        elif(p1.econ == 8500 and p1.WS == 0):
            p2_probW = (rifle_thrift[(rifle_thrift.Team == p2.name)]['Win %'].values[0] + rifle_half[(rifle_half.Team == p2.name)]['Win %'].values[0]) / 2
            p1_probW = (thrift_rifle[(thrift_rifle.Team == p1.name)]['Win %'].values[0] + half_rifle[(half_rifle.Team == p1.name)]['Win %'].values[0]) / 2
            nat2_probW = (rifle_thrift[(rifle_thrift.Team.isnull())]['Win %'].values[0] + rifle_half[(rifle_half.Team.isnull())]['Win %'].values[0]) / 2
            nat1_probW = (thrift_rifle[(thrift_rifle.Team.isnull())]['Win %'].values[0] + half_rifle[(half_rifle.Team.isnull())]['Win %'].values[0]) / 2
            # print("thrift vs rifle", round)

        elif(((p1.prevEcon < 20000 and p1.WS == 0) or (p2.prevEcon < 20000 and p2.WS == 0))):
            if(p1.WS == 0):
                p2_probW = (rifle_half[(rifle_half.Team == p2.name)]['Win %'].values[0] + rifle[(rifle.Team == p2.name)]['Win %'].values[0]) / 2
                p1_probW = (half_rifle[(half_rifle.Team == p1.name)]['Win %'].values[0] + rifle[(rifle.Team == p1.name)]['Win %'].values[0]) /  2
                nat2_probW = (rifle_half[(rifle_half.Team.isnull())]['Win %'].values[0] + rifle[(rifle.Team.isnull())]['Win %'].values[0]) / 2
                nat1_probW = (half_rifle[(half_rifle.Team.isnull())]['Win %'].values[0] + rifle[(rifle.Team.isnull())]['Win %'].values[0]) / 2
                # print("half vs rifle", round)
            else:
                p1_probW = (rifle_half[(rifle_half.Team == p1.name)]['Win %'].values[0] + rifle[(rifle.Team == p1.name)]['Win %'].values[0]) / 2
                p2_probW = (half_rifle[(half_rifle.Team == p2.name)]['Win %'].values[0] + rifle[(rifle.Team == p2.name)]['Win %'].values[0]) /  2
                nat1_probW = (rifle_half[(rifle_half.Team.isnull())]['Win %'].values[0] + rifle[(rifle.Team.isnull())]['Win %'].values[0]) / 2
                nat2_probW = (half_rifle[(half_rifle.Team.isnull())]['Win %'].values[0] + rifle[(rifle.Team.isnull())]['Win %'].values[0]) / 2
                # print("rifle vs half", round)


        ##RIFLE ROUND
        # if(p1.prevEcon >=20000 and p2.prevEcon>=20000):
        else:
            p1_probW = rifle[(rifle.Team == p1.name)]['Win %'].values[0]
            p2_probW = rifle[(rifle.Team == p2.name)]['Win %'].values[0]
            nat1_probW = rifle[(rifle.Team.isnull())]['Win %'].values[0]
            nat2_probW = rifle[(rifle.Team.isnull())]['Win %'].values[0]
            # print("rifle", round)

    

    #Get expected win/loss % for the matchup
    p1_probL = 1 - p1_probW
    p2_probL = 1 - p2_probW
    # p1_exp_probW = p1_probW + p2_probL - nat1_probW
    # p2_exp_probW = p2_probW + p1_probL - nat2_probW
    p1_exp_probW = (p1_probW + p2_probL) / (p1_probW + p2_probW + p1_probL + p2_probL)
    p2_exp_probW = (p2_probW + p1_probL) / (p1_probW + p2_probW + p1_probL + p2_probL)

    # print(p1_exp_probW, p2_exp_probW)

    return p1_exp_probW, p2_exp_probW



#Choose a winner of the round using win %
def calc_winner(p1, p2, p1_exp_probW, p2_exp_probW):

    roundWinner = random.choices([p1, p2], weights=(p1_exp_probW, p2_exp_probW), k=1)[0]

    if(roundWinner == p1):
        roundLoser = p2
    else:
        roundLoser = p1

    # print(roundWinner.name + " Wins!")
    return roundWinner, roundLoser


#Adjust economy of both teams
def round_econ(roundWinner, roundLoser):

    if(roundWinner.WS == 0):
        roundLoser.econ += 9500

    elif(roundWinner.WS == 1):
        roundLoser.econ += 12000

    else:
        roundLoser.econ += 14500

    roundWinner.econ  += 15000


#Get probabilities of each win condition for the round
def determine_round_cond(roundWinner, roundLoser, atk):
    if(roundWinner == atk):
        bomb = (conds.loc[roundWinner.name, "bomb"]["ATK W Tendency"] + conds.loc[roundLoser.name, "bomb"]["DEF L Tendency"]) / 2
        post = (conds.loc[roundWinner.name, "kills (post-plant)"]["ATK W Tendency"] + conds.loc[roundLoser.name, "kills (post-plant)"]["DEF L Tendency"]) / 2
        pre = (conds.loc[roundWinner.name, "kills (pre-plant)"]["ATK W Tendency"] + conds.loc[roundLoser.name, "kills (pre-plant)"]["DEF L Tendency"]) / 2
        time = (conds.loc[roundWinner.name, "time"]["ATK W Tendency"] + conds.loc[roundLoser.name, "time"]["DEF L Tendency"]) / 2

    else:
        bomb = (conds.loc[roundWinner.name, "bomb"]["DEF W Tendency"] + conds.loc[roundLoser.name, "bomb"]["ATK L Tendency"]) / 2
        post = (conds.loc[roundWinner.name, "kills (post-plant)"]["DEF W Tendency"] + conds.loc[roundLoser.name, "kills (post-plant)"]["ATK L Tendency"]) / 2
        pre = (conds.loc[roundWinner.name, "kills (pre-plant)"]["DEF W Tendency"] + conds.loc[roundLoser.name, "kills (pre-plant)"]["ATK L Tendency"]) / 2
        time = (conds.loc[roundWinner.name, "time"]["DEF W Tendency"] + conds.loc[roundLoser.name, "time"]["ATK L Tendency"]) / 2

    return bomb, post, pre, time


#Adjust econ based on the win condition of the round
def bomb_kill_econ(roundCond, atk, defe, roundWinner, roundLoser):   

    atk_killCreds = 1000
    defe_killCreds = 1000

    #Kill creds are determined by number of kills * 200. The probability weight for an amount of kills were determined by me based off the meta in early 2022 
    # and may not be very accurate.

    if(roundCond == "bomb"):

        #Get creds from kills
        atk_killCreds = random.choices([0, 200, 400, 600, 800, 1000], weights=(0, 0, 5, 20, 70, 5), k=1)[0]
        defe_killCreds = random.choices([0, 200, 400, 600, 800, 1000], weights=(15, 15, 15, 15, 20, 20), k=1)[0]

        #Bomb plant for ATK ($1500) + kill creds. ATK wins by bomb time, DEF attempts to save or can't defuse bomb.
        atk.econ += (1500 + atk_killCreds)
        defe.econ += defe_killCreds

        # print("bomb")

    
    elif(roundCond == "post"):

        #Get creds from kills for loser
        if(roundLoser == defe):
            defe_killCreds = random.choices([0, 200, 400, 600, 800, 1000], weights=(10, 10, 20, 25, 35, 0), k=1)[0]
            roundLoser.econ += defe_killCreds
        else:
            atk_killCreds = random.choices([0, 200, 400, 600, 800, 1000], weights=(10, 10, 20, 25, 35, 0), k=1)[0]
            roundLoser.econ += atk_killCreds

        #Winner kills 5 ($1000). Bomb plant for ATK ($1500). ATK wins by killing all in post-plant or DEF wins by defuse
        roundWinner.econ += 1000
        atk.econ += 1500

        # print("post")


    elif(roundCond == "pre"):

        #Get creds from kills for loser
        if(roundLoser == defe):
            defe_killCreds = random.choices([0, 200, 400, 600, 800, 1000], weights=(10, 10, 20, 25, 35, 0), k=1)[0]
            roundLoser.econ += defe_killCreds
        else:
            atk_killCreds = random.choices([0, 200, 400, 600, 800, 1000], weights=(10, 10, 20, 25, 35, 0), k=1)[0]
            roundLoser.econ += atk_killCreds

        #Winner gets 5 * 200 kill creds. DEF wins by killing all in pre-plant
        roundWinner.econ += 1000

        # print("pre")


    else:

        #Get creds from kills 
        defe_killCreds = random.choices([0, 200, 400, 600, 800, 1000], weights=(0, 0, 5, 20, 75, 0), k=1)[0]
        atk_killCreds = random.choices([0, 200, 400, 600, 800, 1000], weights=(35, 30, 20, 10, 5, 0), k=1)[0]

        #DEF wins by ATK side saving. 
        defe.econ += defe_killCreds
        atk.econ += atk_killCreds

        # print("time")
    

    #Maximum money
    if(roundWinner.econ > 45000):
        roundWinner.econ = 45000
    if(roundLoser.econ > 45000):
        roundLoser.econ = 45000
    

    #Set number of deaths
    atk.set_deaths(defe_killCreds)
    defe.set_deaths(atk_killCreds)


#Adjust econ for item buys for each round
#Buys are determined by me based off the meta in early 2022 and may not be very accurate
def buy_items(round, p1, p2, roundWinner, roundLoser):

    #AFTER Pistol
    if(round == 1 or round == 13):

        #Winner buys 4 Spectres, Util, 3 Half-Shield, 2 Full-Shield
        roundWinner.econ -= ((1600 * 4) + (500 * 5) + (400 * 3 + 1000 * 2))

        #Loser Ecos
        roundLoser.econ = 8500
    
    #AFTER 2nd Round (SMG vs ECO) (Exam. Score: 2-0)
    elif((round == 2 or round == 14) and p1.WS + p2.WS == 2):

        #Winner rebuy Rifles, Util, and Full-Shield
        roundWinner.econ -= ((2900 * roundWinner.deaths) + (500 * 5) + (1000 * roundWinner.deaths))

        #Only buy Half-Shield, Bulldog if not enough money
        while(roundWinner.deaths > 0 and roundWinner.econ < 0):
            roundWinner.econ += (600 + 850)
            roundWinner.deaths -= 1

        #Loser rebuy Rifles, Util, and Full-Shield
        roundLoser.econ -= ((2900 * roundLoser.deaths) + (500 * 5) + (1000 * roundLoser.deaths))

        #Only buy Half-Shield, Bulldog if not enough money
        while(roundLoser.deaths > 0 and roundLoser.econ < 0):
            roundLoser.econ += (600 + 850)
            roundLoser.deaths -= 1

    #AFTER 2nd Round Eco Win (Exam. Score: 1-1)
    elif((round == 2 or round == 14) and p1.WS + p2.WS == 1):

        #Winner rebuy Rifles, Util, and Full-Shield
        roundWinner.econ -= ((2900 * roundWinner.deaths) + (500 * 5) + (1000 * 5))

        #Only buy Half-Shield, Bulldog if not enough money
        while(roundWinner.deaths > 0 and roundWinner.econ < 0):
            roundWinner.econ += (600 + 850)
            roundWinner.deaths -= 1

        #Loser Ecos
        roundLoser.econ = 8500

    #OVERTIME
    elif(round>=24):
        p1.econ = 25000
        p2.econ = 25000

    #AFTER 4th
    else:

        #Loser has enough for Rifle Round
        if(roundLoser.econ >= 20000):

            #Loser rebuy Rifles, Util, and Full-Shield
            roundLoser.econ -= ((2900 * roundLoser.deaths) + (500 * 5) + (1000 * roundLoser.deaths))

            #Only buy Half-Shield, Spectre if not enough money
            while(roundLoser.deaths > 0 and roundLoser.econ < 0):
                roundLoser.econ += (600 + 1300)
                roundLoser.deaths -= 1
           
        #Loser doesn't have enough for rifles
        else:
            
            #Force if need to win or saved last round or last round
            if(roundWinner.wins == 12 or roundLoser.deaths != 5 or round == 11):

                #Loser rebuy Rifles, Some Util, and Half-Shield
                roundLoser.econ -= ((2900 * roundLoser.deaths) + (300 * 5) + (400 * roundLoser.deaths))

                #Only buy No Shield, Spectre if not enough money
                while(roundLoser.deaths > 0 and roundLoser.econ < 0):
                    roundLoser.econ += (400 + 1300)
                    roundLoser.deaths -= 1

                #Don't allow econ to equal 8500 (value used to determine eco round)
                if(roundLoser.econ == 8500):
                    roundLoser.econ = 8400

            #Loser Ecos
            else:
                roundLoser.econ = 8500

        #Winner rebuy Rifles, Util, and Full-Shield
        roundWinner.econ -= ((2900 * roundWinner.deaths) + (500 * 5) + (1000 * roundWinner.deaths))

        #Only buy Half-Shield, Bulldog if not enough money
        while(roundWinner.deaths > 0 and roundWinner.econ < 0):
            roundWinner.econ += (600 + 850)
            roundWinner.deaths -= 1


#Simulate a round
def play_round(p1, p2, round):
    # print("START:", p1.prevEcon, p2.prevEcon)

    p1_exp_probW = 0
    p2_exp_probW = 0


    #SET SIDES
    if(round < 13):
        atk = p1
        defe = p2

    if(round >= 13):
        atk = p2
        defe = p1
    
    
    if(round == 13):
        p1.reset_econ()
        p2.reset_econ()


    #Get win %s
    p1_exp_probW, p2_exp_probW = calc_win_percent(p1, p2, round)
    # print(p1_exp_probW, p2_exp_probW)
    

    #DETERMINE ROUND WINNER
    roundWinner, roundLoser = calc_winner(p1, p2, p1_exp_probW, p2_exp_probW)
    # print(roundWinner, roundLoser)


    #ROUND WIN ECONOMY
    round_econ(roundWinner, roundLoser)


    #ROUND CONDITION
    bomb, post, pre, time = determine_round_cond(roundWinner, roundLoser, atk)


    #Adjust Econ for BOMB PLACED and KILLS
    roundCond = random.choices(["bomb", "post", "pre", "time"], weights=(bomb, post, pre, time), k=1)[0]
    bomb_kill_econ(roundCond, atk, defe, roundWinner, roundLoser)
    # print("P1 Deaths: " , p1.deaths , "   P2 Deaths: " , p2.deaths)


    #NEW ECON FROM ROUND END
    p1.set_prevEcon()
    p2.set_prevEcon()
    # print("END:", p1.prevEcon, p2.prevEcon)


    #SET WIN STREAK
    roundWinner.set_wins(True)
    roundLoser.set_wins(False)
    # print("1WS: ", p1.WS, "2WS: ", p2.WS)


    #MONEY SPENT FOR NEXT ROUND (Guns + Util + Armor)
    buy_items(round, p1, p2, roundWinner, roundLoser)


    # print("BOUGHT:", p1.econ, p2.econ)
    # print("\n")
    # print(bomb, post, pre, time)

    # print(roundWinner.name)
    # print(p1.wins, p2.wins, "\n")
    round += 1


    #Recusive call until winner is determined
    if(p1.wins<13 and p2.wins<13):
        return play_round(p1, p2, round)
    
    elif(abs(p1.wins - p2.wins) < 2):
        return play_round(p1, p2, round)
    
    else:
        if(p1.wins>p2.wins):
            # print("Winner: " + p1.name)
            return "1", round-1
        else:
            # print("Winner: " + p2.name)
            return "2", round-1
        print(p1.wins, p2.wins)
    


