# Valorant Esports Odds - Spring 2022 (Updated Summer 2023)
> Monte-Carlo Model for simulating Pro Valorant Matches

The purpose of this project is to create a betting model that can used for the e-sport Valorant. Valorant Champions Tour (VCT) is the professional Valorant league where there is weekly regional games that lead to regional playoff tournaments and then international tournaments.

Using round win-loss data of how teams perform in different round types (Pistol round, Full Buy round, etc.) from the weekly regional matches (received from the [rib.gg](https://www.rib.gg/) Discord bot), the Monte-Carlo Model simulates a game of Valorant between two teams. The simulation goes round by round (first to 13), adjusting the economies of each team based off what happened in the simulated round in order to determine what each team's next round type will be. 

Each team matchup is simulated as a Best of 3 many times to get the odds of each outcome. *This can really only confidently work with regional matches since that is what the win-loss data is from.* 



<br/>

## Results

* Odds Result example:

  ![image](https://github.com/Renzjordan1/Valorant-Esports-Odds/assets/38296706/494c5751-86d8-4047-b301-5c973c180bc1)

<br/>

  

* Back Test (from VCT North America Challengers 2 - 2022)

  * By theoretically placing bets based (using Kelly-Criterion to size each bet) solely on what the model determined to have the highest expected value during VCT North America Challengers 2 - 2022, there was a return of **11.72%**.

    ![image](https://github.com/Renzjordan1/Valorant-Esports-Odds/assets/38296706/f86a19bf-dd4c-4d5d-8b74-b13751019a5a)



  * By doing the same but with placing more probable bets with slightly less expected value as the highest, there was a return of **66.62%**. Though, hindsight
   is 20/20.
 
    ![image](https://github.com/Renzjordan1/Valorant-Esports-Odds/assets/38296706/2fc07898-ede7-4b89-86c0-0a6e15510785)


  ****There is no guarantee that this will be the actual result for future bets.***

  Since this model is based on past results the odds it calculates may not be accurate to a current matches' actual odds as teams could start
  to out or under perform or data from other matches aren't included (past does not indicate future results).
  ***Ex.)** The heavy favorites from the regular season, Ghost Gaming, loses both of their matches in the Playoffs 0-2*
  
   As such, the model may be best used as support in addition to the bettor's knowledge and risk tolerance as seen with the much higher returns when the model was used but with an individual strategy.

  *NOTE: The sportsbook odds data was manually gathered at the time a line was open. Some lines were missed and aren't able to be included.*
  
  

  





<br/>

## How to Run on your Local Machine 
Clone:

```sh
git clone https://github.com/Renzjordan1/Valorant-Esports-Odds/
```

Run :

* To get odds:
```
python testerRun.py
```

* To get data:
```
Copy and paste commands from ribCommands.docx into the rib.gg Discord bot. Edit the event id for the event you want round data for.
```



## Tech Stack

* Python
