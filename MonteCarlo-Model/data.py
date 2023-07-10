import pandas as pd
import matplotlib.pyplot as plt

#W-L Round Data
pistol = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-PistolRoundWL.csv') 
smg_eco = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-SMGvEcoRoundWL.csv')
eco_smg = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-EcovSMGRoundWL.csv') 
bonus_buy = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-BonusVBuyRoundWL.csv') 
buy_bonus = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-BuyVBonusRoundWL.csv')        
rifle = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-RifleVRifleRoundWL.csv')   
rifle_half = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-RifleVHalfRoundWL.csv') 
half_rifle = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-HalfVRifleRoundWL.csv')     
rifle_thrift = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-RifleVThriftRoundWL.csv')   
thrift_rifle = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-ThriftVRifleRoundWL.csv')     


#Total W-L for each round type
pistol.loc["Total"] = pistol.sum(numeric_only=True)
smg_eco.loc["Total"] = smg_eco.sum(numeric_only=True)
eco_smg.loc["Total"] = eco_smg.sum(numeric_only=True)
bonus_buy.loc["Total"] = bonus_buy.sum(numeric_only=True)
buy_bonus.loc["Total"] = buy_bonus.sum(numeric_only=True)
rifle.loc["Total"] = rifle.sum(numeric_only=True)
rifle_half.loc["Total"] = rifle_half.sum(numeric_only=True)
half_rifle.loc["Total"] = half_rifle.sum(numeric_only=True)
rifle_thrift.loc["Total"] = rifle_thrift.sum(numeric_only=True)
thrift_rifle.loc["Total"] = thrift_rifle.sum(numeric_only=True)


#WIN % and LOSS % for each round type
pistol['Win %'] = pistol['Wins'] / (pistol['Wins'] + pistol['Losses'])
smg_eco['Win %'] = smg_eco['Wins'] / (smg_eco['Wins'] + smg_eco['Losses'])
eco_smg['Win %'] = eco_smg['Wins'] / (eco_smg['Wins'] + eco_smg['Losses'])
bonus_buy['Win %'] = bonus_buy['Wins'] / (bonus_buy['Wins'] + bonus_buy['Losses'])
buy_bonus['Win %'] = buy_bonus['Wins'] / (buy_bonus['Wins'] + buy_bonus['Losses'])
rifle['Win %'] = rifle['Wins'] / (rifle['Wins'] + rifle['Losses'])
rifle_half['Win %'] = rifle_half['Wins'] / (rifle_half['Wins'] + rifle_half['Losses'])
half_rifle['Win %'] = half_rifle['Wins'] / (half_rifle['Wins'] + half_rifle['Losses'])
rifle_thrift['Win %'] = rifle_thrift['Wins'] / (rifle_thrift['Wins'] + rifle_thrift['Losses'])
thrift_rifle['Win %'] = thrift_rifle['Wins'] / (thrift_rifle['Wins'] + thrift_rifle['Losses'])

pistol['Loss %'] = 1 - pistol['Win %']
smg_eco['Loss %'] = 1 - smg_eco['Win %']
eco_smg['Loss %'] = 1 - eco_smg['Win %']
bonus_buy['Loss %'] = 1 - bonus_buy['Win %']
buy_bonus['Loss %'] = 1 - buy_bonus['Win %']
rifle['Loss %'] = 1 - rifle['Win %']
rifle_half['Loss %'] = 1 - rifle_half['Win %']
half_rifle['Loss %'] = 1 - half_rifle['Win %']
rifle_thrift['Loss %'] = 1 - rifle_thrift['Win %']
thrift_rifle['Loss %'] = 1 - thrift_rifle['Win %']


#See Win % Rankings
# pistol = pistol.sort_values('Win %')
# smg_eco = smg_eco.sort_values('Win %')
# eco_smg = eco_smg.sort_values('Win %')
# bonus_buy = bonus_buy.sort_values('Win %')
# buy_bonus = buy_bonus.sort_values('Win %')
# rifle = rifle.sort_values('Win %')
# rifle_thrift = rifle_thrift.sort_values('Win %')
# thrift_rifle = thrift_rifle.sort_values('Win %')


#Round Tendency Data
# condsOrig = pd.read_csv ('./NA-VCTChal1/Group (Wk 1-5)/NA-VCTChal1-WinConds.csv')   
condsOrig = pd.read_csv ('./NA-VCTChal2/train (FULL Wk 1-5)/NA-VCTChal2-WinConds.csv')   


#Get Total Games
condsTot = condsOrig.groupby(['Team']).sum()


#Tendency of how teams win or lose a round
condsOrig = condsOrig.replace(to_replace = "defuse", value = "kills (post-plant)")
conds = condsOrig.groupby(['Team', 'Condition']).sum()
conds['ATK W Tendency'] = (conds['Attacking Wins']) / (condsTot['Attacking Wins'])
conds['DEF W Tendency'] = (conds['Defending Wins']) / (condsTot['Defending Wins'])
conds['ATK L Tendency'] = (conds['Attacking Losses']) / (condsTot['Attacking Losses'])
conds['DEF L Tendency'] = (conds['Defending Losses']) / (condsTot['Defending Losses'])



#Test Code
'''df = pd.DataFrame(data)
df['Total']= df['Wins'] + df['Losses']

df2 = df[(df.Situation == "5v4") | (df.Situation == "4v5") ]
df2 = df2.groupby(['Team']).sum()
df2 = df2.Total

print(df2)


dfFK = df[(df.Situation == "5v4")]
dfFK['FKRound'] = dfFK['Total'].divide(df2.values)*100
print(dfFK)


dfFD = df[(df.Situation == "4v5")]
dfFD['FDRound'] = dfFD['Total'].divide(df2.values)*100
print(dfFD)
'''


print("PISTOL\n", pistol, "\n" + "-"*45 + "\n")
print("SMG vs. ECO\n",smg_eco, "\n" + "-"*45 + "\n")
print("ECO vs. SMG\n",eco_smg, "\n" + "-"*45 + "\n")
print("Bonus vs. Buy\n",bonus_buy, "\n" + "-"*45 + "\n")
print("Buy vs. Bonus\n",buy_bonus, "\n" + "-"*45 + "\n")
print("Rifle vs. Rifle\n",rifle, "\n" + "-"*45 + "\n")
print("Rifle vs. Half\n",rifle_half, "\n" + "-"*45 + "\n")
print("Half vs. Rifle\n",half_rifle, "\n" + "-"*45 + "\n")
print("Rifle vs. Thrift\n",rifle_thrift, "\n" + "-"*45 + "\n")
print("Thrift vs. Rifle\n",thrift_rifle, "\n" + "-"*45 + "\n")


print(conds)






